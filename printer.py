import serial
import time
from PIL import Image


def print_text(text, com_port, baud_rate):
    """Send text to the DPU-414 printer."""

    try:
        with serial.Serial(
            com_port,
            int(baud_rate),
            timeout=1
        ) as ser:

            ser.write(text.encode("cp865"))
            ser.write(b"\n")
            ser.flush()

    except serial.SerialTimeoutException:
        print("Write timeout occurred.")

    except serial.SerialException as e:
        print(f"Serial error: {e}")

    except Exception as e:
        print(f"Error: {e}")


def print_image(image_path, com_port, baud_rate):
    """Print an image on the Seiko DPU-414."""

    try:
        # ------------------------------------------------------------
        # Load image
        # ------------------------------------------------------------
        img = Image.open(image_path).convert("L")

        # ------------------------------------------------------------
        # DPU-414 graphics width
        #
        # The DPU-414 has 320 horizontal dots.
        # ------------------------------------------------------------
        max_width = 320

        # Scale image down proportionally if necessary
        if img.width > max_width:

            ratio = max_width / img.width

            new_height = max(
                1,
                int(img.height * ratio)
            )

            img = img.resize(
                (max_width, new_height),
                Image.Resampling.LANCZOS
            )

        # Convert to 1-bit black and white
        img = img.convert("1")

        print(f"Image size: {img.width} x {img.height}")

        # ------------------------------------------------------------
        # Open serial connection
        # ------------------------------------------------------------
        with serial.Serial(
            port=com_port,
            baudrate=int(baud_rate),
            timeout=2,
            write_timeout=5
        ) as ser:

            # --------------------------------------------------------
            # IMPORTANT
            #
            # Set the printer's line-feed distance to 8 dots.
            #
            # ESC A n
            #
            # ESC = 0x1B
            # A   = 0x41
            # n   = 8
            #
            # The graphics command produces an 8-dot-high row,
            # so the normal LF must advance exactly 8 dots.
            # --------------------------------------------------------

            ser.write(b"\x1B\x41\x08")
            ser.flush()

            # --------------------------------------------------------
            # Print image 8 vertical pixels at a time
            # --------------------------------------------------------
            for y in range(0, img.height, 8):

                line_data = bytearray()

                # ----------------------------------------------------
                # Build one graphics row
                # ----------------------------------------------------
                for x in range(img.width):

                    byte = 0

                    for bit in range(8):

                        py = y + bit

                        if py < img.height:

                            pixel = img.getpixel((x, py))

                            # PIL mode "1":
                            #
                            # 0   = black
                            # 255 = white
                            #
                            if pixel == 0:
                                byte |= (1 << (7 - bit))

                    line_data.append(byte)

                # ----------------------------------------------------
                # ESC K n1 n2
                #
                # n1 + n2 specify the number of image bytes.
                # ----------------------------------------------------

                data_length = len(line_data)

                n1 = data_length & 0xFF
                n2 = (data_length >> 8) & 0xFF

                command = bytes([
                    0x1B,       # ESC
                    0x4B,       # K
                    n1,
                    n2
                ])

                # Send graphics command
                ser.write(command)

                # Send graphics data
                ser.write(line_data)

                # ----------------------------------------------------
                # Move exactly one graphics row down.
                #
                # Because ESC A 8 was set above, LF now advances
                # exactly 8 dots instead of the printer's default
                # line spacing.
                # ----------------------------------------------------

                ser.write(b"\x0A")

                ser.flush()

                # Give the printer a little time to process the data
                time.sleep(0.05)

        print("Image sent successfully.")

    except serial.SerialTimeoutException:
        print("Write timeout occurred.")

    except serial.SerialException as e:
        print(f"Serial error: {e}")

    except Exception as e:
        print(f"Error: {e}")

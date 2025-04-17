import serial
import time
from PIL import Image, ImageDraw

def print_text(text, com_port, baud_rate):
    with serial.Serial(com_port, baud_rate, timeout=1) as ser:
        ser.write(text.encode('cp865') + b'\n')

def print_image(image_path, com_port, baud_rate):
    try:
           # Load image and convert to 1-bit black & white
           img = Image.open(image_path).convert('1')

           # Resize to printer max width (DPU-414: 832 px)
           max_width = 300
           # Always resize proportionally to fit width
           ratio = max_width / img.width
           new_height = int(img.height * ratio)
           img = img.resize((max_width, new_height))

           # Convert to 1-bit black & white (again, after resize)
           img = img.convert('1')


           print(f"Image size: {img.width}x{img.height}")

           with serial.Serial(com_port, baud_rate, timeout=2, write_timeout=5) as ser:
               for y in range(0, img.height, 8):
                   line_data = bytearray()

                   for x in range(img.width):
                       byte = 0
                       for bit in range(8):
                           py = y + bit
                           if py < img.height:
                               pixel = img.getpixel((x, py))
                               if pixel == 0:
                                   byte |= (1 << (7 - bit))
                       line_data.append(byte)

                   n1 = len(line_data) & 0xFF
                   n2 = (len(line_data) >> 8) & 0xFF
                   esc_k = b'\x1B\x4B' + bytes([n1, n2])

                   # Send line
                   ser.write(esc_k + line_data + b'\n')
                   ser.flush()           # ensure everything is sent
                   time.sleep(0.1)       # wait before sending next line

               print("Image sent successfully.")

    except serial.SerialTimeoutException:
        print("Write timeout occurred.")
    except Exception as e:
        print(f"Error: {e}")

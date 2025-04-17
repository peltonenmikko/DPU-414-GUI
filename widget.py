from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtCore import Qt  # Added Qt import for AspectRatioMode and TransformationMode
from pathlib import Path
import serial
from ui_form import Ui_Form  # Import generated UI class for form.ui
from ui_text_print import Ui_TextPrint  # Import generated UI class for text_print.ui
from ui_image_print import Ui_ImagePrint  # Import generated UI class for image_print.ui
from printer import print_text, print_image  # Ensure this module exists

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()  # Use the generated UI class for the main window
        self.ui.setupUi(self)  # Setup the UI on the widget
        self.setWindowIcon(QIcon("dpu414.ico"))

        # Populate COM ports and baud rates when initializing the widget
        self.populate_com_ports()
        self.populate_baud_rates()

        self.ui.btnPrintText.clicked.connect(self.open_text_window)
        self.ui.btnPrintImage.clicked.connect(self.open_image_window)

    def populate_com_ports(self):
        """Populate COM port combo box with available serial ports."""
        available_ports = self.get_available_com_ports()
        self.ui.comboComPort.addItems(available_ports)

    def get_available_com_ports(self):
        """Get a list of available COM ports."""
        import serial.tools.list_ports
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def populate_baud_rates(self):
        """Populate baud rate combo box with common baud rates."""
        baud_rates = ['9600', '19200', '38400', '57600', '115200']
        self.ui.comboBaudRate.addItems(baud_rates)

    def open_text_window(self):
        # Create a new window for text print
        self.setWindowIcon(QIcon("dpu414.ico"))
        self.text_window = QWidget()  # New QWidget instance for text print
        self.text_window_ui = Ui_TextPrint()  # Create the UI object for text print
        self.text_window_ui.setupUi(self.text_window)  # Set up the UI on the text window widget
        self.text_window_ui.btnPrintText.clicked.connect(self.send_text_to_printer)

        # Show the text window
        self.text_window.show()

    def open_image_window(self):
        # Create a new window for image print
        self.setWindowIcon(QIcon("dpu414.ico"))
        self.image_window = QWidget()  # New QWidget instance for image print
        self.image_window_ui = Ui_ImagePrint()  # Create the UI object for image print
        self.image_window_ui.setupUi(self.image_window)  # Set up the UI on the image window widget
        self.image_window_ui.btnBrowse.clicked.connect(self.browse_image)
        self.image_window_ui.btnPrintImage.clicked.connect(self.send_image_to_printer)

        # Show the image window
        self.image_window.show()

    def send_text_to_printer(self):
        text = self.text_window_ui.textEdit.toPlainText()  # Get text input
        try:
            # Use selected COM port and baud rate
            com_port = self.ui.comboComPort.currentText()
            baud_rate = self.ui.comboBaudRate.currentText()
            print_text(text, com_port, baud_rate)
            QMessageBox.information(self, "Success", "Text sent to printer!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def browse_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.image_window_ui.lineImagePath.setText(file_path)

            # Load the image
            image = QPixmap(file_path)

            # Convert the image to black and white (grayscale)
            image = image.toImage().convertToFormat(QImage.Format_Grayscale8)

            # Convert back to QPixmap to display in the preview
            pixmap_bw = QPixmap.fromImage(image)

            # Get the current size of the preview label
            label_size = self.image_window_ui.labelPreview.size()

            # Scale the image to fit within the label size while keeping the aspect ratio
            pixmap_scaled = pixmap_bw.scaled(label_size, Qt.AspectRatioMode.KeepAspectRatio)

            # Set the scaled image to the preview label
            self.image_window_ui.labelPreview.setPixmap(pixmap_scaled)

    def send_image_to_printer(self):
        path = self.image_window_ui.lineImagePath.text()  # Get the image path
        if not Path(path).exists():
            QMessageBox.critical(self, "Error", "Image file not found.")
            return
        try:
            # Use selected COM port and baud rate
            com_port = self.ui.comboComPort.currentText()
            baud_rate = self.ui.comboBaudRate.currentText()
            print_image(path, com_port, baud_rate)
            QMessageBox.information(self, "Success", "Image sent to printer!")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    app.exec()

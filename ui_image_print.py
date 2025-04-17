# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_print.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_ImagePrint(object):
    def setupUi(self, ImagePrint):
        if not ImagePrint.objectName():
            ImagePrint.setObjectName(u"ImagePrint")
        ImagePrint.resize(734, 542)
        icon = QIcon()
        icon.addFile(u"dpu414.ico", QSize(), QIcon.Normal, QIcon.Off)
        ImagePrint.setWindowIcon(icon)
        self.gridLayout = QGridLayout(ImagePrint)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineImagePath = QLineEdit(ImagePrint)
        self.lineImagePath.setObjectName(u"lineImagePath")

        self.gridLayout.addWidget(self.lineImagePath, 0, 0, 1, 1)

        self.btnBrowse = QPushButton(ImagePrint)
        self.btnBrowse.setObjectName(u"btnBrowse")

        self.gridLayout.addWidget(self.btnBrowse, 0, 1, 1, 1)

        self.labelPreview = QLabel(ImagePrint)
        self.labelPreview.setObjectName(u"labelPreview")
        self.labelPreview.setScaledContents(False)

        self.gridLayout.addWidget(self.labelPreview, 1, 0, 1, 2)

        self.btnPrintImage = QPushButton(ImagePrint)
        self.btnPrintImage.setObjectName(u"btnPrintImage")

        self.gridLayout.addWidget(self.btnPrintImage, 2, 1, 1, 1)


        self.retranslateUi(ImagePrint)

        QMetaObject.connectSlotsByName(ImagePrint)
    # setupUi

    def retranslateUi(self, ImagePrint):
        ImagePrint.setWindowTitle(QCoreApplication.translate("ImagePrint", u"Image print", None))
#if QT_CONFIG(tooltip)
        self.lineImagePath.setToolTip(QCoreApplication.translate("ImagePrint", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineImagePath.setWhatsThis(QCoreApplication.translate("ImagePrint", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineImagePath.setText("")
        self.btnBrowse.setText(QCoreApplication.translate("ImagePrint", u"Browse", None))
        self.labelPreview.setText("")
        self.btnPrintImage.setText(QCoreApplication.translate("ImagePrint", u"Send to printer", None))
    # retranslateUi


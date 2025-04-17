# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_print.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_TextPrint(object):
    def setupUi(self, TextPrint):
        if not TextPrint.objectName():
            TextPrint.setObjectName(u"TextPrint")
        TextPrint.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"dpu414.ico", QSize(), QIcon.Normal, QIcon.Off)
        TextPrint.setWindowIcon(icon)
        self.gridLayout = QGridLayout(TextPrint)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnPrintText = QPushButton(TextPrint)
        self.btnPrintText.setObjectName(u"btnPrintText")

        self.gridLayout.addWidget(self.btnPrintText, 1, 1, 1, 1)

        self.textEdit = QTextEdit(TextPrint)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 2)


        self.retranslateUi(TextPrint)

        QMetaObject.connectSlotsByName(TextPrint)
    # setupUi

    def retranslateUi(self, TextPrint):
        TextPrint.setWindowTitle(QCoreApplication.translate("TextPrint", u"Print text", None))
        self.btnPrintText.setText(QCoreApplication.translate("TextPrint", u"Send to printer", None))
#if QT_CONFIG(whatsthis)
        self.textEdit.setWhatsThis(QCoreApplication.translate("TextPrint", u"<html><head/><body><p align=\"center\"><br/><br/></p><p align=\"center\"><span style=\" font-weight:700;\">Write the text you want to print in here</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi


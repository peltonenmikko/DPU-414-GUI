# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(241, 94)
        icon = QIcon()
        icon.addFile(u"dpu414.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboComPort = QComboBox(Form)
        self.comboComPort.setObjectName(u"comboComPort")

        self.gridLayout.addWidget(self.comboComPort, 3, 0, 1, 1)

        self.btnPrintImage = QPushButton(Form)
        self.btnPrintImage.setObjectName(u"btnPrintImage")

        self.gridLayout.addWidget(self.btnPrintImage, 4, 1, 1, 1)

        self.btnPrintText = QPushButton(Form)
        self.btnPrintText.setObjectName(u"btnPrintText")

        self.gridLayout.addWidget(self.btnPrintText, 4, 0, 1, 1)

        self.comboBaudRate = QComboBox(Form)
        self.comboBaudRate.setObjectName(u"comboBaudRate")

        self.gridLayout.addWidget(self.comboBaudRate, 3, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DPU-414 GUI", None))
#if QT_CONFIG(whatsthis)
        self.comboComPort.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btnPrintImage.setText(QCoreApplication.translate("Form", u"Print image", None))
        self.btnPrintText.setText(QCoreApplication.translate("Form", u"Print text", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">COM Port</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Baud Rate</p></body></html>", None))
    # retranslateUi


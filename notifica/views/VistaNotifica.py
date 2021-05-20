from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VistaNotifica(object):
    def setupUi(self, VistaNotifica):
        VistaNotifica.setObjectName("VistaNotifica")
        VistaNotifica.resize(304, 453)

        self.verticalLayout = QtWidgets.QVBoxLayout(VistaNotifica)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_imbarcazione = QtWidgets.QLabel(VistaNotifica)
        self.label_imbarcazione.setObjectName("label_imbarcazione")
        self.horizontalLayout.addWidget(self.label_imbarcazione)

        self.label_sacchi = QtWidgets.QLabel(VistaNotifica)
        self.label_sacchi.setObjectName("label_sacchi")
        self.horizontalLayout.addWidget(self.label_sacchi)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.columnView = QtWidgets.QColumnView(VistaNotifica)
        self.columnView.setObjectName("columnView")
        self.verticalLayout.addWidget(self.columnView)

        self.button_invia = QtWidgets.QPushButton(VistaNotifica)
        self.button_invia.setObjectName("button_invia")
        self.verticalLayout.addWidget(self.button_invia)

        self.retranslateUi(VistaNotifica)
        QtCore.QMetaObject.connectSlotsByName(VistaNotifica)

    def retranslateUi(self, VistaNotifica):
        _translate = QtCore.QCoreApplication.translate
        VistaNotifica.setWindowTitle(_translate("VistaNotifica", "VistaNotifica"))
        self.label_imbarcazione.setText(_translate("VistaNotifica",
                                                   "<html><head/><body><p><span style=\" font-size:11pt;\">Imbarcazione</span></p></body></html>"))
        self.label_sacchi.setText(_translate("VistaNotifica",
                                             "<html><head/><body><p><span style=\" font-size:11pt;\">Sacchi</span></p></body></html>"))
        self.button_invia.setText(_translate("VistaNotifica", "Invia"))
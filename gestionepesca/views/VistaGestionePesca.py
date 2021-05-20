from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VistaGestionePesca(object):
    def setupUi(self, VistaGestionePesca):
        VistaGestionePesca.setObjectName("VistaGestionePesca")
        VistaGestionePesca.resize(453, 398)
        VistaGestionePesca.setAutoFillBackground(False)

        self.verticalLayout = QtWidgets.QVBoxLayout(VistaGestionePesca)

        self.gridLayout = QtWidgets.QGridLayout()

        self.label_inserisci_quota = QtWidgets.QLabel(VistaGestionePesca)
        self.label_inserisci_quota.setObjectName("label_inserisci_quota")
        self.gridLayout.addWidget(self.label_inserisci_quota, 0, 0, 1, 1)

        self.lineEdit_quota = QtWidgets.QLineEdit(VistaGestionePesca)
        self.lineEdit_quota.setObjectName("lineEdit_quota")
        self.gridLayout.addWidget(self.lineEdit_quota, 1, 0, 1, 1)

        self.button_conferma = QtWidgets.QPushButton(VistaGestionePesca)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_conferma.setFont(font)
        self.button_conferma.setObjectName("button_conferma")
        self.gridLayout.addWidget(self.button_conferma, 2, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)

        self.button_notifica = QtWidgets.QPushButton(VistaGestionePesca)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_notifica.setFont(font)
        self.button_notifica.setObjectName("button_notifica")
        self.gridLayout_2.addWidget(self.button_notifica, 1, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(VistaGestionePesca)
        QtCore.QMetaObject.connectSlotsByName(VistaGestionePesca)

        def show_notifica():
            vista_notifica = QtWidgets.QWidget()
            ui = Ui_VistaNotifica
            ui.setupUi(vista_notifica)
            vista_notifica.show()

    def retranslateUi(self, VistaGestionePesca):
        _translate = QtCore.QCoreApplication.translate
        VistaGestionePesca.setWindowTitle(_translate("VistaGestionePesca", "Gestione Pesca"))
        self.label_inserisci_quota.setText(_translate("VistaGestionePesca",
                                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Inserisci Quota Totale:</span></p></body></html>"))
        self.button_conferma.setText(_translate("VistaGestionePesca", "Conferma"))
        self.button_notifica.setText(_translate("VistaGestionePesca", "Notifica"))

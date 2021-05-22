from PyQt5 import QtWidgets

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle("Co.Vo.Pi Software")
        self.resize(300, 100)
        self.textName = QtWidgets.QLineEdit(self) #spazio di riempimento per username
        self.textPass = QtWidgets.QLineEdit(self) #spazio di riempimento per password
        self.label_user = QtWidgets.QLabel ('Inserisci il nome utente:',self)
        self.label_password = QtWidgets.QLabel('Inserisci la password: ', self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.GestioneLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label_user)
        layout.addWidget(self.textName)
        layout.addWidget(self.label_password)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def GestioneLogin(self):
        if (self.textName.text() == 'admin' and #USERNAME
                self.textPass.text() == 'password'): #PASSWORD
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Errore', 'Nome utente o password errata')

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.setWindowTitle("Co.Vo.Pi Software")
        window.resize(300, 100)
        window.show()
        sys.exit(app.exec_())

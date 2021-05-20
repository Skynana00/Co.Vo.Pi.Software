from PyQt5 import QtWidgets
import sys



from gestionepesca.views.VistaGestionePesca import Ui_VistaGestionePesca

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    vista_gestione_pesca = QtWidgets.QWidget()
    ui = Ui_VistaGestionePesca()
    ui.setupUi(vista_gestione_pesca)
    vista_gestione_pesca.show()
    sys.exit(app.exec_())
from PyQt5 import QtWidgets

from src.ui.view import Ui_MainWindow

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    janelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.configurarInterface(janelaPrincipal)
    janelaPrincipal.show()
    sys.exit(app.exec_())
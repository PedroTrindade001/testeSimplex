# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

from src.algorithms.simplex import Simplex, expression_util
from src.ui.alert import Ui_Dialog

class Ui_MainWindow(object):
    def configurarInterface(self, janelaPrincipal):

        #Criação da tela da interface
        janelaPrincipal.setObjectName("JanelaPrincipal")
        janelaPrincipal.resize(363, 500)
        janelaPrincipal.setMinimumSize(QtCore.QSize(363, 500))
        janelaPrincipal.setMaximumSize(QtCore.QSize(363, 500))

        #Criação de um Widget
        self.centralwidget = QtWidgets.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")

        #Criação Label 1 (Texto)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 17))
        self.label.setObjectName("label")

        #Criação Label 2 (Texto)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 67, 17))
        self.label_2.setObjectName("label_2")

        # Criação Label 3 (Texto)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 141, 17))
        self.label_3.setObjectName("label_3")

        # Criação Label 4 (Texto)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 20, 91, 17))
        self.label_4.setObjectName("label_4")

        #Criação Combo Box (Menu de escolhas)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 50, 91, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        #Criação de botão
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 191, 25))
        self.pushButton.setObjectName("pushButton")

        #Criação do painel resultado, onde é mostrada a solução
        self.resultPanel = QtWidgets.QTextEdit(self.centralwidget)
        self.resultPanel.setGeometry(QtCore.QRect(20, 330, 321, 131))
        self.resultPanel.setReadOnly(True)
        self.resultPanel.setObjectName("resultPanel")

        # Criação de um Widget (editar texto)
        self.saBlock = QtWidgets.QTextEdit(self.centralwidget)
        self.saBlock.setGeometry(QtCore.QRect(20, 110, 311, 131))
        self.saBlock.setObjectName("saBlock")

        # Criação de um Widget (inserir/editar texto em uma linha)
        self.campoFO = QtWidgets.QLineEdit(self.centralwidget)
        self.campoFO.setGeometry(QtCore.QRect(20, 50, 201, 25))
        self.campoFO.setObjectName("campoFO")

        janelaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(janelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        janelaPrincipal.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.executarSimplex)

        self.traduzirInterface(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)

    #Método Responsável por nomear os "atributos" da interface
    def traduzirInterface(self, janelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "Algoritmo Simplex"))
        self.label.setText(_translate("JanelaPrincipal", "Função Objetivo:"))
        self.label_2.setText(_translate("JanelaPrincipal", "Restrições:"))
        self.label_3.setText(_translate("JanelaPrincipal", "Resultado:"))
        self.label_4.setText(_translate("JanelaPrincipal", "Objetivo:"))
        self.comboBox.setItemText(0, _translate("JanelaPrincipal", "MAX"))
        self.pushButton.setText(_translate("JanelaPrincipal", "Solução"))
        self.saBlock.setToolTip(
            _translate(
                "JanelaPrincipal",
                "Utilize incógnitas diferentes para cada termo de uma restrição",  # noqa: E501
            )
        )
        self.campoFO.setToolTip(
            _translate(
                "JanelaPrincipal",
                "Utilize incógnitas diferentes para cada termo. ex: 3x + 3y ao invés de 3x1 + 3x2",  # noqa: E501
            )
        )

    def executarSimplex(self):
        try:
            objective_function = self.campoFO.text()
            obj = self.comboBox.currentIndex()
            simplex = Simplex(objective_function, obj)
            constraint_block = self.saBlock.toPlainText()
            constraints = constraint_block.split("\n")
            if constraints:
                for constraint in constraints:
                    simplex.adicionarRestricoes(constraint)

                meta = simplex.solve()
                variables = ""
                for incognita in expression_util.get_incognitas(objective_function):
                    variables += f"<br/>Valor de {incognita}: {meta[incognita]}"

                self.resultPanel.setText(
                    f"<b>Solução Ótima: <span style='color:green;'>{meta['solution']}</span></b>{variables}"  # noqa: E501
                )

        except Exception as e:
            self.printException(str(e))

    def printException(self, e: str):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, e)
        Dialog.exec()

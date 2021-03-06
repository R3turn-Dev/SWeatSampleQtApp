# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\foo_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from UIs.help_program_info import Ui_HelpProgramInfo


class Ui_FooApplication(object):
    def setupUi(self, FooApplication):
        FooApplication.setObjectName("FooApplication")
        FooApplication.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FooApplication)
        self.centralwidget.setObjectName("centralwidget")
        FooApplication.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FooApplication)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        FooApplication.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FooApplication)
        self.statusbar.setObjectName("statusbar")
        FooApplication.setStatusBar(self.statusbar)
        self.actionNew_Project = QtWidgets.QAction(FooApplication)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionOpen_Project = QtWidgets.QAction(FooApplication)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.action_2 = QtWidgets.QAction(FooApplication)
        self.action_2.setObjectName("action_2")
        self.actionProgram_Info = QtWidgets.QAction(FooApplication)
        self.actionProgram_Info.setObjectName("actionProgram_Info")
        self.menuFiles.addAction(self.actionNew_Project)
        self.menuFiles.addAction(self.actionOpen_Project)
        self.menuFiles.addSeparator()
        self.menu.addAction(self.actionProgram_Info)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(FooApplication)
        QtCore.QMetaObject.connectSlotsByName(FooApplication)

        # ->> Handling with custom handlers
        self.actionProgram_Info.triggered.connect(self.open_program_info)

    def open_program_info(self):
        self.window = QtWidgets.QMainWindow()
        self.new_ui = Ui_HelpProgramInfo()
        self.new_ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, FooApplication):
        _translate = QtCore.QCoreApplication.translate
        FooApplication.setWindowTitle(_translate("FooApplication", "MainWindow"))
        self.menuFiles.setTitle(_translate("FooApplication", "파일"))
        self.menu.setTitle(_translate("FooApplication", "도움말"))
        self.actionNew_Project.setText(_translate("FooApplication", "새 프로젝트"))
        self.actionOpen_Project.setText(_translate("FooApplication", "프로젝트 열기"))
        self.action_2.setText(_translate("FooApplication", "program info"))
        self.actionProgram_Info.setText(_translate("FooApplication", "프로그램 정보"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FooApplication = QtWidgets.QMainWindow()
    ui = Ui_FooApplication()
    ui.setupUi(FooApplication)
    FooApplication.show()
    sys.exit(app.exec_())

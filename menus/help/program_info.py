import typing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLayout


class UIProgramInfo(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Help_ProgramInfo")
        self.setWindowTitle("프로그램 정보")
        self.resize(400, 313)

        label_logo = QLabel()
        label_logo.setPixmap(QPixmap("resources/enak.jpg"))
        label_logo.setScaledContents(False)
        label_logo.setAlignment(QtCore.Qt.AlignCenter)

        label_creator = QLabel("제작자: 이은학")
        label_creator.setAlignment(QtCore.Qt.AlignCenter)

        label_program_name = QLabel("파일 관리자 데모")
        label_program_name.setAlignment(QtCore.Qt.AlignCenter)
        font = label_program_name.font()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        label_program_name.setFont(font)

        # ->> Layout
        layout = QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        layout.addWidget(label_logo)
        layout.addWidget(label_creator)
        layout.addWidget(label_program_name)

        self.setLayout(layout)

    def showModal(self):
        return super().exec_()

import functools
import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtCore import QRect, QSize, QPoint, QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp, \
    QVBoxLayout, QScrollArea, QLabel, QGridLayout, QHBoxLayout

from menus import help
from utils.sorter import sort_by


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # ->> Tooltip preferences
        QToolTip.setFont(QFont("SansSerif", 10))

        # ->> Centering
        monitor_resolution = QDesktopWidget().screenGeometry()
        widget_size = QSize(1280, 720)
        padding_point = QPoint(
            monitor_resolution.center().x() - widget_size.width() / 2,
            monitor_resolution.center().y() - widget_size.height() / 2)
        self.setGeometry(QRect(padding_point, widget_size))

        # ->> Windows meta
        self.setWindowTitle("Foo Application")
        self.setWindowIcon(QIcon(r"resources/enak.jpg"))

        # ->> Buttons
        # btn = QPushButton(QIcon(r"C:\Users\\Pictures\x-png-15.png"), "Quit", self)
        # btn.setToolTip("button tooltip")
        # btn.move(widget_size.width() - 100, 30)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(self.teardown)

        # ->> Status Bar
        self.statusBar().showMessage("hey Ron")

        # ->> Menu Bar
        bar = self.menuBar()
        bar.setNativeMenuBar(False)

        menu_file = bar.addMenu("&파일")
        menu_help = bar.addMenu("&도움말")

        # # ->> Actions: File
        action_new_project = QAction("프로젝트 생성", self)
        action_new_project.setShortcut("CTRL+SHIFT+N")
        action_new_project.setStatusTip("Create new project")
        menu_file.addAction(action_new_project)

        action_open_project = QAction("프로젝트 열기", self)
        action_open_project.setShortcut("CTRL+SHIFT+O")
        action_open_project.setStatusTip("Open project")
        menu_file.addAction(action_open_project)

        menu_file.addSeparator()

        action_exit = QAction("Exit", self)
        action_exit.setShortcut("CTRL+Q")
        action_exit.setStatusTip("Exit application")
        action_exit.triggered.connect(self.teardown)
        menu_file.addAction(action_exit)

        # # ->> Actions: Help
        action_help_program_info = QAction("프로그램 정보", self)
        action_help_program_info.setStatusTip("프로그램의 정보를 확인합니다.")
        action_help_program_info.triggered.connect(lambda: help.UIProgramInfo().showModal())
        menu_help.addAction(action_help_program_info)

        # ->> Layouts
        # # ->> Left menu
        # # # ->> Project info
        label_project_indi = QLabel("현재 프로젝트")
        label_project_name = QLabel("> Foo project.sweatproject")

        left_project_info = QVBoxLayout()
        left_project_info.addWidget(label_project_indi)
        left_project_info.addWidget(label_project_name)

        # # # ->> Scroll
        label_scroll_desc = QLabel("등록된 감시 폴더 경로")
        left_scroll = QScrollArea()
        scroll_widget = QWidget()
        scroll_grid = QVBoxLayout(scroll_widget)

        left_scroll.setMaximumWidth(230)
        scroll_grid.setAlignment(QtCore.Qt.AlignTop)
        left_scroll.setWidgetResizable(True)

        for n in range(40):
            content = QLabel("Content {}".format(n + 1))
            content.mousePressEvent = functools.partial(self.file_path_label_clicked, content)
            scroll_grid.addWidget(content)

        left_scroll.setWidget(scroll_widget)

        left_bottom = QVBoxLayout()
        left_bottom.addWidget(label_scroll_desc)
        left_bottom.addWidget(left_scroll)

        left_menu_layout = QVBoxLayout()
        left_menu_layout.addLayout(left_project_info)
        left_menu_layout.addWidget(QLabel(""))  # Spacer
        left_menu_layout.addLayout(left_bottom)

        left_menu = QWidget()
        left_menu.setLayout(left_menu_layout)
        left_menu.setMaximumWidth(230)

        # # -> Right menu
        # # # ->> Directory info
        self.label_directory_name = QLabel()
        font = self.label_directory_name.font()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_directory_name.setFont(font)
        self.label_directory_name.setText("Directory name here")

        right_menu_layout = QVBoxLayout()
        right_menu_layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        right_menu_layout.addWidget(self.label_directory_name)

        right_menu = QWidget()
        right_menu.setLayout(right_menu_layout)

        layout = QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        layout.addWidget(left_menu)
        layout.addWidget(right_menu)

        central = QWidget(self)
        central.setLayout(layout)
        self.setCentralWidget(central)

    @staticmethod
    def teardown(*args, **kwargs):
        print("Exiting with", args, kwargs)
        return QCoreApplication.instance().quit()

    def file_path_label_clicked(self, label: QLabel = None, event=None):
        print(label, event)
        self.label_directory_name.setText(label.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

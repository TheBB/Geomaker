import functools
from os.path import dirname, realpath, join
import sys

from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtWebChannel


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.create_ui()

    def create_ui(self):
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)

        view = QtWebEngineWidgets.QWebEngineView()

        self.channel = QtWebChannel.QWebChannel()
        self.channel.registerObject("Main", self)
        view.page().setWebChannel(self.channel)

        html = join(dirname(realpath(__file__)), "assets/map.html")
        view.setUrl(QtCore.QUrl.fromLocalFile(html))
        vbox.addWidget(view)

    @QtCore.pyqtSlot(str)
    def update_objects(self, contents):
        print(contents)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('GeoMaker')
        self.setCentralWidget(MainWidget())


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())

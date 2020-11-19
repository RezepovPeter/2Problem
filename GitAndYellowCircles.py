import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt, QPoint
from random import randint, randrange
from PyQt5 import uic


class SupreMatizm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.qp = QPainter()
        self.DrawButton.clicked.connect(self.ButtonPushed)
        self.flag = False

    def initUI(self):
        self.setWindowTitle('GAYC')
        self.setGeometry(300, 300, 800, 600)

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawcircle()
            self.qp.end()

    def drawcircle(self):
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(self.coords[0] - self.size / 2,
                            self.coords[1] - self.size / 2, self.size, self.size)

    def ButtonPushed(self, event):
        self.size = randint(1, 200)
        self.coords = (randint(0, 800 - self.size), randint(0, 600 - self.size))
        self.drawk()

    def drawk(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SupreMatizm()
    ex.show()
    sys.exit(app.exec())
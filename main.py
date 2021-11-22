import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.generateButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        diameter = randint(5, 175)
        qp.drawEllipse(30, 70, diameter, diameter)
        qp.setBrush(QColor(255, 255, 0))
        diameter = randint(5, 175)
        qp.drawEllipse(205, 70, diameter, diameter)
        qp.setBrush(QColor(255, 255, 0))
        diameter = randint(5, 175)
        qp.drawEllipse(380, 70, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())
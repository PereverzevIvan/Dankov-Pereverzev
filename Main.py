import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from random import randint


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.w = self.width()
        self.h = self.height()
        self.do_paint = False
        self.btn_draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        x, y = randint(50, self.w - 50), randint(50, self.h - 50)
        radius = randint(15, 100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, radius, radius)

    def paint(self):
        self.do_paint = True
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Form()
    wnd.show()
    sys.exit(app.exec())

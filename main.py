import io
import random
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from main_des import MainDesign


class MyWidget(QMainWindow, MainDesign):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.size = self.size()
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(random.randint(1, 256), random.randint(1, 256), random.randint(1, 256)))

            s = random.randint(10, 100)
            max_x = self.size.width() - s
            max_y = self.size.height() - s

            if max_x > 0 and max_y > 0:
                x = random.randint(0, max_x)
                y = random.randint(0, max_y)
                qp.drawEllipse(x, y, s, s)

            qp.end()
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
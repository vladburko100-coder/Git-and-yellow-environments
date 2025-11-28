import io
import random
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>170</y>
      <width>321</width>
      <height>131</height>
     </rect>
    </property>
    <property name="text">
     <string>кнопка</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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
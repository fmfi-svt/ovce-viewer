#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QTimer


class Ovcovac(QMainWindow):
    def __init__(self, app=None):
        super().__init__()

        self.app = app
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.WindowStaysOnTopHint |
                            Qt.FramelessWindowHint |
                            Qt.X11BypassWindowManagerHint)
        self.initUI()

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.setInterval(1000)
        timer.start()

    def initUI(self):
        self.showMaximized()
        self.showFullScreen()
        self.setWindowTitle('Ovce')

        geometry = app.desktop().availableGeometry()
        geometry.setHeight(geometry.height())

        self.setGeometry(geometry)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):

        x = random.randint(0, 200)

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10+x, 15+x, 90, 60)

        qp.setBrush(QColor(255, 80, 0, 160))
        qp.drawRect(130+x, 15+x, 90, 60)

        qp.setBrush(QColor(25, 0, 90, 200))
        qp.drawRect(250+x, 15+x, 90, 60)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ovcovac()
    sys.exit(app.exec_())

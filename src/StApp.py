#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from StTetris import StTetris
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = StTetris()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

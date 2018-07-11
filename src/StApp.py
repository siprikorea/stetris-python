import sys
from StTetris import StTetris
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    stetris = StTetris()
    stetris.start()
    sys.exit(app.exec_())

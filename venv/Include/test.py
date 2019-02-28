import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    w.setWindowTitle("Hello PyQt5")
    sys.exit(app.exec_())




# from PyQt5 import QtWidgets,QtCore
#
# app = QtWidgets.QApplication(sys.argv)
# wigget = QtWidgets.QWidget()
# wigget.resize(360,360)
# wigget.setWindowTitle("hello,pyqt5")
# wigget.show()
#
# sys.exit(app.exec())


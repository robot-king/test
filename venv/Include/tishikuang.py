import  sys

from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("this is a <b>Qwidget</b> window")

        btn = QPushButton("button",self)
        self.setToolTip("this is a <b>Qpushbutton</b> window")
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("tooltip")
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    cla = Example()

    sys.exit(app.exec_())




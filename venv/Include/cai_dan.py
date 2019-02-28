import  sys

from PyQt5.QtWidgets import QMainWindow,qApp,QAction,QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon("exit.png"),"&Exit",self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("exit application")
        exitAct.triggered.connect(qApp.quit)

        self.menuBar()

        menuBar  = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,250,200)
        self.setWindowTitle("menu")
        self.show()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
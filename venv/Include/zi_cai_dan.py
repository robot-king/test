import sys

from PyQt5.QtWidgets import QMainWindow,QAction,QMenu,QApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("file")

        impMenu = QMenu("import",self)
        impAct = QAction("import mail",self)
        impMenu.addAction(impAct)

        newAct = QAction("new",self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300,300,200,200)
        self.setWindowTitle("zi_cai_dan")
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
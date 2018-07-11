import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QLineEdit


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox'
        self.left = 600
        self.top = 400
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # create ico
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('..\luoyc\Demo\Rochan.png'))

        # create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('确定', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, "Message", 'You typed:' + textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        # """打印完毕之后清空文本框"""
        self.textbox.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exit(app.exec_())

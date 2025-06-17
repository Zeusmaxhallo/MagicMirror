from PyQt5.QtWidgets import QWidget


import sys
from PyQt5.QtWidgets import QComboBox, QFormLayout, QLabel, QLineEdit, QApplication, QWidget, QScrollArea
from pure_spotify import PureSpotify
from date_time import DateTime


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):
        ps = PureSpotify()
        ps.setupUi(self)
        #datetime = DateTime()
        #datetime.setupUi(self)
        self.setWindowTitle('DateTime Test')


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.showFullScreen()
    app.exec_()


if __name__ == '__main__':
    main()

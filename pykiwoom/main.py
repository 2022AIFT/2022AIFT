import sys
from PyQt5.QtWidgets import *
from pykiwoom import *
from pykiwoom.kiwoom import Kiwoom


# login
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)

        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect(self.callback_login)

    def callback_login(self, *args, **kwargs):
        if kwargs['err_code'] == 0:
            self.statusBar().showMessage("로그인 완료")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
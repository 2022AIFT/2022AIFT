#  주기저으로 어떤 작업이 수행

import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timer_slot)

    def timer_slot(self):
			#  타이머가 작동될 때 실행되는 코드
        name = threading.currentThread().getName()
        print(f"timer slot is called by {name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
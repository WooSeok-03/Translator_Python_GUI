import sys
from googletrans import Translator
from PyQt5.QtWidgets import *
from PyQt5 import uic

translator = Translator()

#UI파일 연결(ui파일이 python 코드 파일과 같은 디렉토리에 있어야함.)
form_class = uic.loadUiType("Trans_GUI.ui")[0]

#화면 띄우는데 사용되는 Class
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_Window = MyWindow()
    my_Window.show()
    app.exec_()
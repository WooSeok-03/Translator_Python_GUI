import sys
from googletrans import Translator
from PyQt5.QtWidgets import *
from PyQt5 import uic

#번역을 위한 객체 생성
translator = Translator()

#UI파일 연결(ui파일이 python 코드 파일과 같은 디렉토리에 있어야함.)
form_class = uic.loadUiType("Trans_GUI.ui")[0]

#화면 띄우는데 사용되는 Class
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_Translation.clicked.connect(self.Trans_)

    def Trans_(self):

        #comboBox 선택
        if self.Original_language.currentIndex() == 0:
            lang_src = 'en'
        elif self.Original_language.currentIndex() == 1:
            lang_src = 'ja'
        elif self.Original_language.currentIndex() == 2:
            lang_src = 'ko'

        if self.Trans_language.currentIndex() == 0:
            lang_dest = 'ko'
        elif self.Trans_language.currentIndex() == 1:
            lang_dest = 'en'
        elif self.Trans_language.currentIndex() == 2:
            lang_dest = 'ja'

        #번역기능
        original = self.Original_Box.toPlainText()
        trans_show = translator.translate(original, src=lang_src, dest=lang_dest).text

        self.Trans_Box.setText(trans_show)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_Window = MyWindow()
    my_Window.show()
    app.exec_()
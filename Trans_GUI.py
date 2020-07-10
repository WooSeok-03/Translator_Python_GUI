import sys
from googletrans import Translator
from LANGUAGE import LANG
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

        for key in sorted(LANG.keys()):
            self.Original_language.addItem(key)
            self.Trans_language.addItem(key)


        self.btn_Translation.clicked.connect(self.Trans_Buttom)


    def Trans_Buttom(self):

        #comboBox 선택
        for i in sorted(LANG.keys()):
            if self.Original_language.currentText() == i:
                lang_src = LANG[i]
                break

        for i in sorted(LANG.keys()):
            if self.Trans_language.currentText() == i:
                lang_dest = LANG[i]
                break

        #번역기능
        original = self.Original_Box.toPlainText()
        trans_show = translator.translate(original, src=lang_src, dest=lang_dest).text

        self.Trans_Box.setText(trans_show)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    my_Window = MyWindow()
    my_Window.show()
    app.exec_()
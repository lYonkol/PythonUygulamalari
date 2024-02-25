import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout,QTextEdit,QFileDialog,QHBoxLayout
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        
    def init_ui(self):
        self.yazi_alanı =QTextEdit()
        self.temizle = QPushButton("  Temizle  ")
        self.ac =QPushButton("  Aç  ")
        self.kaydet =QPushButton(" Kaydet ")

        h_box =QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box =QVBoxLayout()
        v_box.addWidget(self.yazi_alanı)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.temizle.clicked.connect(self.clear)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.save)
        self.setWindowTitle("NotePad")

        

    def clear(self):
        self.yazi_alanı.clear()

    def dosya_ac(self):
        dosya_ismi =QFileDialog.getOpenFileName(self,"Dosya aç",os.getenv("DESKTOP"))
        with open(dosya_ismi[0],"r",encoding="utf-8")as file:
            self.yazi_alanı.setText(file.read())

        




    def save(self):
        dosya_ismi =QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya_ismi[0],"w",encoding="utf-8")as file:
            file.write(self.yazi_alanı.toPlainText())


class Menu(QMainWindow):
    def __init__(self):
            super().__init__()
            self.pencere = Pencere()
            self.setCentralWidget(self.pencere)
            self.setWindowTitle("Metin Editörü")
            self.menuleri_oluştur()
            self.show()
    def menuleri_oluştur(self):
        menubar =self.menuBar()
        dosya = menubar.addMenu("Dosya")

        dosya_ac =QAction("Dosya Ac",self)
        dosya_ac.setShortcut("CTRL+O")

        dosya_kaydet =QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("CTRL+S")

        temizle =QAction("Dosyayı Temizle",self)
        temizle.setShortcut("CTRL+D")

        cikis =QAction("Çıkış",self)
        cikis.setShortcut("CTRL+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("Metin editoru")
        self.show()
    def response(self,action):
        if action.text() == "Dosya Ac":
            self.pencere.dosya_ac()
        elif action.text() =="Dosya Kaydet":
            self.pencere.save()
        elif action.text() == "Dosya Temizle":
            self.pencere.clear()
        elif action.text() == "Çıkış":
            qApp.quit()

app =QApplication(sys.argv)
main_menu = Menu()
sys.exit(app.exec_())
from PyQt5 import QtWidgets
import sys
import sqlite3
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()
    
    def init_ui(self):
        
        self.kullanıcı_Adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kayıt =QtWidgets.QPushButton("Kayıt ol")
        self.giris = QtWidgets.QPushButton("Giriş yap")
        self.yazialanı = QtWidgets.QLabel("")

        v_box =QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanıcı_Adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazialanı)
        v_box.addStretch()
        v_box.addWidget(self.kayıt)
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.kayıt.clicked.connect(self.register)
        self.show()

    def baglanti_olustur(self):

        baglanti =sqlite3.connect("database.db")

        self.cursor = baglanti.cursor()

        self.cursor.execute("Create Table If Not exists üyeler ( kullanıcı_adı TEXT, parola TEXT)")

        baglanti.commit()
    def login(self):
        adi = self.kullanıcı_Adi.text()
        par =self.parola.text()

        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ? and parola = ?",(adi,par))
        data = self.cursor.fetchall()
        if len(data)==0:
            self.yazialanı.setText("Böyle bir kullanıcı adı yok\n lütfen tekrar deneyin")
        else:
            self.yazialanı.setText("Hoşgeldiniz"+" "+adi)

    def register(self):
        username = self.kullanıcı_Adi.text()
        par = self.parola.text()
        
        self.cursor.execute("Select * From üyeler where kullanıcı_adı = ?",(username,))
        data = self.cursor.fetchall()
        kontrol = True
        for i in data:
            if i in data:
                kontrol = False
        if kontrol == True:
            self.cursor.execute("INSERT INTO üyeler (kullanıcı_adı, parola) VALUES (?, ?)",(username,par))
            self.yazialanı.setText("Başarıyla kayıt oldunuz")
        else:
            self.yazialanı.setText("Bu kullanıcı zaten kayıtlı")


app =QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
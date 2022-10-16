import sys
import os
from PyQt5 import QtWidgets
class Notepad(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Notepad")
        self.byömer = QtWidgets.QLabel("Ömer Aykılıç Tarafından Yapılmıştır")
        self.yazıalanı = QtWidgets.QTextEdit()
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        self.temizle =QtWidgets.QPushButton("Temizle")
        self.dosyaac = QtWidgets.QPushButton("Dosya Aç")
        h = QtWidgets.QHBoxLayout()
        h.addStretch()
        h.addWidget(self.temizle)
        h.addWidget(self.kaydet)
        h.addWidget(self.dosyaac)
        h.addStretch()
        v = QtWidgets.QVBoxLayout()
        v.addWidget(self.yazıalanı)
        v.addLayout(h)
        v.addWidget(self.byömer)
        self.setLayout(v)
        self.temizle.clicked.connect(self.temizlefonk)
        self.kaydet.clicked.connect(self.kaydetfonk)
        self.dosyaac.clicked.connect(self.acfonk)
    def temizlefonk(self):
        self.yazıalanı.clear()
    def acfonk(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        with open(dosya[0],"r") as file:
            self.yazıalanı.setText(file.read())
    def kaydetfonk(self):
        dosya = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya[0],"w") as file:
            file.write(self.yazıalanı.toPlainText())
class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pencere = Notepad()
        self.setCentralWidget(self.pencere)
        self.setWindowTitle("Metin Editörü")
        self.setGeometry(700, 300, 500, 500)
        self.menuleri_olustur()
        self.show()
    def menuleri_olustur(self):
        menu = self.menuBar()
        dosya =menu.addMenu("Dosya")
        dosya_ac = QtWidgets.QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+D")
        dosya_kaydet = QtWidgets.QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")
        temizle = QtWidgets.QAction("Temizle",self)
        cikis =QtWidgets.QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        dosya.triggered.connect(self.response)
    def response(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.acfonk()
        elif action.text() == "Dosya Kaydet":
            self.pencere.kaydetfonk()
        elif action.text() == "Temizle":
            self.pencere.temizlefonk()
        elif action.text() == "Çıkış":
            QtWidgets.qApp.quit()
        

app = QtWidgets.QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())

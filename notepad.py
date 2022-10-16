import sys
import os
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(800,300,400,400)
        self.yazi_alani = QtWidgets.QTextEdit()
        self.ac = QtWidgets.QPushButton("Aç")
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        self.temizle = QtWidgets.QPushButton("Temizle")
        h = QtWidgets.QHBoxLayout()
        h.addWidget(self.temizle)
        h.addWidget(self.ac)
        h.addWidget(self.kaydet)
        v = QtWidgets.QVBoxLayout()
        v.addWidget(self.yazi_alani)
        v.addLayout(h)
        self.setLayout(v)
        self.temizle.clicked.connect(self.click)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        self.show()
    def click(self):
        self.yazi_alani.clear()
    def dosya_ac(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        with open(dosya[0],"r") as file:
            self.yazi_alani.setText(file.read())
    def dosya_kaydet(self):
        dosya = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(dosya[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())

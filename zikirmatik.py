import sys
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Zikirmatik")
        self.setGeometry(800,450,400,200)
        self.sayaç = 0
        self.yazı = QtWidgets.QLabel("{} Zikir Çekildi.".format(self.sayaç))
        self.buton = QtWidgets.QPushButton("Zikir Çek")
        self.byömer = QtWidgets.QLabel("Ömer Aykılıç Tarafından Yapılmıştır.")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı)
        v_box.addWidget(self.buton)
        v_box.addStretch()
        v_box.addWidget(self.byömer)
        self.setLayout(v_box)
        self.buton.clicked.connect(self.click)
        self.show()
    def click(self):
        self.sayaç +=1
        self.yazı.setText("{} Defa Zikredildi.".format(self.sayaç))
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())


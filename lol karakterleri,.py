import time
import random

class karakter():
    def __init__(self ,karakter_ismi = "bilgi yok",saldırı_gücü = "bilgi yok",can = "bilgi yok"):
        self.karakter_ismi = karakter_ismi
        self.saldırı_gücü = saldırı_gücü
        self.can = can

zed = karakter("Zed",80,500)

yasuo = karakter("Yasuo",75,600)

yone = karakter("Yone",85,400)

veigar = karakter("Veigar",can = 500)








print("*************************\nLoL Karakter seçme oyununa hoşgeldiniz...\nSeçtiğiniz karakterlerin özellikleri gözükecektir.\nÇıkmak için 'Çıkış' yazınız.\nSeçilebilir karakterler :\nZed     Yasuo   Yone   Veigar\n*************************")
while True:
    k_isim = input("Lütfen seçmek istediğiniz karakteri yazınız:")

    if k_isim == ("Zed" or "zed"):
        print("Karakterin ismi:")
        time.sleep(1)
        print("**********",zed.karakter_ismi,"**********")
        time.sleep(1)
        print("Karakterin Saldırı Gücü:")
        time.sleep(1)
        print("**********",zed.saldırı_gücü,"**********")
        time.sleep(1)
        print("Karakterin Can Değeri")
        time.sleep(1)
        print("**********",zed.can,"**********")
    elif k_isim == ("Yasuo" or "yasuo"):
        print("Karakterin ismi:")
        time.sleep(1)
        print("**********",yasuo.karakter_ismi,"**********")
        time.sleep(1)
        print("Karakterin Saldırı Gücü:")
        time.sleep(1)
        print("**********",yasuo.saldırı_gücü,"**********")
        time.sleep(1)
        print("Karakterin Can Değeri:")
        time.sleep(1)
        print("**********",yasuo.can,"**********")
    elif k_isim == ("Yone" or "yone"):
        print("Karakterin ismi:")
        time.sleep(1)
        print("**********",yone.karakter_ismi,"**********")
        time.sleep(1)
        print("Karakterin Saldırı Gücü:")
        time.sleep(1)
        print("**********",yone.saldırı_gücü,"**********")
        time.sleep(1)
        print("Karakterin Can Değeri")
        time.sleep(1)
        print("**********",yone.can,"**********")
    elif k_isim == ("Veigar" or "veigar"):
        print("Karakterin ismi:")
        time.sleep(1)
        print("**********",veigar.karakter_ismi,"**********")
        time.sleep(1)
        print("Karakterin Saldırı Gücü:")
        time.sleep(1)
        print("**********",veigar.saldırı_gücü,"**********")
        time.sleep(1)
        print("Karakterin Can Değeri")
        time.sleep(1)
        print("**********",veigar.can,"**********")
    elif k_isim == "Çıkış":
        print("Program sonlandırılıyor...%",random.randint(1,50))
        time.sleep(1)
        print("Program sonlandırılıyor...%",random.randint(50,99))
        time.sleep(1)
        print("Program sonlandırılıyor...%100")
        time.sleep(0.5)
        print("Program sonlandırıldı.")
        break
    







    

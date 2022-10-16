import math
import time
import random
class hesap_makinesi():
    def __init__(self):
        print("Hesap Makinesi Açılıyor...")
        time.sleep(1)
        print("Hesap makinesi Açılıyor %",random.randint(0,100))
        time.sleep(1)
        print("Hesap makinesi açıldı...")

    def topla(self):
        try:
            toplam1 = int(input("Sayı1"))
            toplam2 = int(input("Sayı2"))
            print("Sonuç:",toplam1 + toplam2)
        except ValueError:
            print("Lütfen bir SAYI giriniz...")
    def böl(self):
        try:
            böl1 = int(input("sayı1:"))
            böl2 = int(input("sayı2:"))
            print(böl1 / böl2)
        except ValueError:
            print("Lütfen bir sayı giriniz!")
        except ZeroDivisionError:
            print("Bir sayı 0' a bölünemez!")
    def çarp(self):
        try:
            çarp1=int(input("Sayı1:"))
            çarp2=int(input("Sayı2:"))
            print("Sonuç:",çarp1 * çarp2)
        except ValueError:
            print("Lütfen bir sayı giriniz!")
    def çıkar(self):
        try:
            çıkar1 = int(input("Sayı1:"))
            çıkar2 = int(input("sayı2"))
            çıkarma = çıkar1 - çıkar2
            print("Sonuç:{}".format(çıkarma))
        except ValueError:
            print("Lütfen bir sayı giriniz!")
    
    def sin(self):
        try:
            a = int(input("Sayı:"))
            print(math.sin(a))
        except ValueError:
            print("Lütfen bir Sayı giriniz!")
    def cos(self):
        try:
            b = int(input("Sayı:"))
            print(math.cos(b))
        except ValueError:
            print("Lütfen bir sayı giriniz!")
    def tan(self):
        try:
            c = int(input("Sayı:"))
            print(math.tan(c))
        except ValueError:
            print("Lütfen bir sayı giriniz!")
    def cot(self):
        try:
            d = int(input("Sayı:"))
            print(1/(math.tan(d)))
        except:
            print("Lütfen bir sayı giriniz!")

    def karesi(self):
        try:
            karesi = int(input("Sayı"))
            print(karesi ** 2)
        except:
            print("Lütfen bir sayı giriniz!")
    def üssü(self):
        try:
            üssü1 = int(input("Sayı1:"))
            üssü2 = int(input("Sayı2:"))
            print(pow(üssü1,üssü2))
        except:
            print("Lütfen bir sayı giriniz!")
    def log(sefl):
        try:
            logaritma = int(input("Sayı:"))
            print(math.log10(logaritma))
        except:
            print("Hata!!!")
    def ac(self):
        while True:
            işlem = input("Lütfen Yapmak İstediğiniz İşlemi Giriniz:")
            if işlem == "1":
                hesap_makinesi.topla()
            elif işlem == "2":
                hesap_makinesi.çarp()
            elif işlem == "3":
                hesap_makinesi.çıkar()
            elif işlem == "4":
                hesap_makinesi.böl()
            elif işlem == "5":
                hesap_makinesi.sin()
            elif işlem == "6":
                hesap_makinesi.cos()
            elif işlem == "7":
                hesap_makinesi.tan()
            elif işlem == "8":
                hesap_makinesi.cot()
            elif işlem == "9":
                hesap_makinesi.karesi()
            elif işlem == "10":
                hesap_makinesi.üssü()
            elif işlem == "11":
                hesap_makinesi.log()
            elif işlem == "q":
                print("çıkış yapılıyor...")
                time.sleep(1)
                print("çıkış yapıldı...")
                break
            else:
                print("Geçersiz işlem...")




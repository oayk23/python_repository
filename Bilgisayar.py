import time
import random
import msvcrt
class Bilgisayar():
    def __init__(self,kullanıcı = "Default",bilgisayarın_durumu = "kapalı",ses_düzeyi = 0,uygulama_listesi = ["Hesap Makinesi","İnternet Tarayıcı"],açık_uygulama = "yok",wifi = "Kapalı",işletim_sistemi = "Windows",internet_geçmişi = []):
        self.ses_düzeyi = ses_düzeyi
        self.bilgisayarın_durumu = bilgisayarın_durumu
        self.uygulama_listesi = uygulama_listesi
        self.açık_uygulama = açık_uygulama
        self.wifi = wifi
        self.işletim_sistemi = işletim_sistemi
        self.internet_geçmişi = internet_geçmişi
        self.kullanıcı = kullanıcı
    def bilgisayar_aç(self):
        print("Bilgisayar Açılıyor...%",random.randint(0,50))
        time.sleep(1)
        print("Bilgisayar Açılıyor...%",random.randint(50,99))
        time.sleep(1)
        print("Bilgisayar Açılıyor...%100")
        print("Bilgisayar Açıldı")
        self.bilgisayarın_durumu = "Açık"
    def bilgisayar_kapat(self):
        print("Bilgisayar Kapatılıyor...%",random.randint(0,50))
        time.sleep(1)
        print("Bilgisayar Kapatılıyor...%", random.randint(50,99))
        time.sleep(1)
        print("Bilgisayar Kapatılıyor...%100")
        print("Bilgisayar Kapatıldı")
        self.bilgisayarın_durumu = "Kapalı"
    def ses_düzenleme(self):
        while True:
            print("Sesi Arttırmak İçin 'arttır'\nSesi Azaltmak İçin'azalt'\nÇıkış Yapmak İçin 'çıkış' yazınız.")
            a = input("Seçiminizi Yapınız.")
            if a == "çıkış":
                print("Geri Dönülüyor...")
                break
            elif a == "arttır":
                try:
                    b = int(input("Arttırmak istediğiniz miktarı giriniz(0 ile 100 arasında):"))
                    if (b < 0 and b > 100):
                        print("Bu miktarı giremezsiniz")
                    else:
                        if ((self.ses_düzeyi + b) > 100):
                            print("Girdiğiniz değer maksimum değeri aşmaktadır.\nŞuan ki değer {}".format(
                                self.ses_düzeyi))
                        else:
                            print("Ses düzeyi arttırıldı...")
                            self.ses_düzeyi += b
                            print("Mevcut ses düzeyi : {}".format(self.ses_düzeyi))
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz")
            elif (a == "azalt"):
                try:
                    c = int(input("Azaltmak istediğiniz değeri giriniz(0 ile 100 arasında):"))
                    if (c < 0 and c > 100):
                        print("Böyle bir değer giremezsiniz...")
                    else:
                        if ((self.ses_düzeyi - c) < 0):
                            print("Girdiğiniz değer minimum değerin altına düşürmektedir.\nMevcut Değer: {}".format(
                                self.ses_düzeyi))
                        else:
                            print("Ses düzeyi azaltıldı...")
                            self.ses_düzeyi -= c
                            print("Mevcut ses düzeyi: {}".format(self.ses_düzeyi))
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz.")
    def uygulama_indir(self,uygulama):
        print("Uygulama indirildi :",uygulama)
        self.uygulama_listesi.append(uygulama)
    def hesap_makinesi(self):
        print("""
        ********************
        Hesap makinesine hoşgeldiniz...
        Yapmak istediğiniz işlemi seçiniz:
        1.Toplama
        2.Çıkarma
        3.Çarpma
        4.Bölme
        5.Karesini Alma
        6.Karekökünü Alma
        Çıkış Yapmak için 'q' ya basınız.
        ********************
        """)
        while True:
            hesap_makinesi_girişi = input("İşlemi Seçiniz:")
            if (hesap_makinesi_girişi == "q"):
                print("Çıkış yapılıyor")
                break
            elif (hesap_makinesi_girişi == "1"):
                try:
                    hesap_makinesi_toplama_1 = int(input("Birinci Sayıyı Giriniz :"))
                    hesap_makinesi_toplama_2 = int(input("İkinci Sayıyı Giriniz:"))
                    print("İşlem yapılıyor...")
                    time.sleep(1)
                    print("Sonuç :",hesap_makinesi_toplama_2 + hesap_makinesi_toplama_1)
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz.")
            elif (hesap_makinesi_girişi == "2"):
                try:
                    hesap_makinesi_çıkarma_1 = int(input("Birinci Sayıyı Giriniz:"))
                    hesap_makinesi_çıkarma_2 = int(input("İkinci Sayıyı Giriniz"))
                    print("İşlem yapılıyor...")
                    time.sleep(1)
                    print("Sonuç:",hesap_makinesi_çıkarma_1 - hesap_makinesi_çıkarma_2)
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz.")
            elif (hesap_makinesi_girişi == "3"):
                try:
                    hesap_makinesi_çarpma_1 = int(input("Birinci Sayıyı Giriniz:"))
                    hesap_makinesi_çarpma_2 = int(input("İkinci Sayıyı Giriniz:"))
                    print("İşlem yapılıyor...")
                    time.sleep(1)
                    print("Sonuç:",hesap_makinesi_çarpma_1 * hesap_makinesi_çarpma_2)
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz.")
            elif (hesap_makinesi_girişi == "4"):
                try:
                    hesap_makinesi_bölme_1 = int(input("Birinci Sayıyı Giriniz:"))
                    hesap_makinesi_bölme_2 = int(input("İkinci Sayıyı Giriniz:"))
                    print("İşlem yapılıyor...")
                    time.sleep(1)
                    print("Sonuç",hesap_makinesi_bölme_1 / hesap_makinesi_bölme_2)
                except ZeroDivisionError:
                    print("Bir Sayı 0'a bölünemez.")
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz")
            elif  (hesap_makinesi_girişi == "5"):
                try:
                    hesap_makinesi_karesi = int(input("Sayıyı Giriniz:"))
                    print("İşlem yapılıyor...")
                    time.sleep(1)
                    print("Sonuç:",hesap_makinesi_karesi ** 2)
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz.")
            elif (hesap_makinesi_girişi == "6"):
                try:
                    hesap_makinesi_karekök = int(input("Sayıyı Giriniz:"))
                    print("İşlem yapılıyor...")
                    time.sleep(1)
                    print("Sonuç",hesap_makinesi_karekök ** 0.5 )
                except ValueError:
                    print("Lütfen Bir Sayı Giriniz.")
            else:
                print("Geçersiz İşlem...")
    def internet_tarayıcı(self):
        print("""
        *****************
        İnternet Tarayıcısına Hoşgeldiniz....
        Yapabileceğiniz İşlemler:
        1. Webde Gezin
        2.İnternet Geçmişime Bak
        'q' = çıkış
        ***************** 
           """)
        while True:
            browser = input("Seçim:")
            if (browser == "1"):
                browser_1 = input("Aramak İstediğinizi Yazınız")
                print("Arama Sonuçları:")
                print("Hiçbir Sonuç Bulunamadı")
                self.internet_geçmişi.append(browser_1)
            elif (browser == "2"):
                for i in self.internet_geçmişi:
                    print(i)
            elif (browser == "q"):
                print("Çıkış Yapılıyor...")
                time.sleep(1)
                print("Çıkış Yapıldı.")
                break
            else:
                print("Lütfen Geçerli Bir İşlem Giriniz...")
    def kullanıcı_değiştir_(self):
        kullanıcı_değiştirme = input("Kullanıcı İsmini Giriniz:")
        self.kullanıcı = kullanıcı_değiştirme
    def __str__(self):
        return "Kullanıcı {}\nİşletim Sistemi {}\nUygulamalar {}\nWi-Fi Durumu {}".format(self.kullanıcı,self.işletim_sistemi,self.uygulama_listesi,self.wifi)
    def wifi_aç(self):
        print("Wi-Fi Açıldı...")
        self.wifi = "Açık"
    def wifi_kapat(self):
        print("Wi-Fi Kapandı...")
        self.wifi = "Kapalı"
bilgisayar = Bilgisayar()
print("""
Bilgisayara Hoş Geldiniz {}
İşlemler:
1.Bilgisayarı Aç
2.Bilgisayarı Kapat
3.Bilgisayarın Sesini Düzenle
4.Uygulama İndir
5.Hesap Makinesini Aç
6.İnternet Tarayıcısını Aç
7.Kullanıcı Değiştir
8.Wi-Fi Aç
9.Wi-Fi Kapat
10.Bilgisayarın Özellikleri
Çıkmak için 'çıkış' Yazınız...

""".format(bilgisayar.kullanıcı))
while True:
    giriş = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:")
    if (giriş == "1"):
        if (bilgisayar.bilgisayarın_durumu == "Açık"):
            print("Bilgisayar zaten açık")
        else:
            bilgisayar.bilgisayar_aç()
    elif (giriş == "2"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bilgisayar zaten kapalı")
        else:
            bilgisayar.bilgisayar_kapat()
    elif (giriş == "3"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            bilgisayar.ses_düzenleme()
    elif (giriş == "4"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            uygulamalar = input("İndirmek İstediğiniz Uygulamaları ',' Kullanarak Yazınız:")
            eklenecekler = uygulamalar.split(",")
            for i in eklenecekler:
                bilgisayar.uygulama_indir(i)
            print("Uygulamalar İndirildi...")
    elif (giriş == "5"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            print("Hesap Makinesi Açılıyor...%",random.randint(0,50))
            time.sleep(1)
            print("Hesap Makinesi Açılıyor...%",random.randint(50,99))
            time.sleep(1)
            print("Hesap Makinesi Açılıyor...%100")
            bilgisayar.hesap_makinesi()
    elif (giriş == "6"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            if bilgisayar.wifi == "Kapalı":
                print("Tarayıcıya Bağlanmak İçin Wi-Fi Açınız...")
            else:
                print("Tarayıcı Açılıyor...%",random.randint(0,50))
                time.sleep(1)
                print("Tarayıcı Açılıyor...%",random.randint(50,99))
                time.sleep(1)
                print("Tarayıcı Açılıyor...%100")
                bilgisayar.internet_tarayıcı()
    elif (giriş == "7"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            print("Kullanıcı Ayarları Değiştiriliyor...")
            bilgisayar.kullanıcı_değiştir_()
            time.sleep(1)
            print("Kullanıcı Değiştirildi...")
    elif (giriş == "8"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            if (bilgisayar.wifi == "Açık"):
                print("Wi-Fi Zaten Açık")
            else:
                bilgisayar.wifi_aç()
    elif (giriş =="9"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            if (bilgisayar.wifi == "Kapalı"):
                print("Wi-Fi Zaten Kapalı")
            else:
                bilgisayar.wifi_kapat()
    elif (giriş == "10"):
        if (bilgisayar.bilgisayarın_durumu == "Kapalı"):
            print("Bu İşlemi Yapabilmek İçin Öncelikle Bilgisayarı Açmalısınız")
        else:
            print(bilgisayar)
    elif (giriş == "çıkış"):
        print("Çıkış yapılıyor...%",random.randint(0,50))
        time.sleep(1)
        print("Çıkış yapılıyor...%",random.randint(50,99))
        time.sleep(1)
        print("Çıkış Yapılıyor...%100")
        print("Çıkış Yapıldı...")
        break
    else:
        print("Lütfen Geçerli İşlem Giriniz...")












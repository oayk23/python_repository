import time
import random
import msvcrt

class Kumanda():
    def __init__(self,televizyon_durumu = "Kapalı",ses_düzeyi = 0,kanal_listesi = ["TRT"],açık_kanal = "TRT"):
        print("Televizyon oluşturuluyor...")
        self.televizyon_durumu = televizyon_durumu
        self.ses_düzeyi = ses_düzeyi
        self.kanal_listesi = kanal_listesi
        self.açık_kanal = açık_kanal
    def sesi_düzenle(self):
        while True:
            karakter = input("Sesi artırmak için'Arttır'\nSesi azaltmak için'Azalt'\nÇıkmak için 'çıkış' yazınız.\nSeçim:")
            if (karakter == "Arttır"):
               while True:
                   x = int(input("Arttırmak istediğiniz miktarı giriniz:\n"))
                   if (x < 0):
                       print("Böyle bir sayı arttıramazsınız...")
                   elif(x > 0):
                       self.ses_düzeyi += x
                       break
                   else:
                       print("Ses düzeyi sabit kaldı...")
                       break
            elif (karakter == "Azalt"):
                while True:
                    y = int(input("Azaltmak istediğiniz miktarı giriniz:\n"))
                    if (y < 0):
                        print("Böyle bir sayı kadar azaltamazsınız...")
                    elif (y > 0):
                        self.ses_düzeyi -= y
                        break
                    else:
                        print("Ses düzeyi sabit kaldı...")
                        break
            elif (karakter == "çıkış"):
                print("Komut alındı")
                time.sleep(0.5)
                print("Çıkış yapılıyor")
                break
            else:
                print("Geçersiz işlem")
    def tv_kapat(self):
        if (self.televizyon_durumu == "Kapalı"):
            print("Televizyon zaten kapalı....")
        else:
            print("Tv Kapatılıyor...")
            time.sleep(0.5)
            print("Tv kapatıldı...")
            self.televizyon_durumu = "Kapalı"
    def tv_aç(self):
        if (self.televizyon_durumu == "Açık"):
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            time.sleep(0.5)
            print("Televizyon açıldı....")
            self.televizyon_durumu = "Açık"
    def __str__(self):
        return "TV durumu:{}\nSes düzeyi:{}\nKanal Listesi:{}\nAçık kanal:{}".format(self.televizyon_durumu,self.ses_düzeyi,self.kanal_listesi,self.açık_kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.açık_kanal = self.kanal_listesi[rastgele]
        print("Şuan açık kanal:",self.açık_kanal)
    def kanal_ekle(self,kanal):
        print("Kanal eklendi:",kanal)
        self.kanal_listesi.append(kanal)
kumanda = Kumanda()
print("""*******************

Televizyon Uygulaması

İşlemler ;

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Düzenle

Çıkmak için 'Çıkış' yazın.
*******************""")
while True:
    işlem = input("Lütfen gireceğiniz işlemi seçiniz:")
    if (işlem == "1"):
        kumanda.tv_aç()
    elif(işlem == "2"):
        kumanda.tv_kapat()
    elif(işlem == "3"):
        print(kumanda)
    elif(işlem == "4"):
        if (kumanda.televizyon_durumu == "Kapalı"):
            print("Televizyon Kapalı Olduğu İçin Bu İşlemi Yapamazsınız...")
        else:
            print("Kanal sayısı :", len(kumanda))
    elif(işlem == "5"):
        if (kumanda.televizyon_durumu == "Kapalı"):
            print("Televizyon Kapalı Olduğu İçin Bu İşlemi Yapamazsınız...")
        else:
            kanallar = input("Eklemek İstediğiniz Kanalları ',' ile ayırarak girin:")
            eklenecekler = kanallar.split(",")
            for i in eklenecekler:
                kumanda.kanal_ekle(i)
            print("Kanal Listesi başarıyla güncellendi...")
    elif (işlem == "6"):
        if (kumanda.televizyon_durumu == "Kapalı"):
            print("Televizyon Kapalı Olduğu İçin Bu İşlemi Yapamazsınız...")
        else:
            kumanda.rastgele_kanal()
    elif(işlem == "7"):
        if (kumanda.televizyon_durumu == "Kapalı"):
            print("Televizyon Kapalı Olduğu İçin Bu İşlemi Yapamazsınız...")
        else:
            kumanda.sesi_düzenle()
    elif(işlem == "Çıkış"):
        print("Çıkış yapılıyor...%",random.randint(0,50))
        time.sleep(1)
        print("Çıkış yapılıyor...%", random.randint(50,99))
        time.sleep(1)
        print("Çıkış yapılıyor...½100")
        time.sleep(1)
        print("Çıkış yapıldı...")
        break
    else:
        print("Böyle bir işlem yapamazsınız!")
























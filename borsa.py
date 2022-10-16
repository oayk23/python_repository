x = int(input("kac dolarınız var."))
k = 0
z = 0

while True:
    a = input("pozisyon")
    if (a == "k"):
        b = int(input("kar"))
        x = x*((100+b)/100)
        print(x)
        k +=1
    elif (a == "z"):
        c = int(input("zarar"))
        x = x*((100-c)/100)
        print(x)
        z +=1
    elif (a =="q"):
        print(x)
        ort_bas = (k/(k+z))*100
        print("Toplam Başarı oranı:%{}\nToplam Kar Pozisyonları: {}\nToplam Zarar Posizyonu:{}".format(ort_bas,k,z))
        break
    else:
        print("düzgün gir")

liste = dict()

for i in range(int(input("Kaç ayın değerlerini girmek istersiniz? "))):
    top_gider = 0
    print(50 * "*")
    ay = input("Hangi ayın değerlerini girmek istiyorsunuz? ")
    gelir = int(input(f"{ay} ayı gelirinizi giriniz: "))
    liste[f"{ay} ayının geliri"] = gelir
    for i in range(int(input("Kaç gider değeri girmek istersiniz? "))):
        gider = input("Ne gideri olduğunu giriniz: ")
        gider = gider.upper()
        ay = ay.upper()
        miktar = int(input(f"{ay} Ayının {gider} Giderini Giriniz: "))
        liste[f"{ay} AYININ {gider} GIDERI"] = miktar
        top_gider += miktar
    kalan_para = gelir - top_gider
    print(f"{ay} ayı Geliriniz : {gelir}")
    print(f"{ay} ayı Giderleriniz : {liste}")
    print(f"{ay} ayı Kalan paranız {kalan_para} ")

print(liste)

print(50*"*")
print(f"Hangi ayı görüntülemek istersiniz?")
ayın = input("Görüntülemek istediğiniz ay ve ne gideri olduğunu giriniz(Ör Ocak Ayının Mutfak Gideri): ")
ayın = ayın.upper()
print(f"{ayın}: {liste[ayın]} TL")


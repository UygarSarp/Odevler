import random as r
sayac = 0
deneme_sayisi = 1
sayi = r.randint(0,20)
print("Bilgisayar tarafından 0 ile 20 arasında oluşturulan sayıyı girdiğiniz üç sayının toplamı olarak tahmin etmeye çalışınız ")
while sayac < 1:
    a = int(input("İlk sayıyı giriniz: "))
    b = int(input("İkinci sayıyı giriniz: "))
    c = int(input("Üçüncü sayıyı giriniz: "))
    if a+b+c == sayi:
        sayac +=1
    else:
        print("Bir daha deneyin")
        deneme_sayisi += 1
print("Tebrikler sayıyı buldunuz")
print(f"Sayı : {sayi},Deneme sayınız : {deneme_sayisi}")
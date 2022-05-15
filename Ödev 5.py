print("Sadece 12 Soru ile Hangi Mesleğe Daha Yatkın Olduğunu Öğren!!!")
sorular=["Cinsiyetini öğrenebilir miyiz?  \nA) Erkek B) Kız","Peki yaş aralığın?  \nA) 0-10 B) 10-15 C) 15-20","Boş zamanlarında ne yapmayı seversin  \nA) Kitap okumak,Müzik dinlemek B) Oyun oynamak,Film izlemek C) Spor yapmak,Arkadaşlarla gezmek","Nasıl bir ortamda çalışmak sana göre?  \nA) Doğrudan işin yapıldığı faaliyet ortamında B) Home Office C) Küçük bir ofis","Ekip çalışması yapmayı sever misin?  \nA) Evet, ekip çalışması benim işim B) Hayır, azıcık aşım belasız başım C) İş olsun yeter ki bana fark etmez","Peki, ekip çalışmasında senin için hangisi söylenebilir?  \nA) İş bitiren B) Görev adamı C) Takımı yöneten","Kariyer senin için ne ifade ediyor?  \nA) Daha çok para B) Daha fazla güç C) Yerim belli olsun yeter","İşe nasıl kıyafetlerle gitmek istersin?  \nA) Bir kot, bir tshirt B) Mümkünse pijamayla C) Karizmayı tavan yaptıran üniformamla","Bildiğin bir şeyi başka birisine öğretme konusunda nasılsındır?  \nA) Herkesin aklı kendine, öğrensin işte B) Öğretmek benim işim C) Hiç beceremem, benlik değil","Şimdi kendine bir çalışma arkadaşı seçmeni istiyoruz:  \nA) Mark Zuckerberg B) Salvador Dali C) Donald Trump","Sizi uzun süre görmeyenlerden hangi sözleri işitirsiniz?  \nA) Seni çok arıyoruz B) Hiç değişmemişsin C) Yine acayip formdasın!","Son olarak çalıştığın ortamın olmazsa olmazı…  \nA) Kahve – çay makinesi B) Eğlenceli iş arkadaşları C) Ciddiyet!"]
puan = 0
for i in range(12):
    print(sorular[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevap == "A" or "a":
        puan += 10
    elif cevap == "B" or "b":
        puan += 5
    elif cevap == "C" or "c":
        puan -= 5

if puan >= 100:
    print("Yatkın olduğunuz meslek DOKTORLUK, MÜHENDİSLİK")
elif puan >= 80:
    print("Yatkın olduğunuz meslek ECZACILIK")
elif puan >= 60:
    print("Yatkın olduğunuz meslek PİLOTLUK")
elif puan >= 40:
    print("Yatkın olduğunuz meslek ÖĞRETMENLİK")
elif puan >= 20:
    print("Yatkın olduğunuz meslek AVUKATLIK,HAKİMLİK")
else:
    print("Yatkın olduğunuz meslek İŞ ADAMI ya da SERBEST MESLEK :)")
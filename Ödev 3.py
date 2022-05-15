import random as r
import time



sorular = ["Suyun kaynama derecesi kaçtır? \nA) 78 B) 100 C) 90 D) 80","Sinekli Bakkal Romanının Yazarı Aşağıdakilerden Hangisidir? \nA) Reşat Nuri Güntekin B) Halide Edip Adıvar C) Ziya Gökalp D) Ömer Seyfettin","Şimdiye kadar kurulmuş en büyük imparatorluk hangisidir? \nA) Moğol İmparatorluğu B) Britanya İmparatorluğu C) Rus İmparatorluğu D) Makedonya Krallığı","Aşağıda Verilen İlk Çağ Uygarlıklarından Hangisi Yazıyı İcat Etmiştir? \nA) Hititler B) Sümerler C) Elamlar D) Urartular","2003 Yılında Euro Vizyon Şarkı Yarışmasında Ülkemizi Temsil Eden ve Yarışmada Birinci Gelen Sanatçımız Kimdir? \nA) Grup Athena B) Sertap Erener C) Şebnem Paker D) Ajda Pekkan","Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir? \nA) Ankara B) Gaziantep C) İstanbul D) Bursa","Üç Büyük Dince Kutsal Sayılan Şehir Hangisidir? \nA) Mekke B) Kudüs C) Roma D) İstanbul","Hangi İlimizde Demiryolu Yoktur? \nA) Batman B) Muğla C) Aydın D) Kütahya","Hangi Ülkenin İki Tane Başkenti Vardır? \nA) Senegeal B) Güney Afrika C) El Salvador D)Venezuela","Aşağıdakilerden Hangisi Dünya Sağlık Örgütünün Kısaltılmış İsmidir? \nA) Uhw B) Who C) Unicef D) Nato","Aspirinin Hammaddesi Nedir? \nA) Köknar B) Söğüt C) Kavak D) Meşe","Bir Sebepten Dolayı Tek Kulağına Küpe Takan Osmanlı Padişahı Kimdir? \nA) Kanuni Sultan Süleyman B) Yavuz Sultan Selim C) Orhan Bey D) Fatih Sultan Mehmet","Cevdet Bey ve Oğulları Eseri Kime Aittir? \nA) Yahya Kemal Bayatlı B) Orhan Pamuk C) Atilla İlhan D) Samipaşazade Sezai","Bir Gün Kaç Saniyedir? \nA) 86000 B) 86400 C) 88600 D) 84800","Tsunami Felaketinde En Fazla Zarar Gören Güney Asya Ülkesi Aşağıdakilerden Hangisidir? \nA) Japonya B) Endonezya C) Tayland D) Hindistan","Güneş Sisteminde kaç gezegen bulunmaktadır? \nA) 7 B) 8 C) 9 D) 10","1.Dünya Savaşı Hangi Yıl Başlamıştır? \nA) 1943 B) 1914 C) 1918 D) 1945","Wallis ve Furtuna Ülkesi Aşağıdaki Yıllarda Hangisinde Fransa'ya Bağlanmıştır? \nA) 1960 B) 1959 C) 1958 D) 1957 ","Fatih Sultan Mehmet’in babası kimdir? \nA) 1.Mehmet B) 2.Murat C) Yıldırım Beyazıd D) 1.Murat","Magna Carta hangi ülkenin kralıyla yapılmış bir sözleşmedir? \nA) Fransa B) Britanya C) İspanya D) Almanya"]
cevaplar = ["b","a","b","d","b","b","b","a","b","a","b","c","b","d","b","a","b","d","b","a","b","c","b","d","b","b","b","a","b","d","b","c","b","a","b","c","b","b","b","b"]
r.shuffle(sorular)


dogru = []
yanlis = []
dogru_zaman = []
basla = time.time()
puan = 0
ad = input("Adınızı Giriniz: ")
for i in range(1,11):
    print(f"{i}. Soru Geliyor {ad} Hazır Ol!")
    print(sorular[i])
    zaman = time.time()
    cevap = input(f"Cevabını girmek için 5 saniyen var, Cevabı vermen 5 saniyeden uzun sürerse puan kaybedeceksin {ad}!")
    zaman_b = time.time()
    if (zaman_b - zaman) >= 5:
        puan -= 10
        yanlis.append(sorular[i])
    elif cevap == cevaplar[i*2]:
        puan += 10
        dogru.append(sorular[i])
    else:
        yanlis.append(sorular[i])

simdi = time.time()
print(50*"*")
print(simdi-basla,f"{ad},Saniyede bitirdin!")
print(f"puanın: {puan}")
print("Doğru yaptığın sorular: ", dogru)
print("Yanlış yaptığın sorular: ", yanlis)








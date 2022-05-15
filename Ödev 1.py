import random as r


liste = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
sifreler = dict()
a = int(input("Kaç şifre oluşturmak istersiniz?"))
for i in range( 1,a+1):
    for s in range(16):
        b = r.randint(0, 62)
        sifrel = r.sample(liste,16)
        sifre = ""
        for c in sifrel:
            sifre = sifre+c
        sifreler[f'Sifre {i}'] = sifre
print(sifreler)


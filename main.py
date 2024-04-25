import random

secenekler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

tercih = int(input("kaç değerli bir parolanız olmasını istiyorsunuz? "))

parola = []

for i in range(tercih):
    sifre = random.choice(secenekler)
    parola.append(sifre)

print(parola)

'''
1-) Kullanıcıdan integer türünde bir değer isteyiniz. İstemiş olduğunuz bu değerin çarpım tablosu
değerlerini gösteren kodu for döngüsü ile gerçekleştiriniz (10p).
Örnek: Kullanıcı 5 değerini girerse, çıktı olarak 5 10 15 20 ... ... 50 (10’a kadar)
'''

deger = int(input("Bir sayı giriniz: "))


for i in range(1, 11):
    print(deger * i, end=" ")

print("\n--------------------------------------------\n")



'''
2-) Girilen bir sayının kaç basamaklı olduğunu belirleyen programı 
while döngüsü ile gerçekleştiriniz
'''

sayi = int(input("Bir sayı giriniz: "))

sayi = abs(sayi)

basamak_sayisi = 0

while sayi > 0:
    sayi = sayi // 10  # Sayıyı 10'a böl
    basamak_sayisi += 1  # Basamak sayısını bir artır

# Eğer sayı sıfır ise (yani kullanıcı 0 girmişse), basamak sayısı 1 olmalıdır
if basamak_sayisi == 0:
    basamak_sayisi = 1

print(f"Girilen sayı {basamak_sayisi} basamağa sahiptir.")

print("\n--------------------------------------------\n")



'''
3-) Aşağıda bir listeye ait sayısal değerler verilmiştir.
sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
Bu listedeki 5’e bölünen sayıları çıktı olarak veren programı hem for hem de while döngüsü ile
gerçekleştiriniz. 150’den büyük değerleri dikkate almayınız (20p).
Çıktı: 15, 55, 75, 150
'''

sayilar = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

print("For Döngüsü")
for sayı in sayilar:
    if sayı <= 150 and sayı % 5 == 0: 
        print(sayı, end=", ")


print("\nWhile Döngüsü")
i = 0
while i < len(sayilar):
    sayı = sayilar[i]
    if sayı <= 150 and sayı % 5 == 0:
        print(sayı, end=", ")
    i += 1

print("\n--------------------------------------------\n")

'''
4-) Kullanıcıdan 3 adet (a, b ve c) değer alınız. a (dahil) ve b (dahil) arasında kaç sayının c’ye
bölünebildiğini belirleyen programı yazınız (20p).
Örnek: a = 20, b = 40, c = 5 ise Çıktı: 5
'''

a = int(input("a değerini giriniz: "))
b = int(input("b değerini giriniz: "))
c = int(input("c değerini giriniz: "))

sayac = 0

for sayi in range(a, b + 1):
    if sayi % c == 0:  # Eğer sayı c'ye tam bölünüyorsa
        sayac += 1

# Sonucu yazdır
print(f"{a} ile {b} arasında, {c}'e tam bölünebilen {sayac} sayi var.")

print("\n--------------------------------------------\n")

'''
5-) Aşağıdaki çıktıyı veren programı yazınız (10p).
1 – 99
2 – 98
3 – 97
..
..
..
98 – 2
99 – 1
'''

for i in range(1, 100):
    print(f"{i} - {100 - i}")

print("\n--------------------------------------------\n")

'''
6-) Kullanıcıdan bir IP adresi isteyiniz. İstediğiniz bu IP adresinden sonraki 
5 değeri çıktı olarak veren programı yazınız (30p).
Örnek: 192 168 255 252
Çıktı: 192 168 255 253
192 168 255 254
192 168 255 255
192 169 0 0
192 169 0 1
'''

ip_adresi = input("IP adresini giriniz (örnek: 192.168.255.252): ")

ip_listesi = ip_adresi.split(".")

ip_listesi = [int(octet) for octet in ip_listesi]
for i in range(5):
    # Son okteti artır
    ip_listesi[3] += 1
    
    if ip_listesi[3] == 256:
        ip_listesi[3] = 0
        ip_listesi[2] += 1
        
        if ip_listesi[2] == 256:
            ip_listesi[2] = 0
            ip_listesi[1] += 1
            
            if ip_listesi[1] == 256:
                ip_listesi[1] = 0
                ip_listesi[0] += 1

    print(f"{ip_listesi[0]}.{ip_listesi[1]}.{ip_listesi[2]}.{ip_listesi[3]}")

''' 
1-) Kullanıcıdan 3 adet integer türünde değer alınız. Almış olduğunuz bu değerler bir üçgenin
açılarını ifade edecektir. Bu açı değerlerine göre bu üçgenin dik, geniş ya da dar üçgen olup
olmadığını belirleyen programı yazınız
'''
aci_1 = int(input("1. Açı: "))
aci_2 = int(input("2. Açı: "))
aci_3 = int(input("3. Açı: "))

if aci_1 + aci_2 + aci_3 == 180:
    if aci_1 == 90 or aci_2 == 90 or aci_2 == 90:
        print("Bu bir dik üçgendir.")
    elif aci_1 > 90 or aci_2 > 90 or aci_3 > 90:
        print("Bu bir geniş açılı üçgendir.")
    else:
        print("Bu bir dar açılı üçgendir.")
else:
    print("Bu açı değerleri geçersiz, çünkü üçgenin açıları toplamı 180 olmalıdır.")

print("\n--------------------------------------------\n")

''' 
2-) # İçinde uzaylı olan bir oyun geliştirdiğinizi düşünün. uzaylı_rengi isminde bir değişken oluşturun
ve bu değişken string türünde değerler alsın. Bu değişkene kırmızı, yeşil ya da sarı
değerlerinden birini klavyeden veriniz. Eğer uzaylının rengi yeşilse “Tebrikler, yeşil uzaylıya ateş
ettiğiniz için 5 puan kazandınız” şeklinde bir çıktı veriniz. Eğer rengi yeşil değilse "Tebrikler, yeşil
olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız" şeklinde çıktı veriniz. Senaryoya ait
programı yazınız 
'''

uzayli_rengi = input("Uzaylının rengini giriniz (kırmızı, yeşil, sarı): ").lower()

if uzayli_rengi == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız.")
else:
  print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız.")

print("\n--------------------------------------------\n")

'''
3-) Bir önceki sorudaki örneğe dayanarak if-elif-else yapılarını kullanarak aşağıdaki soruları
cevaplayınız (20p).
a) Eğer uzaylı rengi yeşil ise "Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız",
b) Eğer uzaylı rengi sarı ise "Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız",
c) Eğer uzaylı rengi kırmız ise "Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız"
şeklinde çıktı veren programı yazınız.
'''
# Kullanıcıdan uzaylı rengini al
uzayli_rengi = input("Uzaylının rengini giriniz (kırmızı, yeşil, sarı): ").lower()

# Koşullar
if uzayli_rengi == "yeşil":
    print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız.")
elif uzayli_rengi == "sarı":
    print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız.")
elif uzayli_rengi == "kırmızı":
    print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız.")
else:
    print("Geçersiz renk girdiniz!")

print("\n--------------------------------------------\n")

'''
4-) if-elif-else yapılarını kullanarak bir insanın yaşam evreleri ile ilgili programı oluşturunuz. int
türünde, yaş isminde bir değişken oluşturup, bu değişken için gerekli olan değeri kullanıcıdan
isteyiniz (20p).
a) Eğer bir insanın yaşı 2 yaşından küçük ise, "Bu kişi bebektir",
b) Eğer bir insanın yaşı 2 ile 4 arasındaysa (2 dâhil) "Bu kişi yeni yürümeye başlayan çocuktur",
c) Eğer bir insanın yaşı 4 ile 13 arasındaysa (4 dâhil) "Bu kişi çocuktur",
d) Eğer bir insanın yaşı 13 ile 20 arasındaysa (13 dâhil) "Bu kişi ergendir",
e) Eğer bir insanın yaşı 20 ile 65 arasındaysa (20 dâhil) "Bu kişi yetişkindir",
f) Eğer bir insanın yaşı 65 ve üstü ise (65 dâhil) "Bu kişi yaşlıdır" şeklinde çıktı veriniz.
'''

yas = int(input("Yaşınızı giriniz: "))

# Koşullar
if yas < 2:
    print("Bu kişi bebektir.")
elif 2 <= yas < 4:
    print("Bu kişi yeni yürümeye başlayan çocuktur.")
elif 4 <= yas < 13:
    print("Bu kişi çocuktur.")
elif 13 <= yas < 20:
    print("Bu kişi ergendir.")
elif 20 <= yas < 65:
    print("Bu kişi yetişkindir.")
else:
    print("Bu kişi yaşlıdır.")

print("\n--------------------------------------------\n")

'''
5-) Favori meyvelerinizin olduğu bir liste oluşturunuz ve bu listede 5 adet meyveniz bulunsun.
Listenin adı favori_meyveler şeklinde tanımlansın. if-else yapısını kullanarak örnekte verilen
meyvelerin favori listenizde olup olmadığını kontrol ediniz. Örnek meyveler; elma, armut,
karpuz, kavun, muz, portakal, çilek, vişne, kiraz ve mandalina
'''
favori_meyveler = ["elma", "muz", "portakal", "karpuz", "çilek"]

meyve = input("Lütfen bir meyve giriniz: ").lower()

if meyve in favori_meyveler:
    print(f"{meyve} favori meyvelerim arasında!")
else:
    print(f"{meyve} favori meyvelerim arasında değil.")
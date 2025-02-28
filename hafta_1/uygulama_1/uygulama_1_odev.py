import pandas as pd
import numpy as np

# a-) csv uzantılı dosyadan verileri okuma ve görüntüleme
df = pd.read_csv("data.csv")
print(df)
print("\n--------------------------------------------\n")

# b-) Sıcaklık ve Nem değerleri silindi
df = df.drop(["Sıcaklık","Nem"],axis=1)
print(df)
print("\n--------------------------------------------\n")

# c-) İstatisel bilgiler verildi
print(df.describe())
print("\n--------------------------------------------\n")


''' d-) (3,4) boyutunda bir dizi oluşturunuz. 
Oluşturduğunuz bu dizinin boyutunu (6,2) olacak şekilde değiştiriniz
dizi ellede oluşturabilirdim fakat hızlı olsun diye random sayılardan oluşturdum
''' 
arr = np.random.randint(1,10, size=(3,4))
print(arr)
print("\n--------------------------------------------\n")

# 6,2 olarak boyut değiştirildi
arr = arr.reshape(6,2)
print(arr)
print("--------------------------------------------\n")

# e-) İki tane (3,3) boyutunda rastgele sayılardan meydana bir dizi oluşturunuz. Oluşturulan bu diziyi
# hem yatay hem de dikey olacak şekilde istif (stack) ediniz

dizi1 = np.random.randint(1, 100, (3, 3))
dizi2 = np.random.randint(1, 100, (3, 3))

print("Dizi 1:\n", dizi1)
print("\nDizi 2:\n", dizi2)

# Yatay (horizontal) istifleme
yatay_istif = np.hstack((dizi1, dizi2))
print("\nYatay İstif:\n", yatay_istif)

# Dikey (vertical) istifleme
dikey_istif = np.vstack((dizi1, dizi2))
print("\nDikey İstif:\n", dikey_istif)
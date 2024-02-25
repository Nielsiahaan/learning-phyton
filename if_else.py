ketersediaan = "Daging ayam"
if ketersediaan == "Daging ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

# Combination if elif else and operator
nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

# ternary operator
lulus = True
print("selamat") if lulus else print("perbaiki")

# ternary tuples
kelulusan = ("Perbaiki, Anda belum lulus.", "Selamat, Anda lulus")[lulus]
print(kelulusan)
def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

# persegi_panjang_pertama = mencari_luas_persegi_panjang(5, 10)
# print(persegi_panjang_pertama)

second_rectangle = mencari_luas_persegi_panjang(4,15)
print(second_rectangle)

# Anonim function: Lambda
mencari_luas_persegi_panjang = lambda panjang, lebar: panjang * lebar
print(mencari_luas_persegi_panjang(4,9))
# List
contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
print(contoh_list)
# untuk menghitung panjang list
print(len(contoh_list))

# Set
contoh_set = {1, 3, 3, 5, 5, 5, 7, 7, 9}

print(contoh_set)
print(len(contoh_set))

# String
contoh_string = "Belajar Python"
print(contoh_string)
print(len(contoh_string))

# min and max
angka = [11, 2, 4, 1, 96, 8, 71, 38]
print(min(angka))
print(max(angka))

# count: untuk mengetahui berapa kali suatu object muncul dalam list
genap = [2, 4, 4, 6, 6, 8, 10, 10]
print(genap.count(6))

# menghitung banyak huruf a
string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))

# in and not in: untuk mengetahui nilai atau object that exist in list
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# set value into multiple variable
data = ['shirt', 'white', 'L']
appare1, color, size = data
print(data)
print(appare1)
print(color)
print(size)

# Sort: mengurutkan number or letter
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)

# membalikkan urutan
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort(reverse=True)
print(kendaraan)

# value nilai huruf kapital lebih diutamakan
kendaraan = ['motor', 'mobil', 'helikopter', 'Pesawat']
kendaraan.sort()

print(kendaraan)
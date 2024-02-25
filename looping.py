var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in var_list:
    print(i)
# loop with range
for i in range(10):
    print(i)
# print 1 - 10 with step 2
for i in range(1, 10, 2):
    print(i)

# while
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

# nested for
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

# looping control
# break
for i in range(2):  # perulangan tingkat pertama
    print("Perulangan luar: ", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan looping dalam jika j =1
# continue
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))

# else after for
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
        break
else:
    print("Angka tidak ditemukan.")

count = 0
while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

# pass: statement yang tidak ada tindakan jika kondisi terpenuhi
x = 10
if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")

# List Comprehension
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)

# more simple
pangkat = [n**2 for n in angka]
print(pangkat)


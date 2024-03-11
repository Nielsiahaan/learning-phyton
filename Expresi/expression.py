# Expression: kombinasi dari satu atau lebih variable, constanta, operator, dan fungsi
# untuk menghasikan suatu nilai dalam tipe tertentu

x = 10
y = 2
result = x - y
print(result)

# penggabungan list
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

# replikasi list
learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2

print(replikasi)

'''
Biner
(x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), (x % y), (x == y), (x != y).

Uner
(x += 1), (x-=1), (not x).
'''

a = True
a = not a
print(a)

b = 6
b -= 1
print(b)

c = 6
c += 1

'''
Ekspresi aritmetika: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan numerik.
Ekspresi relasional: jenis ekspresi yang memiliki operan bertipe numerik dan menghasilkan nilai boolean/logika.
Ekspresi logika: jenis ekspresi yang memiliki operan bertipe boolean/logika dan menghasilkan nilai boolean/logika.
'''
print(2 + 2)
print(3 < 10)
print(True or False)

# Jenis jenis operator

# Operator Aritmetika
x = 11
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

# Operator Relasional
x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Operator Logika
# And operator
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Or operator
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# NOT operator
print(not True)
print(not False)

# Operator Assignment
# +=
x = 11
x += 5
print(x)

# -=
x = 11
x -= 5
print(x)

# *=
x = 11
x *= 5
print(x)

# /=
x = 11
x /= 5
print(x)

# %=
x = 11
x %= 5
print(x)

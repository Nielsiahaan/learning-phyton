'''
slicing merujuk pada pengambilan data berdasarkan index dari rentang tertentu
'''

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

''' 
at the first syntax, i asked to fetch data from index 0 to index fourth with each element 2 dan kelipatannya will be passed.
the second one, it fetched the data from index 1 to last index
the third syntax fetched the data from index 0 until index 2
'''

"""
Tuple digunakan untuk data yang bersifat sekali deklarasi dan dapat dieksekusi lebih cepat
Tuple bersifat immutable
"""
x = (1, "Dicoding", 1 + 3j)
print(type(x))
print(x[1])
print(x[0:3])

'''
Set: kumpulan item bersifat unik, tanpa urutan
dapat diinisialisasikan dengan kurawal.
Set tidak memiliki indeks.
Set digunakan untuk menghilangkan duplikat pada suatu data
'''

x = {1, 2, 7, 2, 4, 12}
print(x[0])

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)



'''
List: jenis kumpulan data terurut. List Python tidak mengharuskan memiliki tipe data yang sama di dalamnya, but array
'''

x = [1, 2.2, 'Dicoding']
print(type(x))

x = [1, 'Dicoding', True,  1.0]
print(x[2])

'''
List python bersifat mutable : can be changed
'''
x[0] = 'Indonesia'
print(x)

'''
fetching data based on index
'''

x = ["laptop", "monitor", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])
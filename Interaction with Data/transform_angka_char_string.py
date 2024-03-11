'''
upper and lower func
'''

kata = 'dicoding'
kata = kata.upper()
print(kata)
kata = kata.lower()
print(kata)

'''
rstrip(): to delete whitespace at the right or the end of string
lstrip(): to delete whitespace at the left or the beginning of string
strip(): to delete whitespace pada bagian awal dan akhir
'''
print('dicoding    '.rstrip())
print('     dicoding'.lstrip())
print("         Dicoding          ".strip())

'''
if u wanna eliminate the character
'''
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

'''
Startswith(): to find out a word of string at the beginning
Metode endswith() bertujuan untuk menemukan suatu kata pada akhir string
'''

print('Dicoding Indonesia'.startswith('Dicoding'))
print('Dicoding Indonesia'.endswith('Dicoding'))

'''
Join: to combine the strings
split() bertujuan untuk memisahkan kata/substring berdasarkan delimiter.
'''
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('Dicoding Indonesia !'.split())
# Variable global
a = 10

def add(b):
    result = a + b
    return result

bilanganPertama = add(20)
print(bilanganPertama)


# Variable local
def add(a, b):
    lokal_var = 5
    result = a+b-lokal_var
    return result

bilanganPertama = add(10,20)
print(bilanganPertama)

# new variable
nama = "Dicoding Indonesia"
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    # Method object
    def tambah_kecepatan(self):
        self.kecepatan += 10

    # Static method: tidak terikat dengan class nya
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

    # Class Method
    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari class Mobil")

mobil_1 = Mobil('Merah', 'DicodingCar', 200)
print(mobil_1.warna)
print(mobil_1.merek)
print("Before added: ")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()
print("After added: ")
print(mobil_1.kecepatan)

mobil_1.intro_mobil()


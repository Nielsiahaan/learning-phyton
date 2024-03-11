class Car:
    def __init__(self, warna, merk, speed):
        self.warna = warna
        self.merk = merk
        self.speed = speed

    def tambah_kecepatan(self):
        self.speed += 10


class MobilSport(Car):
    def turbo(self):
        self.speed += 50

    # Override
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan Anda meningkat! Hati-Hati!")

# Base Class Car
car1 = Car("Red", "Honda Jazz", 160)
print(car1.speed)

# Mobil Sport class
sportCar = MobilSport("Hitam", "DicodinSportCar", 160)
print(sportCar.speed)
sportCar.turbo()
print(sportCar.speed)

class Kendaraan:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


mobil = Kendaraan(max_speed=200, mileage=15)
motor = Kendaraan(max_speed=150, mileage=20)

print(f"Mobil - Maksimal Kecepatan: {mobil.max_speed} km/jam, Jarak Tempuh: {mobil.mileage} km")
print(f"Motor - Maksimal Kecepatan: {motor.max_speed} km/jam, Jarak Tempuh: {motor.mileage} km")

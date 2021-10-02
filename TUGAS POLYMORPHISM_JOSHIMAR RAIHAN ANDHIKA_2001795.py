#defining parent-class
class Kendaraan:
 brand = "HONDA"
 diskon = 10/100
 def __init__(self,jenis_kendaraan, kapasitas_penumpang, harga_kendaraan):
     self.jk = jenis_kendaraan
     self.kp =kapasitas_penumpang
     self.hk = harga_kendaraan
     self.harga_final = 0
 def potongan_harga(self):
  return self.harga_final + self.hk - int (self.hk * self.diskon)

class Mobil(Kendaraan):
     diskon = 50/100

mobil = Mobil("Mobil", 8, 90000000)

print(f"Harga {mobil.jk} setelah diskon: Rp.{mobil.potongan_harga()}")
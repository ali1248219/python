# module matematika dengan import
from matematika import tambah, kurang, kali

# lebih disarankan menggunakan from dan import ditulis satu persatu dibandingkan yang di bawah, karena susah mencari sumbernya nanti
from matematika import *

# bisa menggunakan alias
from matematika import pangkat as pang

hasil_tambah = tambah(3, 4, 4, 5)
print(f"hasil tambah adalah {hasil_tambah}")

hasil_kurang = kurang(6, 4, 3)
print(f"hasil kurang = {hasil_kurang}")

hasil_pangkat = pang(2)(3)
print(f"hasil pangkat : {hasil_pangkat}")

# fungsi __init__.py adalah mengeksekusi saat kita import package dan menjadi rantai penghubung

import cobainit
from cobainit.fisika import gaya


hasil = cobainit.matematika.tambah(1,4,5,2)
print(hasil)


hasil_gaya = gaya(10,9.8)
print(hasil_gaya)
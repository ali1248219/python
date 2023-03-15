# date and time

import datetime as dt

print("\nSelamat datang di zona ramalan\n")

hari_ini = dt.date.today()
print (f"sekarang tanggal : {hari_ini}\n")
print(f"masukkan informasi tentang kamu")
tanggal = int(input("Masukkan tanggal lahir : "))
bulan = int(input("Masukkan bulan lahir : "))
tahun = int(input("Masukkan tahun lahir : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print(f"berarti kamu lahir di hari {tanggal_lahir:%A} dan umur kamu : {umur_tahun} ")
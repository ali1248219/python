# perulangan (loop)


# for kondisi:
#   aksi

# for dengan list

angkaangka = [0,1,2,3,4,5]
print(angkaangka)

for i in angkaangka:
    print(f"i sekarang {i}")
    
print("akhir dari program")


hewan = ["bebek" , "ayam" , "sapi"]

for i in hewan:
    print(f"di hewan ada {i}")
print("ya itu semua")

# for dengan range

angka_range_1 = range(5)
for i in angka_range_1:
    print(f"sekarang hitung {i}")

angka_range = range(1,10)
for i in angka_range:
    print(f"i sekarang {i}")
    
nama_lengkap = "Feadri Justy Aulia"
for huruf in nama_lengkap:
    print(f"{huruf}")
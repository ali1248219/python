data_angka = [1, 54, 2, 6, 98, 6, 4, 4, 5, 6, 1]
print(data_angka)

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
jumlah_data_1 = data_angka.count(1)
print(jumlah_data_1, jumlah_data_3, jumlah_data_4)

# ambil posisi data

data = ["dindin",  "ucup", "otong"]
print(f"data = {data}")

index_ucup = data.index("ucup")
print(index_ucup)

index_otong = data.index("otong")
print(index_otong)

# mengurutkan list
print(f"sebelum dishort {data}")

data.sort()
data_angka.sort()

print(f"data setelah di sort {data}")
print(f"data setelah di sort {data_angka}")

data.reverse()
data_angka.reverse()
print(f"data setelah di sort {data_angka}")
print(f"data setelah di sort {data}")

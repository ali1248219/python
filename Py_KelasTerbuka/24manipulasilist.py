# operasi data
# index
data = ["dindin",  "ucup", "otong"]

# mengambil data dari list
data_0 = data[0]
print(f"indeks ke 0 adalah {data_0}")
data_akhir = data[-1]
print(f"indeks terakhir adalah {data_akhir}")

# mengambil jumlah data dalam list
panjang_data = len(data)
print(panjang_data)

# manipulasi data list
# nambah data pada list
print(f"data sebelum ditambah : {data}")
data.insert(0, "cecep")
print(f"data sesudah ditambah : {data}")

# menambah diakhir list
# menggunakan append
data.append("coco")
print(f"data sesudah ditambah : {data}")

# menambah list dengan list
data_baru = ["ujang", "anton"]
data.extend(data_baru)
print(f"data sesudah digabung : {data}")

# merubah data
data[2] = "mikael"
print(f"data sesudah diubah : {data}")

# meremove data
data.remove("otong")
print(f"data sesudah dihapus : {data}")

# remove data paling belakang
data.pop()
print(f"data sesudah dipop : {data}")

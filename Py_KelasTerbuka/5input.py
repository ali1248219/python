data = input("Masukkan data : ")

# data yg diinput pasti str

print (f"datanya adalah : {data}, tipe datanya : {type(data)}")

# untuk mengubah menjadi yg lain, butuh casting, contoh :

data_int = int(data)
print (f"datanya adalah : {data_int}, tipe datanya : {type(data_int)}")

# atau bisa juga langsung pada awal pengetikan seperti data = int(input("inpu data"))

# untuk mengubah data ke bool, harus dicasting dalam bentuk int terlebih dahulu baru casting ke bool
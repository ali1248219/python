# merubah satu tipe ke tipe lain
# perubahan data dari float ke int akan membulat ke bawah

data_int = 9
print (f"datanya : {data_int}, tipenya  {type(data_int)}")

data_float = float(data_int)
print (f"datanya : {data_float}, tipenya  {type(data_float)}")

data_bool = bool(data_int)
print (f"datanya : {data_bool}, tipenya  {type(data_bool)}")

data_string = str(data_int)
print (f"datanya : {data_string}, tipenya  {type(data_string)}")
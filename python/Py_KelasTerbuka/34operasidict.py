# operator dict

data_dict = {
    "key" : "value",
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung"
}

# panjang dictionary, untuk membuat konstanta gunakan semuanya huruf kapital

LENDICT = len(data_dict)
print(f"panjang dari dictionary : {LENDICT}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah KEY nya ada ? {CHECKKEY}")

# mengakses value / read dengan get

print(data_dict["cup"])
# bisa membedakan mana dict atau list dll
# gunakan method get
print(data_dict.get("cup"))

# mengupdate data
data_dict["cup"] = "cucup serucup"
print(data_dict)

# menambah data
data_dict["sep"] = "asep seresep"
print(data_dict)

# menggunakan update, kalo data nya exist maka akan diganti, jika tidak ada maka akan ditambah
data_dict.update({"cup" : "ucup surucup"})
print(data_dict)

data_dict.update({"oom" : "oom borobom"})
print(data_dict)

# menghapus / delete

del data_dict["oom"]
print(data_dict)
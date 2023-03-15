# angka tanpa koma = interger
# angka dan koma = float
# kumpulan karakter = string
# data biner True / False = Boolean

data_interger = 1
print (f"datanya bernilai {data_interger}, dan tipe datanya {type(data_interger)}")

data_float = 1.5
print (f"datanya bernilai {data_float}, dan tipe datanya {type(data_float)}")

data_string = "fj"
print (f"datanya bernilai {data_string}, dan tipe datanya {type(data_string)}")

data_bool = False
print (f"datanya bernilai {data_bool}, dan tipe datanya {type(data_bool)}")


# # tipe data khusus
# bilangan kompleks

data_complex = complex(5,6)
print (f"datanya bernilai {data_complex}, dan tipe datanya {type(data_complex)}")

# tipe data bahasa c

from ctypes import c_double

data_c_double = c_double(10.5)
print (f"datanya bernilai {data_c_double}, dan tipe datanya {type(data_c_double)}")
# width and multiline

# data

data_nama = "ucup purucup"
data_umur = 19
data_tinggi = 174.6
data_nomor_sepatu = 40

# string standar
data_string = f"nama : {data_nama}, umur : {data_umur} , tinggi : {data_tinggi}, nomor sepatu : {data_nomor_sepatu}"
print(data_string)

# string multiline menggunakan enter,newline
data_string = f"nama : {data_nama} , \numur : {data_umur} , \ntinggi : {data_tinggi}, \n nomor sepatu : {data_nomor_sepatu}"
print(data_string)

# string multiline menggunakan kutip triplets
data_string = f"""
nama : {data_nama}, 
umur : {data_umur}, 
tinggi : {data_tinggi}, 
nomor sepatu : {data_nomor_sepatu}
"""
print(data_string)

# mengatur lebar
data_nama = "Ucup"
data_string =f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print(data_string)
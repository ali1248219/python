# run time error, error yg terjadi saat runtime

# data_input = int(input(f"masukkan angka :"))
# hasil = 10/data_input

# print(hasil)

# from math import nan    

# bisa gunakan try
# contoh sederhana
# input_user = int(input("masukkan nilai : "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil nya adalah {hasil}")

# contoh pada aplikasi

# while True:
#     angka = int(input("masukkan angka pembagi : "))
#     try:
#         hasil = 10/angka
#         print(f"hasilnya adalah {angka}")
#         is_done = input("apakah mau lanjut ? (y/n) :")
#         if is_done == "n":
#             break
#     except:
#         print("pembagi tidak boleh 0")
# print("akhir dari program")

# contoh aplikasi membuat file.txt
# try:
#     with open("data.txt","r") as file:
#         print(file.read())
# except:
#     print("file tidak ditemukan, membuat file baru")
#     with open("data.txt","w",encoding="utf-8") as file:
#         file.write("file baru")

# print("akhir dari program")

# contoh membuat exeption

# from numbers import Number

# def tambah (a,b):
#     if not isinstance(a,Number) and not isinstance(b,Number):
#         raise "input pertama harus angka"
#     return a+b

# print(tambah(4,3))
# tutorial membaca fiel eksternal


print(3*"=", "membaca file txt", 3*"=")
file = open ("data.txt",mode="r")

# cek status

print(f"apakah status file readable ? : {file.readable()}")
print(f"apakah status file writeable ? : {file.writable()}")

# baca seluruh file
print(file.read())

# print(file.readline(),end=""") #membaca line pertama
# print(file.readline(),end="") #membaca line kedua end adalah untuk menghapus enter pada tiap line

# baca semua baris menjadi list

# print(file.readlines())


# menutup file dengan file.close sedangkan untuk mengecek apakah sudah tertutup dengan file.closed
print(f"apakah file sudah diclosed ? : {file.closed}")
file.close()
print(f"apakah file sudah diclosed ? : {file.closed}")

# salah satu teknik membuat file di python

print(3*"=", "membaca file txt dengan with", 3*"=") #supaya tidak susah make menutup file

with open ("data.txt",mode="r") as file:
    content = file.read()
    print(content,end="")


# latihan mandiri untuk membuka file

with open("data.txt",mode="r") as file:
    content = file.read()
    print(content)
print(f"apakah file sudah di closed ? : {file.closed}")
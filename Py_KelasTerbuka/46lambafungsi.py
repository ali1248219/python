# lambda dan anonymous

# membuat program lebih simpel

def kuadrat(angka):
    return angka**2


print(kuadrat(3))

# kita coba dengan lambda
# output = lambda argument:expression


def lambda_kuadrat(angka): return angka**2


print(lambda_kuadrat(3))


def lambda_2_input(num, pow): return num**pow


print(lambda_2_input(4, 2))

# kegunaan
# membuat sorting list
data_list = ["otong", "dudung", "ucup"]
data_list.sort()
print(data_list)

# sortin berdasarkan jumlah huruf pakai fungsi
data_list = ["otong", "dudung", "ucup"]


def panjang_nama(nama):
    return len(nama)


data_list.sort(key=panjang_nama)
print(data_list)


data_list = ["otong", "dudung", "ucup"]
data_list.sort(key=len)
print(data_list)


# sortin berdasarkan jumlah huruf pakai lambda

data_list = ["otong", "dudung", "ucup"]
data_list.sort(key=lambda nama: len(nama))

# filter

data_angka = [1, 5, 9, 4, 6, 8, 2, 7, 3]
data_angka.sort()
print(data_angka)


def angka_kurang_dari_lima(angka):
    return angka < 5


data_angka_baru = list(filter(angka_kurang_dari_lima, data_angka))
print(data_angka_baru)

data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(data_angka_baru)

# data genap
data_genap = list(filter(lambda x: (x % 2 == 0), data_angka))
print(data_genap)

# data ganjil
data_ganjil = list(filter(lambda x: (x % 2 != 0), data_angka))
print(data_ganjil)

# data kelipatan 3
data_3 = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_3)

# anonymous function
# currying <- haskell curry


def pangkat_biasa(angka, n):
    hasil = angka**n
    return hasil


data_hasil = pangkat_biasa(3, 2)
print(data_hasil)


def pangkat(n):
    return lambda angka: angka**n


pangkat4 = pangkat(4)
print(f"hasil pangkat4 dari angka 2 adalah {pangkat4(2)} ")

print(f"pangkat bebas {pangkat(2)(3)}")

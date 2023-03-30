import numpy as np


# perbedaan array dan list adalah, list masih menggunakan koma untuk pemisah angka, sedangkan array tidak, contoh :
list = [1, 2, 3, 4]
vector_a = np.array([1, 2, 3, 4])

print(f"hasil dari list : {list}")
print(f"hasil dari array : {vector_a}")

# sehingga list tidak bisa langsung kita kali atau pangkatkan, sedangkan array bisa
print(vector_a*2)
print(vector_a+3)  # berarti awal angka di tambah 3

# fungsi utama numpy adalah pada saat penggunaan matriks (sejauh ini)

# buat matrix standar :

matrix_s = np.array([(1, 2), (3, 4)])
print(matrix_s)

matrix_0 = np.zeros((2, 2))
print(matrix_0)

matrix_1 = np.ones((2, 2))
print(matrix_1)


jumlah = matrix_s + matrix_1
print(jumlah)

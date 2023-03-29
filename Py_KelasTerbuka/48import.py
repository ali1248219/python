#  import

# fungsi import adalah ambil program dari external .py

# 1.untuk menyambung program dari external
# INGATTT NAMA FILE TIDAK BOLEH DIAWALI ANGKA
import contohimportfungsi
import contohimport

# 2. import dengan data maka panggil namespace nya dulu

print(contohimport.nama)

# 3. import dengan fungsi
print(f"{contohimportfungsi.math(3,5)}")

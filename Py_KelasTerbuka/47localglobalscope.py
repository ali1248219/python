# local dan global scope variable

nama_global = "dudung"  # akan hidup di manapun


# akses variabel global dalam loop

def fungsi():
    print(f"fungsi menampilkan {nama_global}")


fungsi()

for i in range(0, 5):
    print(f"loop {i} = {nama_global}")


# variabel lokal scope
def fungsi2():
    nama_lokal = "ucup"  # ini bisa diakses hanya di fungsi ini saja

# var tidak akan bisa diakses karena posisinya di global
# fungsi2()
# print(nama_local)

# contoh penggunaan
# urutan variabel haruslah di atas fungsi dll


nama = "otong"


def say_otong():
    print(f"hai teman teman {nama}")


say_otong()

# merubah variabel global

angka = 0


def ubah_angka(nilai_baru):
    # kita deklarasikan dulu variabel untuk emnjadi global, hanya berlaku untuk fungsi
    global angka
    angka = nilai_baru


print(angka)
ubah_angka(10)
print(angka)

tinggi = 10


def ubah_tinggi(nilai_tinggi_baru):
    global tinggi
    tinggi = nilai_tinggi_baru


ubah_tinggi(12)
print(tinggi)

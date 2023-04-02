# __main__ adalah untuk top level code environment


# __name__ = "__main__" akan terjadi jika ada di program utama
print(__name__)

# contoh penggunaan __main__

# deklarasi


def fungsi_tambah(a: int, b: int) -> int:
    return a+b


# fungsi utama

if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1, angka2)
    print(f"hasil tambah = {hasil}")

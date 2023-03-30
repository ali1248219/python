# bisa menggunakan cara di bawah atau

# def cari_terkecil(list_angka):
#     angka_terkecil = list_angka[0]
#     for i in range(1, len(list_angka)):
#         angka = list_angka[i]
#         if angka < angka_terkecil:
#             angka_terkecil = angka
#     return angka_terkecil


# list_angka = [3, 13, 1, 61]
# hasilnya = cari_terkecil(list_angka)
# print(hasilnya)


# bisa menggunakan cara ini
def cariterkecil(list_angka):
    terkecil = min(list_angka)
    return terkecil


list_angka = [3, 13, 1, 61]
nilaiterkecil = cariterkecil(list_angka)

print(f"mencari nilai terkecil, hasilnya : {nilaiterkecil}")


def cariterbesar(list_angka):
    terbesar = max(list_angka)
    return terbesar


list_angka = [3, 13, 1, 61]
nilaiterbesar = cariterbesar(list_angka)
print(f"nilai terbesar nilainya : {nilaiterbesar}")

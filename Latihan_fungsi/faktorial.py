def cari_faktorial(angka):
    hasil_faktorial = 1
    for i in range(1,angka+1):
        hasil_faktorial *= i
    return hasil_faktorial

hasil = cari_faktorial(4)
print(hasil)


def apakahFaktorial(angka):
    hasil = 1
    for i in range(1,angka+1):
        hasil *= i
    return hasil

hasil_hitung = apakahFaktorial(3)
print(hasil_hitung)
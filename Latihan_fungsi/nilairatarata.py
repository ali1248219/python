# mencari nilai rata rata

def cariratarata(list_angka):
    rumus = sum(list_angka) / len(list_angka)
    return rumus


list_angka = [3, 1, 5, 6, 7]
hasilnya = cariratarata(list_angka)
print(hasilnya)

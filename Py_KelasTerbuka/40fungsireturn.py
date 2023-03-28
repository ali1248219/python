# fungsi dengan kembalian (return value)
# y = 2x+1
#  y =f(x)

def fungsi_kuadrat(input_angka) :
    hasil_kuadrat = input_angka **2
    return hasil_kuadrat

y = fungsi_kuadrat(3)
print(y)

z = 10 + fungsi_kuadrat(9)
print(z)

# fungsi dengan return banyak

def operasi_mm(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return tambah, kurang, kali, bagi

# tentukan variable pada fungsi sesuai urutan
tambah, kurang , kali ,bagi = operasi_mm(6,4)

print(f"hasil tambah = {tambah}")
print(f"hasil kurang = {kurang} ")
print(f"hasil kali = {kali}")
print(f"hasil bagi = {bagi}")



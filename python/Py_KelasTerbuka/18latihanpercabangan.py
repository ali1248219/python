# latihan

# kalkulator sederhana
print(20*"x")
print("Kalkulator Expert")
print(20*"x" + "\n")

angka_1= float(input("Masukkan angka pertama : "))
operator= input("Operator (+,-,x,/) :")
angka_2= float(input("Masukkan angka kedua : "))


# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
if operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
if operator == "x" or "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
if operator == "/" or ":":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
    
print("Perhitungan selesai")
# latihan keras

# membuat gabungan area rentang dari angka

# +++++3------10++++

inputUser = float(input(" masukan angka yang nilainya \n kurang dari 3 \n atau \n lebih besar dari 10 : "))

# +++++3---------
# cek angka kurang dari 3
isKurangDari = (inputUser < 3)

# cek angka lebih dari 10
isLebihDari = (inputUser > 10)

# cek keduanya, sebenarnya bisa make OR tp sepertinya mustahil ada kedua angkanya jadi gunakan XOR

isCorrect = isKurangDari ^ isLebihDari
print("------------")
if isCorrect == True:
    print(f"{isCorrect} !! \n angka {inputUser} termasuk angka yang kurang dari 3 atau lebih dari 10")
else:
    print(f" ternyata : {isCorrect} ! \n angka {inputUser} tidak termasuk angka yang kurang dari 3 atau lebih dari 10")

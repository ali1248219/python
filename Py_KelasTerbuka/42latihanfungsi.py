<<<<<<< HEAD
import os
# push
# membuat program menghitung luas dan keliling persegi panjang

# buat header
# buat inti pada input nilai, perkalian

def header():
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING SEGITIGA':^40}")
    print(f"{'-'*40:^40}")

def input_nilai():
    lebar = int(input('Masukkan nilai lebar : '))
    panjang = int(input('Masukkan nilai panjang : '))
    return lebar,panjang #direturn karena mau kita gunakan fungsinya di tempat lain

def luas(lebar,panjang):
    return lebar * panjang #langsung gunakan return

def keliling(lebar,panjang):
    return 2*(lebar + panjang)

def pesan(message,nilai):
    print(f"hasil perhitungan {message} = {nilai}")

# masuk ke program
while True:
    header()
    
    opsi = input("mau hitung luas atau keliling ? : ")
    if opsi == "luas":
        LEBAR, PANJANG = input_nilai()
        LUAS = luas(LEBAR, PANJANG)
        pesan("",LUAS)
    else:    
        LEBAR, PANJANG = input_nilai()
        KELILING = keliling(LEBAR, PANJANG)
        pesan("",KELILING)    
    
    isContinue = input("apakah akan lanjut ? (y/n)")
    if isContinue == "n":
        break
=======
import os
# push
# membuat program menghitung luas dan keliling persegi panjang

# buat header
# buat inti pada input nilai, perkalian

def header():
    os.system('cls')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING SEGITIGA':^40}")
    print(f"{'-'*40:^40}")

def input_nilai():
    lebar = int(input('Masukkan nilai lebar : '))
    panjang = int(input('Masukkan nilai panjang : '))
    return lebar,panjang #direturn karena mau kita gunakan fungsinya di tempat lain

def luas(lebar,panjang):
    return lebar * panjang #langsung gunakan return

def keliling(lebar,panjang):
    return 2*(lebar + panjang)

def pesan(message,nilai):
    print(f"hasil perhitungan {message} = {nilai}")

# masuk ke program
while True:
    header()
    
    opsi = input("mau hitung luas atau keliling ? : ")
    if opsi == "luas":
        LEBAR, PANJANG = input_nilai()
        LUAS = luas(LEBAR, PANJANG)
        pesan("",LUAS)
    else:    
        LEBAR, PANJANG = input_nilai()
        KELILING = keliling(LEBAR, PANJANG)
        pesan("",KELILING)    
    
    isContinue = input("apakah akan lanjut ? (y/n)")
    if isContinue == "n":
        break
>>>>>>> d51f1b36938187345951a805d15431e03e7144f4
print("program selesai")
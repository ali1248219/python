# tugasnya adalah membaut bintang 5 turunan

turunan = 5

# rumus FOR

print("rumus for awal")
bintang = 1
for i in range(turunan):
    print("*"*bintang)
    bintang += 1
print("rumus for akhir")

print("Rumus while awal")

# Rumus While

bintang = 1
while True:
    print("*"*bintang)
    bintang += 1
    
    if bintang > turunan:
        break
print ("Rumus while akhir")


# Menggunakan Continue, mencari yang angka ganjil saja
print("Bintang di angka ganjil")

bintang = 1
turunan = 10
while True:
    if bintang %2 == 1:
        print("*"*bintang)
        bintang +=1
    else:
        bintang +=1
        continue
    if bintang > turunan:
        break
        
# Membuat tutup segitiga

"""
     *
    ***
  *******
************
"""

turunan = 10
bintang_kanan = 1
bintang_kiri = turunan
bentuk = input("Simbol apa yang ingin dijadikan bintang? : ")

while True:
    if bintang_kanan % 2:
        print (" "*bintang_kiri, bentuk * bintang_kanan)
        bintang_kanan +=1
        bintang_kiri -= 1
    else:
        bintang_kanan +=1
        continue
    if bintang_kanan > turunan:
        break
while True:
    if bintang_kanan % 2:
        bintang_kiri += 1
        print (" "*bintang_kiri, bentuk * bintang_kanan)
        bintang_kanan -=1
    else:
        bintang_kanan -=1
    if bintang_kanan == 0:
        break
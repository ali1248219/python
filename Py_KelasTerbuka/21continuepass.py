# continue , pass , break

# pass = dummy yg tidak dieksekusi

angka = 0
while angka < 5:
    angka +=1
    if angka == 3:
        print("wadaw")
        pass #hanya dilewati
    print(angka)
print("laporan selesai") 

# continue , akan membuat loop loncat ke step selanjutnya

angka = 0
print(f"angka sekarang = {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang {angka}")
    
    if angka == 3:
        print("eyyoo")
        continue #ini akan membuat aksi berikutnya ke skip dan lgsg ke step berikutnya, dalam hal ini wazzap ke skip tiap ada angka 3
    
    print("wazzaap")
print("selesai")

# break, akan berhenti apabila kondisi tercapai

angka = 0

while angka < 5:
    angka += 1
    print (f"angka sekarang {angka}")
    if angka == 3:
        print("nice")
        break
    print("wazz")
print("cukup")

rekues = int(input("Masukan berapa kali perulangan : "))
nomor = 0

while True:
    nomor += 1
    print (f"sekarang nomor : {nomor}")
    
    if nomor == rekues:
        print("okeh")
        break
    print ("wzz")
print("cukup")
# program list buku

list_buku = []
while True:
    print("===MASUKAN DATA BUKU===")
    judul = input("masukkan judul \t\t : ")
    penulis = input("masukkan penulis \t : ")
    harga = input("masukkan harga \t\t : ")

    buku_baru = [judul,penulis,harga]
    list_buku.append(buku_baru)
    
    print("No.\t| judul\t\t| penulis\t\t| harga")
    for index,buku in enumerate(list_buku):
        print(f"{index+1}\t | {buku[0]}\t\t | {buku[1]}\t\t | {buku[2]}")
    
    isLanjut = input ("apakah akan dilanjutkan? (y/n)")
    
    if isLanjut == "n":
        break
print("Program selesai")
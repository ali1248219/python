def fungsi1 (nama,tinggi,berat):
    # fungsi biasa
    print(f" namanya : {nama} ,tingginya : {tinggi} ,beratnya : {berat}")

fungsi1("bebek",180,90)


def fungsi(**kwargs): #menjadi dictionary, digunakan untuk membuat option
    # fungsi kwargs
    print(kwargs)

fungsi(nama="ucup",tinggi=190,berat=90)


def math(*args,**kwargs):
    output = 0
    if kwargs["opsi"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["opsi"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print (f"Tidak ada operasi")
    return output
    
hasil = math (1,2,3,5,1,6, opsi = "kali")
print (hasil)
# ketika tidak memberi argumen pada input
# def fungsi(argument):
# def fungsi (argument) = nilai defaultnya : 

# contoh 1
def say_hello(nama = "Kamu"):
    print(f"hallo {nama}")

say_hello()
say_hello("fj")


# contoh 2
def sapa_dia(nama, pesan ="kamu ganteng"):
    # fungsi dnegan satu input biasa dan satu default
    print(f"hai {nama} , {pesan}")

sapa_dia("dudung","hai ganteng")
sapa_dia("toni")

def sapa_doi(nama_sapa = "stranger" , pesan = "hai hai"):
    print(f"{nama_sapa} {pesan}")

sapa_doi("","orang") #kenapa ya tidak bisa default di satu saja? , cukup panggil argumennya dengan nama
sapa_doi(pesan="halloooo")



# contoh 3

def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(3,2))

# untuk kasus argument yg banyak, argumennya bisa dipanggil
print(hitung_pangkat(angka=4,pangkat=5))
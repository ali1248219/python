# fungsi dengan argumen
# fungsi() adalah sebagai argument atau parameter atau input


def hello_world(nama):
    # badan fungsi
    print(f"selamat datang dunia wahai {nama}")


hello_world("FJ")

# program tambah


def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} ditambah {angka_2} = {hasil}")


tambah(5, 3)


def kali(angka3, angka4):
    hasil_kali = angka3 * angka4
    print(f"{angka3} dikali {angka4} = {hasil_kali}")


kali(5, 9)


def kurang(angka5, angka6):
    hasil = angka5 - angka6
    print(f"{angka5} dikurang {angka6} = {hasil}")


kurang(0, 7)


def bagi(angka7, angka8):
    hasil = angka7 / angka8
    print(f"{angka7} dibagi {angka8} = {hasil}")


bagi(9, 3)


def say_hi(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"peserta yang terhormat {peserta}")


# dibawah ini variabelnya bisa bebas namun punya value sama dengan parameter
anggota = ["cucup", "totong", "oom"]
say_hi(anggota)


def panggil_pegawai(list_pegawai):
    for pegawai in list_pegawai:
        print(f"panggilan kepada mas {pegawai}")


list_test = ["dodo", "mari", "ocek"]
panggil_pegawai(list_test)

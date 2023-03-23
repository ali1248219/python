import datetime
import os
import string
import random
# from keys
# template dict mahasisaw


mahasiswa_template = {
    'nama': 'nama',
    'nim': '123456',
    'sks': 0,
    'lahir': datetime.datetime(1111, 11, 11)
}

# bikin dict kosong

data_mahasiswa = {}

while True:
    os.system("cls")

    print(f"{'selamat datang':^20}")
    print(f"{'data mahasiswa':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama mahasiswa: ")
    mahasiswa['nim'] = input("nim mahasiswa: ")
    mahasiswa['sks'] = int(input("sks mahasiswa: "))

    TAHUN_LAHIR = int(input("Tahun Lahir : (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir : (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir : (1-30) : "))
    mahasiswa['lahir'] = datetime.datetime(
        TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<7} {'SKS':<3} {'lahir':<10}")
    print("-"*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks']
        lahir = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<3} {SKS:<3} {lahir:<10}")
    print("\n")
    is_done = input("Sudah selesai input? (y/n)")
    if is_done == "y":
        break

print("\n Akhir dari program mahasiswa")

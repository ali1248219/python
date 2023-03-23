import datetime
import string
import random

# kita akan membuat tabel untuk perjadin sederhana
# yang dibutuhkan : nama, nip, tujuan, tanggal perdin

# formatnya kita buat dulu

pegawai_template = {
    'nama': 'nama',
    'nip': 139784,
    'tujuan': 'bali',
    'kkp': True,
    'tanggal_perdin': datetime.datetime(1111, 11, 11)
}

# bikin dict kosong

pegawai_data = {}

while True:
    print(f"{'selamat datang':^30}")
    print(f"{'penginputan SIMPELKAN':^30}")
    print("-"*30)

    # input data dulu

    pegawai = dict.fromkeys(pegawai_template.keys())
    pegawai['nama'] = input("masukkan nama pegawai : ")
    pegawai['nip'] = int(input("masukkan nip pegawai : "))
    pegawai['tujuan'] = input("masukkan tujuan pegawai : ")
    pegawai['KKP'] = input("Apakah menggunakan KKP ? : (True/False) ")
    TAHUN_BERANGKAT = int(input("Masukkan TAHUN Berangkat : "))
    BULAN_BERANGKAT = int(input("Masukkan BULAN Berangkat : "))
    TANGGAL_BERANGKAT = int(input("Masukkan TANGGAL Berangkat : "))
    pegawai['tanggal_perdin'] = datetime.datetime(
        TAHUN_BERANGKAT, BULAN_BERANGKAT, TANGGAL_BERANGKAT)

    KODE_UNIK = ''.join((random.choice(string.ascii_uppercase)
                        for i in range(4)))
    pegawai_data.update({KODE_UNIK: pegawai})

    print(f"{'KEY':<4} {'nama':<16} {'nip':<6} {'tujuan':<10} {'kkp':<5} {'tanggal_perdin':<10}")
    print("-"*30)

    for pegawai in pegawai_data:
        KEY = pegawai
        NAMA = pegawai_data[KEY]['nama']
        NIP = pegawai_data[KEY]['nip']
        TUJUAN = pegawai_data[KEY]['tujuan']
        KKP = pegawai_data[KEY]['kkp']
        TANGGAL_DINAS = pegawai_data[KEY]['tanggal_perdin'].strftime("%x")
        print(f"{KEY:<4} {NAMA:<16} {NIP:<6} {TUJUAN:<10} {KKP:<5} {TANGGAL_DINAS:<10}")
    print("\n")
    isDone = input("Apakah sudah selesai ? (y/n)")
    if isDone == "y":
        break
print("akhir dari program")

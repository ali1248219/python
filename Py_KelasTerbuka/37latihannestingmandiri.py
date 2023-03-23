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

# while True:
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
KODE_UNIK = ''.join((random.choice(string.ascii_uppercase) for i in range(4)))
pegawai_data.update({KODE_UNIK: pegawai})

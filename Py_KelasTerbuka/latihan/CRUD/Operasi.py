from . import Database
from .util import random_string
import time


# buat fungsi input database
def create_first_data():
    pegawai = input("Pegawai : ")
    lokasi = input("Lokasi : ")
    while (True):
        try:
            tahun = int(input("tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print(
                    "Format yang dimasukkan salah, silahkan masukkan sesuai format yyyy")
        except:
            print("Format yang dimasukkan salah, silahkan masukkan sesuai format yyyy")
# data frame
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["pegawai"] = pegawai + Database.TEMPLATE["pegawai"][len(pegawai):]
    data["lokasi"] = lokasi + Database.TEMPLATE["pegawai"][len(lokasi):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date_add"]} , {data["pegawai"]} , {data["lokasi"]} , {data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Surat tugas tidak ditemukan, silahkan buat surat tugas baru")


# buat fungsi read
def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_pegawai = len(content)
            # print(f" Jumlah pegawai : {jumlah_pegawai}")
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_pegawai:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Fungsi read error")
        return False


def create(tahun, lokasi, pegawai):
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["pegawai"] = pegawai + Database.TEMPLATE["pegawai"][len(pegawai):]
    data["lokasi"] = lokasi + Database.TEMPLATE["pegawai"][len(lokasi):]
    data["tahun"] = str(tahun)
    data_str = f'{data["pk"]}, {data["date_add"]} , {data["pegawai"]} , {data["lokasi"]} , {data["tahun"]}\n'
    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Surat tugas tidak berhasil ditambahkan, ada data yang salah, coba lagi")


def update(no_pegawai, pk, data_add, pegawai, lokasi, tahun):
    data = Database.TEMPLATE.copy()
    data["pk"] = pk
    data["date_add"] = data_add
    data["pegawai"] = pegawai + Database.TEMPLATE["pegawai"][len(pegawai):]
    data["lokasi"] = lokasi + Database.TEMPLATE["pegawai"][len(lokasi):]
    data["tahun"] = str(tahun)
    data_str = f'{data["pk"]}, {data["date_add"]} , {data["pegawai"]} , {data["lokasi"]} , {data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with (open(Database.DB_NAME, 'r+', encoding="utf-8")) as file:
            file.seek(panjang_data*(no_pegawai-1))
            file.write(data_str)
    except:
        print("error dalam update data")

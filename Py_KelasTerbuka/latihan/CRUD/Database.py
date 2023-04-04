from . import Operasi


DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "xxxxxx",
    "date_add": "yyyy-mm-dd",
    "pegawai": 255 * " ",
    "lokasi": 255 * " ",
    "tahun": "yyyy"
}


def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Data Surat Tugas Sudah Tersedia")
    except:
        print("Surat Tugas tidak ditemukan , silahkan buat Surat Tugas baru")
        Operasi.create_first_data()

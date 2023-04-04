from . import Operasi


def read_console():
    data_file = Operasi.read()

    index = "No"
    pegawai = "Pegawai"
    lokasi = "Lokasi"
    tahun = "Tahun"

    # Header
    print("\n" + "="*60)
    print(f"{index:4} | {pegawai:20} | {lokasi:15} | {tahun:5}")
    print("-"*60)

    # Data
    for index, data in enumerate(data_file):  # type: ignore
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        pegawai = data_break[2]
        lokasi = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {pegawai:.20} | {lokasi:.15} | {tahun:4}")
    # Footer
    print("="*60 + "\n")


def create_console():
    print("\n \n" + "="*30)
    print("Silahkan masukkan data Surat Tugas")
    pegawai = input("Pegawai\t: ")
    lokasi = input("lokasi\t: ")
    # buat tahun antisipasi error
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

    Operasi.create(tahun, lokasi, pegawai)
    print("\n berikut ini adalah data baru anda")
    read_console()


def update_console():
    read_console()
    while (True):
        print("silahkan pilih nomor pegawai yang akan diupdate")
        no_pegawai = int(input("nomor pegawai : "))
        data_pegawai = Operasi.read(index=no_pegawai)

        if data_pegawai:
            break
        else:
            print("Nomor tidak valik, coba lagi")

    data_break = data_pegawai.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    pegawai = data_break[2]
    lokasi = data_break[3]
    tahun = data_break[4][:-1]
    # [:-1]-> ini supaya enter pada belakang data tidak diambil

    while (True):
        # ini adalah data yang ingin diubah
        print("\n"+"="*30)
        print("Silahkan pilih data yang mau diubah \n")
        print(f"1. Pegawai \t : {pegawai:.40} ")
        print(f"2. Lokasi \t : {lokasi:.40}")
        print(f"3. Tahun \t : {tahun:.5}")

        # memilih atribut update
        user_option = input("Pilih data : [1,2,3]: ")
        print("\n" + "="*30)
        match user_option:
            case "1": pegawai = input("Pegawai \t : ")
            case "2": lokasi = input("Lokasi \t : ")
            case "3":
                while (True):
                    try:
                        tahun = int(input("tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print(
                                "Format yang dimasukkan salah, silahkan masukkan sesuai format yyyy")
                    except:
                        print(
                            "Format yang dimasukkan salah, silahkan masukkan sesuai format yyyy")
            case _: print("indeks tidak cocok")

        # selesai perbaikan/update
        is_done = input("apakah data yang diedit sudah sesuai ? (y/n) :")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_pegawai, pk, data_add, pegawai, lokasi, tahun)


def delete_console():
    read_console()
    while (True):
        print("silahkan pilih nomor pegawai yang akan didelete")
        no_pegawai = int(input("nomor pegawai : "))
        data_pegawai = Operasi.read(index=no_pegawai)

        if data_pegawai:
            break
        else:
            print("Nomor tidak valik, coba lagi")

    while True:
        data_break = data_pegawai.split(',')
        pk = data_break[0]
        data_add = data_break[1]
        pegawai = data_break[2]
        lokasi = data_break[3]
        tahun = data_break[4][:-1]

        is_done = input("Yakin akan dihapus ? (y/n) :")
        if is_done == "y" or is_done == "Y":
            break

    while (True):
        # ini adalah data yang ingin dihapus
        print("\n"+"="*30)
        print("Silahkan pilih data yang mau dihapus \n")
        print(f"1. Pegawai \t : {pegawai:.40} ")
        print(f"2. Lokasi \t : {lokasi:.40}")
        print(f"3. Tahun \t : {tahun:.5}")

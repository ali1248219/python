# file awal ada di persiapan

# di sini kita akan belajar mengenai database dan operasi serta util

# Header
import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name
    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print("SIMPELKAN, 1 APLIKASI")
    print("UNTUK SELURUH PROSES KEUANGAN")
    print("="*30)

    # cek database ada atau tidak
    CRUD.init_console()

    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("SIMPELKAN, 1 APLIKASI")
        print("UNTUK SELURUH PROSES KEUANGAN")
        print("="*30)

        print("1. Pilih Surat Tugas")
        print("2. Buat Surat Tugas")
        print("3. Edit Surat Tugas")
        print("4. Hapus Surat Tugas \n")
        print("="*30)

        # Inti Program
        user_pilih = input(f"\n Masukkan opsi : ")
        match user_pilih:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete.console()

        print("\n")
        print("="*30)

        # End Program
        is_done = input("apakah selesai ? (y/n) :")
        if is_done == "y":
            break
        print("program selesai")

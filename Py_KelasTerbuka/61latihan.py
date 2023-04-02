import os

if __name__ == "__main__":
    sistem_operasi = os.name
    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(f"{'SELAMAT DATANG DI APLIKASI MAGIC'}")
        print(f"{'MEMPERMUDAH PROSES KEUANGAN UTK SEMUA ORANG YTTA'}")
        print(f"{'='*40}")

        print(f"1. Pilih Surat Tugas")
        print(f"2. Buat Surat Tugas")
        print(f"3. Edit Surat Tugas")
        print(f"4. Hapus Surat Tugas")

        user_option = input(f" \n masukan opsi : ")

        print(f" \n {'='*40} \n")

        match user_option:
            case "1": print("Pilih Surat Tugas")
            case "2": print("Buat Surat Tugas")
            case "3": print("Edit Surat Tugas")
            case "4": print("Hapus Surat Tugas")

        print(f" \n {'='*40} \n")

        is_done = input("apakah selesai ? (y/n) : ")
        if is_done == "y":
            break

    print("Program selesai")

    #  ini tahap pertama

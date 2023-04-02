import os

if __name__ == "__main__":
    sistem_operasi = os.name    
    while True:        
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
    
        print(f"{'SELAMAT DATANG DI APLIKASI MAGIC'}")
        print(f"{'MEMPERMUDAH PROSES KEUANGAN UTK SEMUA ORANG YTTA'}")
        print(f"{'='*40}")
                
        print(f"1. Read Surat Tugas")
        print(f"2. Create Surat Tugas")
        print(f"3. Update Surat Tugas")
        print(f"4. Delete Surat Tugas")
        
        user_option = input(f" \n masukan opsi : ")
        
        print(f" \n {'='*40} \n")
        
        match user_option:
            case "1": print ("Read Data")
            case "2": print ("Create Data")
            case "3": print ("Update Data")
            case "4": print ("Delete Data")
        
        print(f" \n {'='*40} \n")
        
        is_done = input("apakah selesai ? (y/n) : ")
        if is_done == "y":
            break
        
    print ("Program selesai")
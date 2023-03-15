# operasi dan manipulasi

# 1.menyambung string (concatenate) , dengan +
name = "Feadri"
family_name =" Justy Aulia"

full_name = name +""+ family_name
print(full_name)

# 2. menghitung panjang string
panjang = len(full_name)
print(panjang)

# 3. operator untuk string
d = "d"
status = d in full_name
print(status)

D = "D"
status = D not in full_name
print (status)

# mengulang string
print("wk"*10)

# indexing, mengambil data dari string
print("Indeks ke 0 adalah : " + full_name[0])
print("Indeks ke 2 adalah : " + full_name[2])
print("Indeks ke 6 adalah : " + full_name[6])
print("Indeks ke 6-9 adalah : " + full_name[6:10])
print("Indeks ke -2 adalah : " + full_name[-2])
print("Indeks ke 0,2,4,6,8 adalah : " + full_name[0:9:2]) #rumusnya 0 sampai 9 , increment 2

# item paling kecil
print("paling kecil : " + min(full_name))
print("paling kecil : " + max(full_name))

# mengeceknya menggunakan ascii code
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah : " + str(ascii_code))
data = 117
print("char un tuk ASCII 117 adalah " + chr(data))

# 4. Operator dalam bentuk method

data = "otong suruotong"
jumlah = data.count("o") #objek itu data, method itu count
print("jumlah o pada otong adalah : " + str(jumlah))
print(f"jumlah hurug o pada otong adalah {jumlah}")

# 5. Methods

## merubah case dari string
#merubah semua ke upper case dan lowe case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("salam upper : " +salam)
salam = salam.lower()
print("santay dikit : " + salam)

##Pengecekan dengan isX method

#contoh pengecekan lower case
salam = "Sister"
apakah_lower = salam.islower()
print(apakah_lower)
apakah_upper = salam.isupper()
print(apakah_upper) 
apakah_title = salam.istitle()
print(apakah_title)

# isalpha() <-- cek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab , newline
# istitle() <-- cek awal kata huruf kapital

##cek komponen startwith() dan endswith()
cek_start = "Sang Popo".startswith("Sa")
print(cek_start)

## penggabungan komponen join() split()
pisah = ["aku" , "sheyenk" , "kamuh"]
gabungan = " ".join(pisah)
print(gabungan)

# alokasi karakter , rjust() , ljust() , center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'"+ kiri + "'")

tengah = "tengah".center(10)
print("'"+ tengah + "'")

# strip <-- menghilangkan tanda
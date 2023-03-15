# format string

# bisa untuk string, integer, boolean, float

nama = "marlin"
format_str = f"hello {nama}"
print(format_str)

# untuk ribuat bisa diakalin dengan :, atau _ contoh

angka = 100000
format_str = f"ini nilainya {angka:,}"
print(format_str)

# untuk desimal gunakan :. lalu jumlah yg diinginkan dan tambahkan f

angka = 200.22411
format_str = f"nilai belakangnya {angka:.2f}" 
print(format_str)

# menampilkan leading zero

angka = 2422.22
format_str = f"nilai depannya {angka:010.3f}"
print(format_str)

# menampilkan + - menggunakan :+d atau +.

angka_minus = -10
angka_plus = +10
format_minus = f"ini angka minus {angka_minus}"
format_plus = f"ini angka plus {angka_plus:+.2f}"

print (format_minus)
print (format_plus)

# memfotmat persen
persentase = 0.045
format_persentase = f"persentase {persentase:.2 %}"
print(format_persentase)

# format angka lain (binary , octal , hexadecimal)

angka = 233
format_binary = f"binari {bin(angka)}"
format_octal = f"octal {oct(angka)}"
format_hexadecimal = f"hexadecimal {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)
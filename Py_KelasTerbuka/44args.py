"""
*args
"""

# ketika memasukan banyak data pada fungsi, menggunakan bintang

def jumlahkan(*args):
    output = 0
    for angka in args:
        output += angka
    return output

hasil = jumlahkan(3,3,1,1,4,6,7,2)
print(hasil)
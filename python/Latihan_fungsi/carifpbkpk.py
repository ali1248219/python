# langkah pertama input bilangan a dan b yg ingin dicari fpb dan kpk nya
a = int(input("masukkan bilangan pertama : "))
b = int(input("masukkan bilangan kedua : "))

# langkah ke dua buat list kosong
list1 = []
list2 = []

# langkah ketiga masukkan nilai dari 1 sampai a atau b ke list 1
for i in range(1,a+1):
    list1.append(i)
print(list1)

# langkah ke empat masukkan nilai pada list 1 yang memenuhi syarat dapat dibagi habis oleh bilangan a dan b ke list 2 
for x in list1:
    if a%x == 0 and b%x == 0:
        list2.append(x)
print(list2)

# langkah ke lima : FPB adalah elemen terbesar pada list2
fpb = max(list2)
print (fpb)

# langkah ke enam : KPK adalah hasil kali dua elemen a dan b dibagi dengan fpb dari a dan b
kpk = a*b / fpb
print(kpk)
# looping dari list

# for loop

kumpulan_angka = [4,5,6,2,3,1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

# for loop dan range

kumpulan_angka_2 = [2,5,6,1,2]

panjang = len(kumpulan_angka_2)
for i in range(panjang):
    print(f"angka : {kumpulan_angka_2[i]}")

i = 0
while i < panjang:
    print(kumpulan_angka_2[i])
    i+= 1
    if i == panjang:
        break

# list comprehension

data = ["ucup",1,2,3,"otong"]
[print(f" cara simpelnya : {i}") for i in data]

# enumerate

data_list = ["ucup",1,2,3,"otong"]
for index,Value in enumerate(data_list):
    print(f"index : {index}, value : {Value}")
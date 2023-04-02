# list

# kumpulan data numbers

data_angka = [1, 2, 3, 4, 7, 8]
print(data_angka)

# kumpulan data string
data_string = ["ayam", "bebek", "kelinci"]
print(data_string)

# data boolean
data_boolean = [True, False, False, True]
print(data_boolean)


# data campuran
data_campuran = ["babi", 3, "True", 5.5]
print(data_campuran)

# data list

# cara alternatif bikin list
data_range = range(1, 10, 2)  # range : start, stop, step
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehensif , hanya untuk python
list_biasa = list(range(0, 10))
# gunanya list pakai for, angkanya bisa dikuadrat
list_pake_for = [i**2 for i in range(0, 10)]
print(list_biasa)
print(list_pake_for)

# List pakai for pake if
list_pake_for_if = [i**2 for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)

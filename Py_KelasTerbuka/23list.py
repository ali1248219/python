# LIST = kumpulan data alias array

# kumpulan_data = [1,2,8,4,5]
# for i in kumpulan_data:
#     print(i)


# cara alternatif membuat list

data_range = range(0,10,2) #range(start, stop, step)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# list menggunakan for if
list_pake_for_if = [i*3 for i in range (0,10) if i !=5]
print(list_pake_for_if)
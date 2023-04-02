data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"ini list biasa {data_list_biasa}")

list_2d = [data_0,data_1] #bentuknya list dalam list
print(f"list 2D {list_2d}")

# fungsi list : untuk data yang berseri

peserta_1=["ucup",23,"Laki-laki"]
peserta_2=["ipan",24,"wanita"]
peserta_3=["popo",20,"laki-laki"]

list_peserta = [peserta_1,peserta_2,peserta_3]
print(f"para peserta : {list_peserta}")

for peserta in list_peserta:
    print(f"nama \t\t: {peserta[0]}")
    print(f"umur \t\t: {peserta[1]}")
    print(f"jenis kelamin \t: {peserta[2]}")

# tapi ketika melakukan copy list pada nested list dan mengganti data, data list awal akan ikut berubah

list_copy = list_peserta.copy()
print(list_copy)
peserta_1[0] = "otong"
print(list_copy)
print(list_peserta)
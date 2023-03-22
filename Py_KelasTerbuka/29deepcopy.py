data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1]
data_2d_copy = data_2d.copy()
print(f"Data : {data_2d}")
print(f"Data : {data_2d_copy}")

# mengambil data
data = data_2d[0]
print(f"data diambil : {data}")
data = data_2d[0][1]
print(f"data diambil : {data}")

# addres semuanya

print(f"addres data_2d :{hex(id(data_2d))} ")
print(f"addres data_2d :{hex(id(data_2d_copy))} ")

print(f"addres dari member ke 1")
print(f"addres data_2d :{hex(id(data_2d[0]))} ")
print(f"addres data_2d :{hex(id(data_2d_copy[0]))} ")
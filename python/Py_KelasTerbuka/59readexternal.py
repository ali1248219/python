# membuat data terovewrite
# dia akan membuat file baru bila tidak ada

#  mengganti file lama
# with open("data.txt" , mode="w",encoding="utf-8") as file:
#     file.write(f"cup surucup")

# # mode append
# # with open("data.txt",mode="a",enc
# # oding="utf-8") as file:
# #     file.write(f"\n ton si toni")


# fungsi r+ akan menimpa isi text
with open("data.txt","r+",encoding="utf-8") as file:
    data = file.read() #bisa juga dilihat datanya
    file.write("menambah dengan r+") #file akan tertimpa
    print(data)
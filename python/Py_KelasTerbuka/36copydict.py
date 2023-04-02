# copy dictionary

teman_teman = {
    "cup": "serucup",
    "tong": "melotong",
    "dip": "skididip",
    "poo": "poproo"
}

friends = teman_teman.copy()
teman_teman[0] = "cip"
print(f"teman-teman : {teman_teman}")
print(f"friends : {friends}")

# pop dictionary ke value dictionary
dataAsep = friends.pop("poo")
print(f"data Asep : {dataAsep}")
print(f"data friends : {friends}")

# popitem dictionary ke value terakhir
dataTerakhir = friends.popitem()
print(f"data terakhir : {dataTerakhir}")

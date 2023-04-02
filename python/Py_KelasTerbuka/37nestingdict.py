# multikeys and nesting

import datetime

mahasiswa1 = {
    "nama": "cucup",
    "NIM": "1232323",
    "SKS_LULUS": 30,
    "beasiswa": False,
    "lahir": datetime.datetime(1999, 4, 29)
}

mahasiswa2 = {
    "nama": "totong",
    "NIM": "1232326",
    "SKS_LULUS": 30,
    "beasiswa": True,
    "lahir": datetime.datetime(2000, 2, 29)
}

mahasiswa3 = {
    "nama": "brooo",
    "NIM": "1232226",
    "SKS_LULUS": 30,
    "beasiswa": False,
    "lahir": datetime.datetime(2004, 5, 2)
}

data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3
}

print(f"{'KEY':<6} {'NAMA':<17} {'NIM':<7} {'SKS':<3} {'Beasiswa':<9} {'lahir':<10}")
print("-"*60)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['NIM']
    SKS = data_mahasiswa[KEY]['SKS_LULUS']
    beasiswa = data_mahasiswa[KEY]['beasiswa']
    lahir = data_mahasiswa[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<17} {NIM:<3} {SKS:<3} {beasiswa:^9} {lahir:<10}")

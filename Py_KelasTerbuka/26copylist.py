# teknik menduplikat list

data = ["ucup", "utup", "aduduu"]
print(f"data = {data}")

klon = data  # pass by reference
print(f"data = {klon}")

# kita akan merubah member dari a
# semua akan terpenaruh meskipun salah satunya diapa2kan
data[1] = "totok"
klon.sort()
print(f"data = {data}")
print(f"data = {klon}")

# karena addresnya sama

print(f"addres dari data = {hex(id(data))}")
print(f"addres dari klon = {hex(id(klon))}")

# caranya adalah dengan copy

kopi = data.copy()  # full duplikat data baru
print(kopi)
print(f"addres dari kopi = {hex(id(kopi))}")

kopi[0] = "ucok baba"
print(f"kopi = {kopi}")

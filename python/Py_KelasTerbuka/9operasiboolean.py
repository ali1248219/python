# operasi logika atau boolean

# not, or , xor , and

# not , akan menjadikan variabel negasi dari aslinya
print(f"---NOT---")
a = True
b = not a

print(f"a = {a} , b = {b}")

# or harus ada minimal 1 true maka true.
print (f"---OR---")
a = True
b = False
c = a or b
print (f"a = {a}, b = {b}, c = {c}")

# xor , harus salah satu True, sisanya false
print(f"---XOR---")
a = True
b = True
c = a ^ b
print (f"a = {a}, b = {b}, c = {c}")

# and , keduanya harus True
print(f"---AND---")
a = True
b = False
c = a and b
print(f"a = {a} , b = {b}, c = {c}")
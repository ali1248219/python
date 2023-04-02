# operasi bitwise atau binari, dalam bahasa indo = operasi masing masing bit

a = 9
b = 5

# bit wise or (|)
c = a | b
print (f"nilai a : {a} , dan binernya : {format(a,'08b')} ")
print (f"nilai b : {b} , dan binernya : {format(b,'08b')} ")
print (f"nilai c : {c} , dan binernya : {format(c,'08b')} ")

# bit wise and (&)
c = a & b
print (f"nilai a : {a} , dan binernya : {format(a,'08b')} ")
print (f"nilai b : {b} , dan binernya : {format(b,'08b')} ")
print (f"nilai c : {c} , dan binernya : {format(c,'08b')} ")

# bit wise xor (^)
c = a ^ b
print (f"nilai a : {a} , dan binernya : {format(a,'08b')} ")
print (f"nilai b : {b} , dan binernya : {format(b,'08b')} ")
print (f"nilai c : {c} , dan binernya : {format(c,'08b')} ")

# bit wise not (~)
c = ~a
print (f"nilai a : {a} , dan binernya : {format(a,'08b')} ")
print (f"nilai b : {b} , dan binernya : {format(b,'08b')} ")
print (f"nilai c : {c} , dan binernya : {format(c,'08b')} ")

#shift right (>>) dan shift left (<<)
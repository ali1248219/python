"""
RANGE FUNCTIOIN PYTHON

for i in range (1,5,1) -> start , stop , step
start = optional dan dimulai dari 0
stop = wajib di isi dan stopnya itu merupakan angka sebelum yg disebutkan
step = optional dan dimulai dari 1
"""

for i in range(5): #dengan begini akan otomatis stop di angka 4, start dan step menjadi default
    print(i, end="  ") #tulisan end adalah untuk pemisah jaraknya

print("\n")

for i in range(3,12+1,3): #dengan begini akan stop di angka 12. karena ditambah 1
    print(i,end="  ")

print("\n")

for i in range(13,0,-1): #dengan begini akan menjadi decrement
    print(i,end="  ")
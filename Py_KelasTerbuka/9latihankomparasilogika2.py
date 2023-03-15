# tugasnya itu ngebuat 2 rumus ini satu persatu, tp kayaknya bakal saya bikin menjadi opsi saja

# a = -----0++++5----8+++++11-----

# b = ++++0----5+++++8-----11+++++

inputUser = float(input("Masukkan angka : "))

#cek komparasi a dan b
isCorrectA = (inputUser >= 0 and inputUser <= 5) or (inputUser >= 8 and  inputUser <=11)
isCorrectB = (inputUser <= 0 or inputUser >=5) and (inputUser <= 8 or inputUser >= 11)
print (f"angka {inputUser} jika di cek menggunakan opsi A maka : {isCorrectA}")
print (f"angka {inputUser} jika di cek menggunakan opsi B maka : {isCorrectB}")
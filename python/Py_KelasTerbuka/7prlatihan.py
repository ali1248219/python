# bikin konversi dari fahrenheit ke kelvin

print("\n Fahrenheit ke Kelvin \n")

fahrenheit = float(input("masukan suhu dalam fahrenheit : "))
print(f"suhu dalam fahrenheit : {fahrenheit} fahrenheit")

# konversikan fahrenheit ke celcius

celciusfahrenheit = (5/9) * (fahrenheit - 32)
print (f"suhu dalam celcius : {celciusfahrenheit} celcius")

#  konversikan fahrenheit ke reamur

reamurfahrenheit = (4/9) * (fahrenheit - 32)
print (f"suhu dalam reamur : {reamurfahrenheit} reamur")

# dari celcius konversi ke kelvin

kelvincelciusfahrenheit = celciusfahrenheit +273
print (f"suhu dalam kelvin : {kelvincelciusfahrenheit} kelvin")

# dari reamur konversi ke kelvin

kelvinreamurfahrenheit = ((5/4) * reamurfahrenheit) + 273
print (f"suhu dalam kelvin : {kelvinreamurfahrenheit} kelvin")


# bikin konversi dari kelvin ke fahrenheit

print("\n========================\n")

kelvin = float(input("masukan suhu dalam kelvin : "))
print (f"suhu dalam kelvin : {kelvin} kelvin")

# konversi kelvin ke celcius
celciuskelvin = kelvin - 273
print(f" suhu dalam celcius : {celciuskelvin} celcius")

#  konversi kelvin ke reamur

reamurkelvin = (4/5) * (kelvin-273)
print(f" suhu dalam reamur : {reamurkelvin} reamur")

# konversi celcius ke fahrenheit

fahrenheitcelciuskelvin = (9/5) * (celciuskelvin + 32 )
print(f" suhu dalam fahrenheit : {fahrenheitcelciuskelvin} fahrenheit")

# konversi reamur ke fahrenheit

fahrenheitreamurkelvin = 9/4 * (reamurkelvin + 32)
print(f" suhu dalam fahrenheit : {fahrenheitreamurkelvin} fahrenheit")
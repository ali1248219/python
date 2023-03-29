"""
TYPE HINTS PADA FUNGSI, digunakan untuk membuat orang tahu harus mengisi apa pada parameterny
"""

# bentuk standar fungsi

# def fungsi (parameter):
#     print(parameter)

# fungsi(1)
# fungsi("cup")

# penggunaan type hints

def fungsi_dengan_hints(argument:int) -> int: #ini adalah bentuk type hints. yg kiri adalah bentuk awal dan yg akhir adalah bentuk hasil 
    output = 10**argument
    return output

hasil = fungsi_dengan_hints(2)
print(hasil)

def display(argument:str):
    print(argument)

display("ucup")
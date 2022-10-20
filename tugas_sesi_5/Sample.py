# Contoh Coding Sederhana
def tambah():
    a = int(inp("Angka 1: ")
    b = int(inp("Angka 2: ")
    c = a + b
    print(c)

def kurang():
    a = int(inp("Angka 1: ")
    b = int(inp("Angka 2: ")
    c = a - b
    print(c)

def kali():
    a = int(inp("Angka 1: ")
    b = int(inp("Angka 2: ")
    c = a * b
    print(c)

def bagi():
    a = int(inp("Angka 1: ")
    b = int(inp("Angka 2: ")
    c = a / b
    print(c)

def pilihan():
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("Exit")

while True:
    pilihan()
    pil = int(inp("Pilihan : ")
    if pil == 1:
        tambah()
    elif pil == 2:
        kurang()
    elif pil == 3:
        kali()
    elif pil == 4:
        bagi()
    else:
        break

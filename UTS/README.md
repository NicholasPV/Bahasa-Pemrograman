# Bahasa Pemrograman - UTS
Nama  : Nicholas Patrick Varian\
NIM   : 20210801102\
Prodi : Teknik Informatika

## Nomor 1
Source Code:
```py
print("saya belajar Bahasa Pemrograman menggunakan python")
```

## Nomor 2
Source Code:
```py
print("MENGHITUNG LUAS SEGITIGA")
alas = int(input("Masukkan Alas: "))
tinggi = int(input("Masukkan Tinggi: "))
luas = alas * tinggi / 2
print(luas)
```

## Nomor 3
Source Code:
```py
print("====================\nPROGRAM QUIZ\n====================")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
print("\nNama: " + nama + "\nNIM: " + nim)
```

## Nomor 4
Source Code:
```py
print("====================\nNESTED LOOPING\n====================")
pulau = ["Kalimantan", "Sumatra", "Sulawesi"]
bagian = [" West", " North", " South"]
for a in range(3):
    for b in range(3):
        print(pulau[a] + bagian[b])
```

## Nomor 5
Source Code:
```py
print("====================\nPROGRAM MENU\n====================")
def menu():
    nama = input("\nMasukkan Nama: ")
    nim = input("Masukkan NIM: ")
    print("Pilihan:\n1. Capucino\n2. Teh\n3. Exit")
    
def capucino():
    print("Memilih Capucino")
    harga = int(input("Masukkan Harga: "))
    ppn = harga * 10/100
    total = harga + ppn
    print("Jumlah yang harus dibayar adalah Rp. " + str(total))
    
def teh():
    print("Memilih Teh")
    harga = int(input("Masukkan Harga: "))
    ppn = harga * 10/100
    total = harga + ppn
    print("Jumlah yang harus dibayar adalah Rp. " + str(total))
    
while True:
    menu()
    pil = int(input("Masukkan Pilihan: "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print("Pilihan tidak ada. Silahkan pilih kembali.")
```

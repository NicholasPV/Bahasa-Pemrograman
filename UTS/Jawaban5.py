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

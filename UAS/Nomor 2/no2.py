def exceptionHandling():
    try:
        pembilang = int(input("Masukkan Angka 1: "))
        penyebut = int(input("Masukkan Angka 2: "))

        hasil = pembilang / penyebut

        print("Hasilnya adalah ", hasil)
    except:
        print("Error: Penyebut tidak boleh bernilai 0.")
    finally:
        print("Program Exception Handling telah selesai dijalankan.")

exceptionHandling()

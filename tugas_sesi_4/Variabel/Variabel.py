# Variabel
a = "Nicholas"
def func():
    a = "Patrick"
    print("Selamat " + a)
func()
print(a)

# Definisi
# Def namaFungsi(Parameter)
def tambah():
    a = 10
    b = 5
    c = a + b
    print(c)
tambah()

# Definisi Parameter
def data(nama, nim):
    print(f"Nama saya adalah {nama} dengan {nim}")
data("Nicholas", "20210801102")

# Contoh
def luasPersegi(sisi):
    return sisi * sisi
luasPersegi(10)

def luasSegitiga(alas, tinggi):
    return 0.5 * alas * tinggi
luasSegitiga(10, 5)

import mysql.connector

# Koneksi ke database
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="no5patrick"
)
cursor = connect.cursor()

# Membuat tabel
create_table = """
CREATE TABLE Makanan (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nama VARCHAR(50),
    Makanan VARCHAR(50)
)
"""
cursor.execute(create_table)

add_user = "INSERT INTO Makanan (Nama, Makanan) VALUES (%s, %s)"
user_data = ("Mwehehe", "Borgar")
cursor.execute(add_user, user_data)
connect.commit()

# Mengambil data
query = "SELECT * FROM Makanan"
cursor.execute(query)

for (ID, Nama, Makanan) in cursor:
    print("ID: {}, Nama: {}, Makanan: {}".format(ID, Nama, Makanan))

# Menutup koneksi
cursor.close()
connect.close()

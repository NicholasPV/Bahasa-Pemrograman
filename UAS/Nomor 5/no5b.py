import mysql.connector
import tkinter as tk

# Connect to the database
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="no5patrick"
)

# Create a cursor
cursor = connect.cursor()

# Function to insert data into the database
def insert_data():
    name = entry_name.get()
    makanan = entry_makanan.get()
    cursor.execute("INSERT INTO Makanan (Nama, Makanan) VALUES (%s, %s)", (name, makanan))
    connect.commit()
    label.config(text="Data berhasil dimasukkan!")

# Function to fetch data from the database
def fetch_data():
    cursor.execute("SELECT * FROM Makanan")
    results = cursor.fetchall()
    return results

# GUI
window = tk.Tk()
window.title("Input Data ke Database")

label = tk.Label(window, text="Masukkan Data:")
label.grid(row=0, column=0, columnspan=2)

name_label = tk.Label(window, text="Name:")
name_label.grid(row=1, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

makanan_label = tk.Label(window, text="Makanan:")
makanan_label.grid(row=2, column=0)
entry_makanan = tk.Entry(window)
entry_makanan.grid(row=2, column=1)

insert_button = tk.Button(window, text="Insert", command=insert_data)
insert_button.grid(row=4, column=0, columnspan=2)

window.mainloop()

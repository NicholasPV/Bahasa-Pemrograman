import tkinter

window = tkinter.Tk()
window.title("Contoh GUI Python")

nama = tkinter.Label(window, text = "Nama: Nicholas Patrick Varian")
nama.pack()
nim = tkinter.Label(window, text = "NIM: 20210801102")
nim.pack()
prodi = tkinter.Label(window, text = "Prodi: Teknik Informatika")
prodi.pack()

def click():
    button.config(text = "I was Clicked")

button = tkinter.Button(window, text = "Click Me", command = click)
button.pack()

window.mainloop()

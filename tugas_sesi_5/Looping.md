# Looping
Looping adalah sebuah urutan perintah yang secara terus menerus diulang sampai mencapai suatu kondisi tertentu.

## Looping with Range
Dalam Python, looping menggunakan range digunakan untuk melakukan pengulangan sebanyak angka yang dimasukkan dalam range.\
for var in range(3):\
    print(var)

## Looping with Break
Dalam Python, dalam proses looping dapat digunakan break. Break berguna untuk menghentikan pengulangan jika memenuhi kondisi tertentu. Sebagai contoh, pada code di bawah, break akan menghentikan looping jika menemukan huruf "g".\
for b in "Pemrograman":\
    if b == "g":\
        break\
    print(b)

## Looping with Continue
Dalam Python, dalam proses looping dapat digunakan continue. Continue berguna untuk melewati/skip satu siklus pengulangan jika memenuhi kondisi tertentu. Sebagai contoh, pada code di bawah, continue akan dilakukan saat menemukan huruf "r", sehingga huruf "r" tidak akan di print.\
for c in "Pemrograman":\
    if c == "r":\
        continue\
    print(c)

## Nested Loop
Nested Loop adalah looping yang berada di dalam sebuah looping lainnya.

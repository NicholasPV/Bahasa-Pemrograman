from array import *
import array as arr 

# Array Bilangan Bulat
numbers = arr.array("a" ,[10, 20, 30])
print(numbers)

# Array Bilangan Desimal
numbers = array("b" ,[10.0, 20.0,30.0])
print(numbers)

# Mencetak Elemen Array
numbers = arr.array('i',[10, 20, 30])
print(numbers[0]) # Elemen Pertama
print(numbers[1]) # Elemen Kedua
print(numbers[2]) # Elemen Ketiga

print(numbers[-1]) # Elemen Terakhir
print(numbers[-2]) # Elemen Kedua Terakhir
print(numbers[-3]) # Elemen Ketiga Terakhir

# Mencetak Array sesuai Index
numbers = arr.array('i',[10, 20, 30])
print(numbers.index(10)) # Elemen pada Indeks ke-10

numbers = arr.array('i',[10, 20, 30, 10, 20, 30])
print(numbers.index(5))

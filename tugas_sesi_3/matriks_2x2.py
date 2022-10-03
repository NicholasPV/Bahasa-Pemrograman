#Matriks 2x2
matriksA = [[1, 2], [2, 3]]
matriksB = [[9, 8], [7, 6]]

tambahAB1 = matriksA[0][0] + matriksB[0][0], matriksA[0][1] + matriksB[0][1]
tambahAB2 = matriksA[1][0] + matriksB[1][0], matriksA[1][1] + matriksB[1][1]

kurangAB1 = matriksA[0][0] - matriksB[0][0], matriksA[0][1] - matriksB[0][1]
kurangAB2 = matriksA[1][0] - matriksB[1][0], matriksA[1][1] - matriksB[1][1]

print("Matriks A =")
print([matriksA[0][0]], [matriksA[0][1]])
print([matriksA[1][0]], [matriksA[1][1]])
print()

print("Matriks B =")
print([matriksB[0][0]], [matriksB[0][1]])
print([matriksB[1][0]], [matriksB[1][1]])
print()

print("Hasil Penjumlahan Matriks A + B =\n" + str([tambahAB1]) + "\n" + str([tambahAB2]) + "\n")
print("Hasil Pengurangan Matriks A - B =\n" + str([kurangAB1]) + "\n" + str([kurangAB2]))

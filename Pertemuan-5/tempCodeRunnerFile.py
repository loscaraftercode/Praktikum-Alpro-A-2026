def kurang_matriks(matrix_A, matrix_B):
    baris, kolom = len(matrix_A), len(matrix_A[0])
    hasil = [[matrix_A[i][j] - matrix_B[i][j] for j in range(kolom)] for i in
range(baris)]

matrix_A = [[5, 3, 1],
            [2, 8, 4],
            [6, 0, 7]]
matrix_B = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
C_kurang = kurang_matriks(matrix_A, matrix_B)
for baris in C_kurang
    print (baris)
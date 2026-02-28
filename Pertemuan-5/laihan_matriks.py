
#menjumlahkan matriks a dan b simpan dalam variabel c_tambah
def tambah_matrix(matrix_A, matrix_B):
        if len(matrix_A) != len(matrix_B) or len(matrix_A[0]) != len (matrix_B[0]):
                print('Error: ukuran matriks tidak sama')
                return  None
        baris, kolom = len(matrix_A), len(matrix_A[0])
        hasil = [[matrix_A[i][j] + matrix_B[i][j] for j in range(kolom)] for i in range(baris)]
        return hasil 

matrix_A = [[5, 3, 1],
            [2, 8, 4],
            [6, 0, 7]]
matrix_B = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
C_tambah = tambah_matrix(matrix_A, matrix_B)
print("hasil penjumlahan matriks:")
for baris in C_tambah:
    print(baris)

#matriks a - b simpan dalam variabel c_kurang
def kurang_matriks(matrix_A, matrix_B):
    baris, kolom = len(matrix_A), len(matrix_A[0])
    hasil = [[matrix_A[i][j] - matrix_B[i][j] for j in range(kolom)] for i in
range(baris)]
    return hasil

matrix_A = [[5, 3, 1],
            [2, 8, 4],
            [6, 0, 7]]
matrix_B = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
C_kurang = kurang_matriks(matrix_A, matrix_B)
print ("hasil pengurangan matriks:")
for baris in C_kurang:
    print(baris)
    
#mengalikan skalar, c_skalar
def kali_skalar(matriks, k):
    hasil = []
    for baris in matriks:
        baris_baru = [elemen * k for elemen in baris]
        hasil.append(baris_baru)
    return hasil
    
matrix_A = [[5, 3, 1],
            [2, 8, 4],
            [6, 0, 7]]

C_skalar = kali_skalar(matrix_A, 3)
print("hasil perkalian skalar matriks")
for baris in C_skalar:
    print(baris)


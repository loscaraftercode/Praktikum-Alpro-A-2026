def input_angka(pesan, tipe='int'):
    while True:
        try:
            nilai = input(pesan)
            if tipe == 'int':
                return int(nilai)
            elif tipe == 'float' :
                return float(nilai)
            
        except ValueError:
            print(f' input tidak valid!, masukan angka {tipe}.')
    
angkaPertama = input_angka('Masukkan angka pertama: ', 'int')
angkaKedua = input_angka('Masukkan angka kedua: ', 'int')

try:
    hasil = angkaPertama / angkaKedua
    print(f'Angka Pertama: {angkaPertama}, Angka Kedua: {angkaKedua} ')
    print(f'hasil baginya adalah: {hasil}')
except ZeroDivisionError:
    print("Erorr : tidak bisa membagi dengan nol.")
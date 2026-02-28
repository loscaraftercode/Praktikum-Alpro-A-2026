angka_list = [10, 20, 30, 40, 60]
try:
    idx = int(input('Masukkan index (0-5): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')
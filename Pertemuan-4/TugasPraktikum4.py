#kita membuat custom exception
class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__(f' Nama terlalu pendek! Nama minimal 3 karakter!')

class UmurError(Exception):
    def __init__(self, umur):
        self.umur = umur
        super().__init__(f'umur tidak memenuhi. syarat umur antara 17-60 Tahun.')

class EmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__("Tidak Valid! Email Harus mengandung'@'!")

class NomorError(Exception):
    def __init__(self, no_HP):
        self.no_HP = no_HP
        super().__init__("Nomor HP harus 10-13 digit!")

#kita membuat fungsi validasi
def validasi_nama(nama):
    if len(nama) < 3:
        raise NamaError(nama)

def validasi_umur(umur):
    if umur < 17 or umur > 60:
            raise UmurError(umur)

def validasi_email(email):
    if "@" not in email:
        raise EmailError(email) 

def validasi_noHP(no_HP):
    if not no_HP.isdigit():
        raise NomorError(no_HP)
    if not 10 <= len(no_HP) <= 13:
            raise NomorError("Nomor HP harus 10-13 digit!")

    return True

#kita memmbuat struktur input dan Try-Except
print("=== REGISTRASI PESERTA SEMINAR ===")
while True:
    try:
        nama = input("Nama Lengkap:")
        validasi_nama(nama)
        break
    except NamaError as e :
        print("[ERROR]", e)
while True:
    try:
        umur = int(input("Umur:"))
        validasi_umur(umur)
        break
    except UmurError as e :
        print("[ERROR]", e)
        
while True:
    try:
        email = input("Email:")
        validasi_email(email)
        break
    except EmailError as e :
        print("[ERROR]", e)
        
while True:
    try:
        no_HP = input("No HP:")
        validasi_noHP(no_HP)
        break
    except NomorError as e :
        print("[ERROR]", e)
        
print ("Proses input selesai.")

#kita membuat tampilan output akhir
print("\n=== DATA PESERTA ===")
print(f'Nama     :{nama}')
print(f'Umur     :{umur}')
print(f'Email    :{email}')
print(f'Nomor HP :{no_HP}')
print("Status   : TERDAFTAR") 
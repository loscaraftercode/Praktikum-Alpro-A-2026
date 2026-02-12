#soal 1
def fizzbuzz_plus(n):
    for i in range (1, n + 1):
        hasil = ""

    if i % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:         
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if i % 7 == 0:
        print ("seven")
    
    if hasil == "":
        print(i)
    else:
        print(hasil)

fizzbuzz_plus(28)

#soal 2

def is_password_valid(password)
    
    
is_password_valid(password)

#soal 3
def hitung_nilai(tugas, uts, uas):

    nilai = tugas*0.3 + uts*0.3 + uas*0.4

    if nilai >= 85:
        print ("grade:A")
    elif nilai >= 70:
        print ("grade:B")
    elif nilai >= 55:
        print ("grade:C")
    elif nilai >= 40:
        print ("grade:D")
    elif nilai <40:
        print ("grade:E")
    print("Nilai : ", nilai)
hitung_nilai(80, 75, 90)

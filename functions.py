#Python Function
# fungsi adalah kode yang akan jalan jika dipanggil

#bikin fungsi:
def my_function():
  print("Hello from a function") 

#cara memanggil:
my_function()

#bisa memanggil fungsi beberapa kali:
def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#Function Names
#valid:
calculate_sum()
_private_function()
myFunction2()

#kenapa menggunakan fungsi?
#contoh saat ngin mengkonversi suhu dari farenheit ke celcius beberapa kali  dalam program. tanpa fungsi, kita menulis kode dengan perhitungan yang sama berulang kali.

#tanpa fungsi
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3) 

#dengan fungsi:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50)) 

#mengembalikan nilai:
#bisa mengembalikan nilai yang ada di kode dengan menmanggil perinth return.
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)  #output: Hello from a function

#bisa menggunakan perintah mengembalikan nilai seperti biasa:
def get_greeting():
  return "Hello from a function"

print(get_greeting()) 

#Python Function Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 

#Parameters vs Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") 

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")  #error jika 1 yang panggil

#Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus") 

#Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog") 

#Positional Arguments
# saat memanggil fungsi dengan argumen tanpa menggunakan kata kunci, argumen tersebut disebut argumen posisional.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#bisa ditukar
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog") 


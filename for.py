#Python for Loops
# perulangan ini melakukan iterasi pada sebuah urutan (misalnya, daftar, tuple, string, atau rentang) dan mengeksekusi blok kode untuk setiap item dalam urutan tersebut.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)
#Output: b a n a n a
#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  #output: apple banana 

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#output: apple cherry

#The range() Function
for x in range(6):
  print(x)
#output: 0 1 2 3 4 5

for x in range(2, 6):
  print(x) 
#output: 2 3 4 5

#lompat 3 angka
for x in range(2, 30, 3):
  print(x)
for x in range(2, 30, 3):

  print(x) 
#output: 2 5 8 11 14 17 20 23 26 29

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!") 

for x in range(6):
if x == 3: break
  print(x)
else:
  print("Finally finished!") 

#Nested Loops
#adalah loop didalam loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 


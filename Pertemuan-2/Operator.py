#Python Operators
print(10 + 5) 
#contoh:

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400) 

#Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Division in Python
#Python has two division operators:

#/ - Division (returns a float)
x = 12
y = 5

print(x / y)
#// - Floor division (returns an integer)
x = 12
y = 5

print(x // y)

#Assignment Operators
#Operator masukan digunakan untuk menetapkan nilai ke variabel
= 	x = 5 	x = 5 	
+= 	x += 3 	x = x + 3 	
-= 	x -= 3 	x = x - 3 	
*= 	x *= 3 	x = x * 3 	
/= 	x /= 3 	x = x / 3 	
%= 	x %= 3 	x = x % 3 	
//= 	x //= 3 	x = x // 3 	
**= 	x **= 3 	x = x ** 3 	
&= 	x &= 3 	x = x & 3 	
|= 	x |= 3 	x = x | 3 	
^= 	x ^= 3 	x = x ^ 3 	
>>= 	x >>= 3 	x = x >> 3 	
<<= 	x <<= 3 	x = x << 3 	
:= 	print(x := 3) 	x = 3
print(x) 	

#Python Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#output berupa true atau false

#Chaining Comparison Operators
#kita bisa menggunakan perbandingan operator yang berturut

x = 5

print(1 < x < 10)

print(1 < x and x < 10)

#Python Logical Operators

#and
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

#or
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

#not
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

#Python Identity Operators
#Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
#is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
#is not
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Difference Between is and ==

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y) # output: false
print(x is y) # output : true

#Python Membership Operators
#Membership Operators
#is
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) #output: false
# is not
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits) #true

#Membership in Strings
text = "Hello World"

print("H" in text) #output: true
print("hello" in text) #output : false
print("z" not in text) #output : true

#Python Bitwise Operators
#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print(6 & 3)
#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
print(6 | 3)
#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
print(6 ^ 3)

#Python Operator Precedence
print((6 + 3) - (6 + 3)) 
print(100 + 5 * 3) 

#Left-to-Right Evaluation
#Jika dua operator memiliki prioritas yang sama, ekspresi dievaluasi dari kiri ke kanan.
print(5 + 4 - 7 + 3) # output: 5


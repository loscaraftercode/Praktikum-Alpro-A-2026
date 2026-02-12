#Python Conditions and If statements
a = 33
b = 200
if b > a:
  print("b is greater than a")

  number = 15
if number > 0:
  print("The number is positive")
  a = 33

#Indentation
a = 33
b = 200
if b > a:
  print("b is greater than a") # you will get an error 
#salah letak spasi bisa menimbulkan error

#Multiple Statements in If Block
age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


#Using Variables in Conditions
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#Python Elif Statement
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Multiple Elif Statements
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#how elif works
#When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

#when to use elif
#Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")



#Python Else Statement
#The Else Keyword
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Else Without Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#How Else Works
#The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Complete If-Elif-Else Chain
#You can combine if, elif, and else to create a comprehensive decision-making structure.
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


# Python Shorthand If
# Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
a = 5
b = 2
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


#Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Python Logical Operators
#Logical operators are used to combine conditional statements. Python has three logical operators:

    #and - Returns True if both statements are true
    #or - Returns True if one of the statements is true
    #not - Reverses the result, returns False if the result is true

#The and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not Operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Combining Multiple Operators
#You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#nested if
#nested artinya bersarang
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#How Nested If Works
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#Python Pass Statement
#The pass Statement
a = 33
b = 200

if b > a:
  pass

#pass in Development
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#pass vs Comments
score = 85

if score > 90:
# This is excellent
# This will raise an IndentationError 

#ini bisa erorr karena kode block kosong, tetapi

score = 85 
if score > 90:
  pass # This is excellent
print("Score processed")

#ini jalan

# pass with Multiple Conditions
#You can use pass in any branch of an if-elif-else statement.
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")
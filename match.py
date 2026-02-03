day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

    day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

    month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

    i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  for x in "banana":
  print(x)

  for x in range(6):
  print(x)

  for x in range(2, 6):
  print(x)
  
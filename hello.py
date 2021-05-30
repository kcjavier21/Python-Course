import os

# patient_name = "John Smith"
# patient_age = 20
# patient_isNew = True

os.system('cls')

# print("Name: " + patient_name)
# print("Age: " + str(patient_age))
# print("New Patient: " + str(patient_isNew))


# === STRINGS ====

# course = "Python Programming"
# print("String Length: " + str(len(course)))
# print("0TH index: " + str(course[0]))
# print("Last Index: " + str(course[-1]))
# print("First three characters: " + str(course[0:3]))
# print("First to last characters: " + str(course[0:]))


# === ESCAPE SEQUENCES ===
# Double Quotes - \"   :  Single Quotes = \'
# Slash - \\"   :  New Line = \n

# course = "Python \"Programming\""
# print(course)

# === FORMATTED STRINGS ===
# first = "Ken"
# last = "Javier"
# full = f"{first} {last}"
# print(full)

# === STRING METHODS ===
# course = "  python programming"
# print("Uppercase        : " + str(course.upper()))
# print("Lowercase        : " + str(course.lower()))
# print("Title Form       : " + str(course.title()))
# print("No Whitespace    : " + str(course.strip()))
# print("Find Index       : " + str(course.find("pro")))
# print("Replace          : " + str(course.replace("p","j")))
# print("In String        : " + str("pro" in course))
# print("Not In String    : " + str("swift" not in course))

# === NUMBERS ===
# print("Add              : " + str(10 + 3))
# print("Subtract         : " + str(10 - 3))
# print("Multiply         : " + str(10 * 3))
# print("Divide           : " + str(10 / 3))
# print("Divide in integer: " + str(10 // 3))
# print("Remainder        : " + str(10 % 3))
# print("Exponent         : " + str(10 ** 3))

# import math

# print("Round        : " + str(round(2.9)))
# print("Absolute val : " + str(abs(2.9)))
# print("Ceil         : " + str(math.ceil(2.9)))
# print("Floor        : " + str(math.floor(2.9))

# === TYPE CONVERSION ===

# x = input("x: ")
# y = int(x) + 1
# print(f"X: {x}, y: {y}")



# ==== INPUT DATA =====

# birth_year = input("Enter your birth_year: ")
# age = 2020 - int(birth_year)
# print(age)

# first_number = input("First: ")
# sec_number = input("Second: ")
# sum = int(sec_number) + int(first_number)
# print(sum)

# ==== STRINGS ====
course = 'Python for Beginners'
# print(course.upper())
# print(course.find('y'))
# print(course.replace('for', '4'))
print('Python' in course)

# ==== IF STATEMENTS ====
# temperature = 25

# if temperature > 30:
#     print("It's a hot day!")
#     print("Drink plenty of water!")
# elif temperature > 20:
#     print("It's a nice day!")
# elif temperature > 10:
#     print("It's a bit cold!")
# else:
#     print("It's cold!")


# ==== TERNARY OPERATOR ====
# age = 22
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)


# ==== LOGICAL OPERATORS ====
# high_income = False
# good_credit = True
# student = True

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")


# === CHAINING COMPARISON OPERATORS ====
# age = 22
# if 18 <= age < 65:
#     print("Eligible")





# === EXERCISE ====

# weight = input("Weight: ")
# option = input("(K)g or (L)bs: ")

# if option.upper() == 'K':
#     weight = float(weight) * 2.20462
#     weight = format(weight, '.2f')
#     print("Weight in Lbs:" + str(weight))
# elif option.upper() == 'L':
#     weight = float(weight) / 2.20462
#     weight = format(weight, '.2f')
#     print("Weight in Lbs: " + str(weight))
# else:
#     print("Invalid input!")


# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1


# === LISTS ===

# names = ['Steve', 'Tony', 'Peter', 'Wanda']
# print(names[0]) #Steve
# print(names[-1]) #Wanda
# names[0] = 'Rogers'
# print(names)
# print(names[0:3]) #['Steve', 'Tony', 'Peter']

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)
# numbers.insert(2, 6)
# print(numbers)
# numbers.remove(3)
# print(numbers)

# print(1 in numbers) #True
# print(len(numbers)) #6

# numbers.clear()
# print(numbers)


# === FOR LOOPS ===
# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")

# for number in range(1, 4):
#     print("Attempt", number, (number) * ".")

# for number in range(1, 10, 2):  #params - start, end, steps/skips
#     print("Attempt", number, (number) * ".")


# numbers = [1, 2, 3, 4, 5]

# for item in numbers:
#     print(item)

# === RANGE FUNCTION ===
# numbers = range(5)
# numbers = range(5, 10)
# numbers = range(5, 9, 2)
# print(numbers)

# for number in numbers:
#     print(number)

# ctr = 0
# for num in range(1, 10):
#     if (num%2 == 0):
#         print(str(num) + "\n")
#         ctr = ctr + 1

# print(f"We have {str(ctr)} even numbers")



#=== FUNCTIONS ====

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome Aboard")

# greet("Ken", "Javier")

# === Keyword Arguments ===
# def increment(number, by):
#     return number + by

# print(increment(number=2, by=1))

# === Default Arguments ===
# def increment(number, by=1):
#     return number + by

# print(increment(2))


# ==== *args ====
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
    
#     return total

# print("Start")
# print(multiply(2, 3, 4, 5))


# ==== **args ====
# def save_user(**user):
#     #print(user)
#     print(user["name"])

# save_user(id=1, name="Ken", age="20")


# === Fizz Buzz ===

# def fizz_buzz(input):

#     if (input % 3) == 0 == (input % 5):
#         return "FizzBuzz"
#     elif (input % 3) == 0:
#         return "Fizz"
#     elif (input % 5) == 0:
#         return "Buzz"
#     else:
#         return input

# print(fizz_buzz(30))
import os

# patient_name = "John Smith"
# patient_age = 20
# patient_isNew = True

os.system('cls')

# print("Name: " + patient_name)
# print("Age: " + str(patient_age))
# print("New Patient: " + str(patient_isNew))

# ==== INPUT DATA =====

# birth_year = input("Enter your birth_year: ")
# age = 2020 - int(birth_year)
# print(age)

# first_number = input("First: ")
# sec_number = input("Second: ")
# sum = int(sec_number) + int(first_number)
# print(sum)

# ==== STRINGS ====
# course = 'Python for Beginners'
# print(course.upper())
# print(course.find('y'))
# print(course.replace('for', '4'))
# print('Python' in course)

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
# numbers = [1, 2, 3, 4, 5]

# for item in numbers:
#     print(item)

# === RANGE FUNCTION ===
# numbers = range(5)
# numbers = range(5, 10)
numbers = range(5, 10, 2)
print(numbers)

for number in numbers:
    print(number)
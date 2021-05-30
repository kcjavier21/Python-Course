# === HANDLING EXCEPTIONS ===

# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown.")



# === HANDLING DIFFERENT EXCEPTIONS ===

# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


# ==== CLEANING UP ====

# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()


# === The WITH Statement ===

# try:
#     with open("hello.py") as file:
#         print("File opened.")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")


# === Raising Exceptions ===

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less.")
#     return 10 / age

# try:
#     print(calculate_xfactor(0))
# except ValueError as error:
#     print(error)



# === Cost of Raising Exceptions ===
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less.")
    return 10 / age

try:
    print(calculate_xfactor(0))
except ValueError as error:
    pass
"""


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(0)
if xfactor == None:
    pass
"""


print("First code = ", timeit(code1, number=1000))
print("First code = ", timeit(code2, number=1000))

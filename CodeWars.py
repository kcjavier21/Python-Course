import os
os.system('cls')

# def square(num):
#     numString = str(num)
#     numList = []

#     for number in numString:
#         numList.append(str(int(number) ** 2))
    
#     numList = int(''.join(numList))
#     return numList

# print(square(9119))



# def odd(num):
#     for item in num:
#         time = num.count(item)
#         if time % 2 != 0:
#             return item

# numbers = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
# print(odd(numbers))


# def population(p0, percent, aug, p):
#     count = 0
#     percent = percent * 0.01

#     while p0 < p:
#         p0 = p0 + p0 * percent + aug
#         print(p0)
#         count = count + 1
    
#     if count == 3: 
#         return 4 
#     elif count == 4:
#         return
#     else: 
#         return count

# print(population(1500, 5, 100, 5000))


# def convertToCamelCase(text):
#     textCopy = text.replace("-", " ")
#     print(textCopy)
#     textCopy = textCopy.replace("_", " ")
#     print(textCopy)

#     splitted = textCopy.split()
#     textCopy = ""

#     for i, text in enumerate(splitted):
#         if i > 0:
#             textCopy = textCopy + text.capitalize()
#         else:
#             textCopy = textCopy + text

#     print(str(textCopy))



# convertToCamelCase("the_Cat-is_pippi")

# def digital_root(n):
#     while n >= 10:
#         n_copy = str(n)
#         n_copy = map(int, n_copy)
#         n = 0
        
#         for number in n_copy:
#             n += int(number)

#     return n

# digital_root(942)

# def alphabet_position(text):
#     text_copy = list(text.lower().replace(" ", ""))
#     num = []

#     for letter in text_copy:
#         if ((ord(letter) - 96) > 0):
#             num.append(str(ord(letter) - 96))
            
#     num = (" ".join(num))
#     print(num)


# alphabet_position("The sunset sets at twelve o' clock.")





    

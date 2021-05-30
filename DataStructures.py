import os
os.system('cls')

# === LISTS ===

# letters = ["a", "b", "c", "d"]
# matrix = [[0, 1], [2,3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(5, 20))
# chars = list("Hello World")
# print(chars)

# === Accessing Items ===

# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters)
# print(letters[0])   #--> First character
# print(letters[0:3]) #--> First three
# print(letters[::2]) #--> With Skip

# numbers = list(range(0,20))
# print(numbers[::-1]) # --> Reversed Order


# === List Unpacking ===
# numbers = [1, 2, 3, 4, 5]
# #first, second, third = numbers
# #first, second, *other = numbers
# first, *other, last = numbers
# print(first)
# print(other)
# print(last)


# === Looping over loops ===
# letters = ["a", "b", "c"]

# for letter in letters:
#     print(letter)

# for letter in enumerate(letters): # --> Tupple
#     print(letter)

# === Add and Remove Items ===
# letters = ["a", "b", "c"]

# #Add
# letters.append("d")
# letters.insert(0, "-")
# print(letters)

# #Remove
# #letters.pop()
# #letters.pop(0)
# #letters.remove("b") #--> First b only
# del letters[0:3] # --> First three letters
# letters.clear() # --> Clear the list
# print(letters)


# === Find Item ==
# letters = ["a", "b", "c"]

# print(letters.index("c"))
# if "d" in letters:
#     print(letters.index("d"))


# === Sorting List ===
# numbers = [3, 51, 2, 8, 6]
#numbers.sort()
#numbers.sort(reverse=True)
# print(sorted(numbers)) #--> Does not modify the original list
# print(numbers)

#Sort Tupples
# items = [
#     ("Product 1", 10),
#     ("Product 2", 9),
#     ("Product 3", 12)
# ]

# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
# print(items)



# === Lambda Function ===
items = [
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

# items.sort(key=lambda item: item[1])
# print(items)

# === Map Function ===
# prices = list(map(lambda item: item[1], items))
# print(prices)

# === Filter Function ===
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)

# === List Comprehension ===
# prices = [item[1] for item in items]
# print(prices)

# filtered = [item for item in items if item[1] >= 10]
# print(filtered)


# === Zip Function ===
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))





# ==== STACKS ====



# ==== QUEUE =====
# from collections import deque

# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)

# if not queue:
#     print("Empty")
    

# ==== TUPLES ====


# ==== ARRAYS ====
# from array import array

# numbers = array("i", [1, 2, 3])
# numbers.append(4)
# numbers.insert(0, 0)
# print(numbers)


# === Sets ===
# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print("yes")


# === DICTIONARIES ====

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20

# if "a" in point:
#     print(point["a"])

# print(point.get("a"))

# del point["x"]
# print(point)

# for key, value in point.items():
#     print(key, value)



# === Dictionary Comprehension ====

# values = {x * 2 for x in range(5)}
# print(values)


# === Generator Comprehension ===
# values = {x * 2 for x in range(5)}
# print(values) 


# === Unpacking Operator ===

# numbers = [1, 2, 3]
# print(*numbers)

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]

# first = {"x": 1}
# second = {"x": 10, "y": 2}
# combined = { **first, **second, "z": 1 }
# print(combined)


# ==== Exercise ===

# sentence = "This is a common inteview question"
# highest = 0

# for item in sentence:
#     time = sentence.count(item)
    
#     if time > highest:
#         highest = time
#         highestChar = item
        

# print(highest, highestChar)









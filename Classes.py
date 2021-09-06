import os
os.system('cls')

# ==== Creating Custom Class ====

# class Point:
#      def draw(self):
#          print("draw")

# point = Point()
# print("Type of Point:   " + str(type(point)))
# print("Is Instance?     " + str(isinstance(point, int)))



# ==== Constructors =====
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point(1, 2)
# point.draw()


# ==== Class vs Instance Attributes ===

# Class Attributes - are shared by all instances of the class.
# Instance attributes - belong to specific instances only.

# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# Point.default_color = "blue"

# point = Point(1, 2)
# print(point.default_color)
# point.draw()


# point = Point(3, 4)
# print(point.default_color)
# point.draw()




# ==== Class vs Instance Methods ===

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)


#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point.zero()
# point.draw()



# ==== Magic Methods ===

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# point = Point.zero()
# print(point)


# ==== Comparing Objects ===

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(3, 3)
# other = Point(1, 2)
# print(point > other)


# ==== Performing Arithmetic Operations ===
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(3, 3)
# other = Point(1, 2)
# combined = point + other
# print(combined.x)



# ==== Making Custom Containers ====
# class TagCloud:
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)

# cloud = TagCloud()
# print(cloud._TagCloud__tags)

# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("JavaScript")
# #print(cloud.tags)
# print(cloud["python"])


# ==== Properties ===

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     # price = property(get_price, set_price)

# product = Product(10)
# print(product.price)


# ==== INHERITANCE ====


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

    
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)
    



















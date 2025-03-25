# class person:

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def __del__(self):
#         print("object is being deconstructed.")

# persondetails = person(name="nipun", age=30)
# print(f"Name: {persondetails.name}, Age: {persondetails.age}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name

x = Person('Mike', 25)
y = Person('Sarah', 27)
z = Person('Mike', 28)

print(x==z)



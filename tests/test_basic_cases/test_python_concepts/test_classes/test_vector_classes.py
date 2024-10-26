class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    def __repr__(self):
        return f"X: {self.x} and Y: {self.y}"

    def __len__(self):
        return 100

    def __call__(self):
        print("Hello I'm the Object that is being called")


v1  = Vector(10, 20)
v2 =  Vector(20, 30)

v3 = v1 + v2
print(f"Value of v3.x is {v3.x} and v3.y is {v3.y}")
print(v3)
print(len(v3))

v3()
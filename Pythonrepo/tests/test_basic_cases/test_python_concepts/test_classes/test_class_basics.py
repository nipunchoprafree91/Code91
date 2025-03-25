import pytest

class TestA:
    """
    My class A
    """

    def __init__(self):
        self.A1: str = "A1"


        """
        My class A constructor
        """
        print("A class Constructor")


    def test_methA(self):
        """
        My method A
        """

        print("A class Method.")

class TestB:
    """
    My class B
    """
    def __init__(self):
        self.B1: str = "B1"

    def test_methA(self):
        """
        My method B
        """

        print("B class Method.")

class TestClass():
    pass

my_test_class = TestClass()
print(my_test_class)
print(type(TestClass))
print(type(type))

Testclass = type('Testclass', (), {"typeof": "dynamic", "isautomated": True})
print(Testclass)
print(Testclass().typeof)
print(Testclass().isautomated)
#same as type
print(Testclass().isautomated.__class__)
print(type(Testclass().isautomated))
print(type(str))
print(type(list),type(float), type(dict), type(tuple))
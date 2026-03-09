import numpy as np
a = 100
b = 2
d = 3
list1 = [1, 2, 3, 4, 5]
if 1 not in list1:
    print("1 is not in the list")
d = ~a
print(a)
print(d)
list1 = sorted(list1)
list1.sort()
list1.reverse()
list2 = list(reversed(list1))
k = len(list1)
my_set = set()
c = False
string = "Hello, World!"
len1 = len(string)
if "hello" in string.lower():
    print("The string contains 'hello'")
if string.startswith("Hello"):
    print("The string starts with 'Hello'")
else:
    print("The string does not start with 'Hello'")
if string.endswith("!"):print("The string ends with '!'")
else:print("The string does not end with '!'")
if not True == True:
    print("hello")
if True or False and False:
    print("This will always print")
if a == 1:
    pass
for i ,j in zip(list1,list1):
    print(i,j)
print(",".split("hello"))
print("%d" % a)
print()
print("this is a test".find("a test"))
print(str(a))
print(repr(a))
print(np.ones((4,3)))
print(np.zeros((2,5)))
# while True:
#     if not a:
#         break
#     print(a)
x = 0
print(print("hello") is None)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    name = "Alice"
    age = 30
alice = Person("Alice", 30)
i = isinstance(alice, Person)
alice.name = "Bob"
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def work(self):
        return f"{self.name} is working with employee ID {self.employee_id}."
    def _private_method(self):
        return "This is a private method."
class MyClass:
    a = 1
    b = 2
instance = MyClass()
print(instance.__dir__())
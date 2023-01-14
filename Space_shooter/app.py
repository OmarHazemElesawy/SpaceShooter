print("hello")
print('#'*10)  # expression
# name=input('what is your name?') # string from user
# print('hi'+ name)
# birth_year=input('year of birth: ')
# age = 2020-int(birth_year)
# print(age)
email = """ 
hi omar,
good morning.
how is life
yours,
foo
"""
print(email)
test = "Omar Hazem"
another = test[:]
print(test[0])
print(test[-1])  # last
print(test[0:3])  # 0 included 3 is not
print(test[1:])  # exclude first char
print(another)
#####################
first = "omar"
last = "hazem"
name = first+" "+last
print(name.upper())
print(name.find("h"))
print(name)
print("omar" in name)
print(name.title())
message = first+" ["+last+"] is a coder"
msg = f"{first} [{last}] is a coder"
print(message)
print(msg)
print("*"*20)
####################
is_hot = False
is_cold = True
if is_hot:
    print("it is hot")
elif is_cold:
    print("it is cold")
else:
    print("it is a lovely day")
print("bye")
print("-"*20)
has_high_income = True
has_good_credit = True
if has_good_credit and has_good_credit:
    print("good to go")
if has_good_credit or has_good_credit:
    print("maybe")
print("-"*20)
# secret = 9
# i = 0
# while i < 3:
#     guess = int(input("Guess: "))
#     if guess == secret:
#         print("you won!")
#         break
# else:
#     print("you lost")
list1 = [1, 2, 3]
x, y, z = list1  # unpacking
print(f"({x}, {y}, {z})")
print("-"*20)
customer = {"name": "omar", "age": 30, "male": True}
print(customer["name"])
print(customer.get("birthdate"))  # none
print(customer.get("birthdate", 1990))  # default value 1990
customer["birthdate"] = "apr 22 2000"
# get_sth = float(input("the king of the north"))
# print(get_sth*2)


class Person:
    def __init__(self, name_person):
        self.name_person = name_person

    def talk(self):
        print(f"hi , I am {self.name_person}")


print("-"*20)
for items in "python":
    print(items)
print("-"*20)
# list comprehension
names = ["omar", "toa", "noha"]
print(names)
persons = [person for person in names]
print(persons)
numbers = [1, 2, 3, 4]
print(numbers)
new_numbers = [2*num for num in numbers]
print(new_numbers)

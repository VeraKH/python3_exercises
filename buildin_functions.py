# BUILD-IN FUNCTIONS
name = input('Input your name:')
print(name.capitalize())
print(dir(name))

# EXPRESSIONS - result of it is value of one type
# examples
# 5 + 3 = 8 Sum of vars
# a < b True or False
# 'Hello'+'World' Hello World
# my_func(10,5) Call of function is also expression. Result of Function is new value

print(10 + 5)
print(print(10 + 5))  # Func print return None

input('Input your name:')
print(input('Input your name:'))

# NO functions or no instruction in expressions
# print(If True:print(10)
# print(def my_fn():
#     print(Vera)


# STATEMENTS -  call the action

# 1
my_name = 'Vera'  # Присвоение значения
# 2
if my_name:
    print('Yes')
# 3
import datetime  # Module import

print(datetime.MAXYEAR)


def my_name():
    a = 5 + 5
    # print(return a)
    return 5 + 5


# DYNAMIC TYPISATION in PYTHON

def print_name(name):
    print(name)


print_name('Vera')
print_name = 15  # CHANGE VALUE FOR print_name

# print_name('Vera') ERROR
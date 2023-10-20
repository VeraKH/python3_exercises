# if, if...else, if..elif

# false: all empty,
# int 0, float 0.0, complex 0j.
# bool False, NoneType None

# to check if it is false: bool(value)

# TRUE - values that are not FALSE

print('1. if')

my_number = 25
if my_number > 0:
    print(my_number, 'is positive')

print('2. if not')

person = {'age': 20}

if not person.get('name'):
    print('No name')

num_1 = 10
num_2 = 5.3

if (num_1 > 0 and
        num_2 > 0 and
        isinstance(num_1, int) and
        isinstance(num_2, int)):
    print('Both numbers are ints and positive')
print('something wrong')

print('3. if else')

my_number_1 = 21.5

if type(my_number_1) is int:
    print(f"{my_number_1} is int")
else:
    print(f"{my_number_1} is not int")

my_phone = {'color': 'black'}

if my_phone.get('brand'):
    print(f"My phone is {my_phone['brand']}")
else:
    print('There is no brand info')

print('4. if Elif')

my_number_2 = 'fsdsd'

if type(my_number_2) is int:
    print(f"{my_number_2} is int")
elif type(my_number_2) is bool:
    print(f"{my_number_2} is bool")
else:
    print(f"{my_number_2} is Not bool and not int")

# if type(my_number_2) is int:
#     print(f"{my_number_2} is int")
# if type(my_number_2) is bool:
#     print(f"{my_number_2} is bool")
# if:
#     print(f"{my_number_2} is Not bool and not int")

print("5. ternary operator")

product_qty = 10
print("in stock" if product_qty > 0 else "out of stock")


temp = 24
weather = "hot" if product_qty > 0 else "cold"
print(weather)

my_image = ('1920', '1080', True)
print(f"{my_image[0]}x{my_image[1]}") if \
    len(my_image) == 2 else print('Incorrect image formated')

my_image_2 = ('1920', '1080')
message = f"{my_image_2[0]}x{my_image_2[1]}" if \
    len(my_image_2) == 2 else 'Incorrect image formated'
print(message)

print('6. if in function')


def nums(a, b):
    if (type(a) is not int) or (type(b) is not int):
        return 'Один из аргументом не целое число'
    if a >= b:
        return f"{a} больше или равно {b}"
    return f"{a} меньше {b}"


print(nums(5, 1))
print(nums(True, 10))

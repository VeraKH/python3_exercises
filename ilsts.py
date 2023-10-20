print('ANY types of elements in list')
user_inputs = [True, 'hi', 10, 5]
print(1, user_inputs)

print('ORDER of elements matters')
my_fruits_1 = ['apple', 'banana', 'pear']
my_fruits_2 = ['apple', 'pear', 'banana']
print(my_fruits_1 == my_fruits_2)

print('LENGTH of elements')
print(2, len(my_fruits_1))  # 3

print('GET element by id')
print(3, my_fruits_2[1])

print('CHANGE element by index')
my_fruits_2[1] = 'mango'
print(4, my_fruits_2)

print('DELETE element by index')
del my_fruits_2[0]
print(5, my_fruits_2, len(my_fruits_2))

print('List of dictionaries')
users = [
    {
        'user_id': 123,
        'user_name': 'Vera'
    },
    {
        'user_id': 321,
        'user_name': 'Dima'
    }
]

print(1, users, len(users))
print(users[1]['user_id'])  # 321

print('METHODS for lists')
# POP and APPEND change the list, not create new one

users = []

print('APPEND')
users.append('Vera')
users.append('Dima')
users.append('Lev')
print(1, users, len(users))

print('POP')
users.pop()
print(2, users, len(users))
removed_element = users.pop(0)
print(3, users, len(users))
print(4, removed_element)

print('SORT')
numbers = [3, 7, 99, 199, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print('CONVERT TO LIST')
greeting = 'Hello world'
greeting_letters = list(greeting)
print(1, greeting_letters)

user = {
    'user_id': 123,
    'user_name': 'Vera'
}

user_dic_to_list = list(user)
print(2, 'Keys only goes to list: ', user_dic_to_list)

print('ARIFMETICS in LISTS')

rating = [2.5, 5.0, 4.3, 3.7, 4, 5]
print('MIN: ', min(rating))
print('MAX: ', max(rating))
print('SUM: ', sum(rating))
print('AVARAGE: ', sum(rating) / len(rating))

print('SUM of lists')

all_fruits = [my_fruits_1, my_fruits_2]
print(1, all_fruits)

print('MAGIC method ___add__ doesn\'t change original lists, creates new one')
all_fruits = my_fruits_1 + my_fruits_2
print(2, all_fruits)

print('CUT THE LISTS')
first_two_ratings = rating[:2]  # Not include 2
print(1, first_two_ratings)
first_two_ratings = rating[1:-1]  # Not include -1
print(2, first_two_ratings)
first_two_ratings = rating[-2]
print(3, first_two_ratings)

print('1. COPY THE LIST BY LINK')

my_cars = ['BMV', 'Mercedes']
copied_cars = my_cars  # they link to one object!
copied_cars.append('Audi')
print('they link to one object: ', id(copied_cars) == id(my_cars))

print('2. COPY THE LIST by SLICE')
copied_cars = my_cars[:]  # they link to one object! copy by slice
copied_cars.append('Audi')
print('two different lists: ', id(copied_cars) == id(my_cars))

print('3. COPY THE LIST by COPY')
copied_cars = my_cars.copy()  # they link to one object! copy by slice
copied_cars.append('Lada')
print('two different lists: ', id(copied_cars) == id(my_cars), copied_cars, my_cars)

print('4. COPY THE LIST by LIST')
copied_cars = list(my_cars)  # they link to one object! copy by list
copied_cars.append('Toyota')
print('two different lists: ', id(copied_cars) == id(my_cars), copied_cars, my_cars)

print('5. COUNT')
my_nums = [10, 50, 0, 5, 5, 100]
print(my_nums.count(5))
my_nums.insert(2, -10)  # BEFORE this index
print(my_nums)

print('6. CLEAR')
my_nums.clear()
print(my_nums)

print('7. EXTEND')
my_nums = [10, 50, 0, 5, 5, 100]
my_nums.extend('abc')
print(my_nums)

print('8. Unpacking')

my_fruits_3 = ['apple', 'banana', 'pear']

my_apple, my_banana, my_pear = my_fruits_3

my_apple_1, *remaining_fruits = my_fruits_3

print(my_apple, my_banana, my_pear)
print(my_apple_1)  # string
print(remaining_fruits)  # list

print('4. Unpacking to function')

#user_data = ['Vera', '']
user_data = ['Vera', 35]


def user_info(name, age):
    if not age:
        return f"{name} has no age"
    return f"{name} is {age}"


print(user_info(*user_data))
#print(user_info(name=user_data[0], age=user_data[1]))
#print(user_info(user_data[0], user_data[1]))
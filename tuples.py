my_fruits = ('apple', 'lemon', 'banana', 'lime', 'lemon')
my_fruits_2 = ('banana', 'apple', 'lime')

print('1. ORDER matters: ', my_fruits == my_fruits_2)

print('2.1 GET element by index: ', my_fruits[1])
print('2.2 GET element by index: ', my_fruits[-1])

users = (
    {
        'user_id': 123,
        'user_name': 'Vera'
    },
    {
        'user_id': 321,
        'user_name': 'Dima'
    }
)

my_user = {
        'user_id': 321,
        'user_name': 'Dima',
}

print('3.1 DICTIONARY in tuple: ', users, len(users))

print('3.2 DICTIONARY in tuple: ', users[1]['user_id']) #321

users[1]['user_id'] = 100
print('3.2 DICTIONARY in tuple - can change dict element: ', users[1]['user_id']) #100

fruit_1 = 'apple'
fruit_2 = 'banana'
fruit_3 = 'lime'

fruit_tuple = (fruit_1, fruit_2, fruit_3)
print('4. VARS as elements in tuple: ', fruit_tuple)

#print('5. INDEXT does not exist: ', my_fruits[6]) #tuple index out of range

all_fruits = my_fruits + my_fruits_2
print('5. COMBINE tuple: ', all_fruits)

#my_fruits[-1]='limon'
#del my_fruits[1]
#print('3.1 Can not change: ', my_fruits) #error
#print('3.2 Can not change: ', my_fruits) #error

print('6. COUNT: ', all_fruits.count('lime'))

print('7. INDEX: ', all_fruits.index('apple'))

num_tuple = (2, 4, 7, 8, 7, 2)
num_list = list(num_tuple)
new_list = [3, 7]
num_list = num_list + new_list
num_tuple = tuple(num_list)

print('8. CONVERT to LIST and BACK: ', num_tuple)

print('9. CONVERT DICT to TUPLE: ', tuple(my_user))


print('10. Unpacking')

my_fruits_3 = ('banana', 'apple', 'lime')

my_apple, my_banana, my_pear = my_fruits_3

print(my_apple, my_banana, my_pear)

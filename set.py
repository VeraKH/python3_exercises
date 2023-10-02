# set is unsorted que of unique elements, changeable, often of one type

my_fruits = {'apple', 'lemon', 'banana', 'lime', 'lemon'}
my_fruits_2 = {'apple', 'banana', 'lime', 'lemon', 'lemon'}
my_numbers = {151, 245, 762, 167, 151, 167}
my_numbers_list = [151, 245, 762, 167, 151, 167]
my_inputs = {True, 'Vera', 10.5}  # usually not do like this

print('1. TYPE', type(my_fruits), my_fruits)
print('2. UNIQUE ELEMENTS ONLY: ', my_numbers)
print('3. ORDER DOES NOT MATTERS: ', my_fruits == my_fruits_2)
print('4. LEN', len(my_fruits), my_fruits)
print('5. ORDER DOES NOT MATTERS: ', my_fruits == my_fruits_2)
print('6. GET ITEM magic method is to get element by index. Sets do not have this method. THIS is for LIST:',
      my_numbers_list[0] == my_numbers_list.__getitem__(0))


print('7. DOES NOT HAVE INDEXES')
# my_fruits[0] #ERROR
print('8. CAN NOT CHANGE ELEMENTS, so can not put lists, dicts to the sets')
# my_fruits{[1, 2], [3,4]}) #ERROR
print('9. CAN NOT USE DEL method')
# del my_fruits[0] #ERROR

print('10. CAN NOT USE DEL method')

print('11. CREATE EMPTY SET:', set())

new_set_1 = {'Hello', 'world'}
new_set_2 = {'Mars', 'Moon', 'world', 'hello', 'Hello'}
new_set_1.add('and all')
print('12. ADD NEW ELEMENT:', new_set_1)
# all_sets = new_set_1.union(new_set_2)
all_sets = new_set_1 | new_set_2
print('13. UNION SETS:', all_sets)

print('14.1 INTERSECTION IN UNIONS:', new_set_1.intersection(new_set_2))
print('14.2 INTERSECTION IN UNIONS:', new_set_1 & new_set_2)

num_1 = {10, 5, 35}
num_2 = {20, 5, 12, 10, 35}
result = num_1.issubset(num_2)

print('15. SUBSET IN UNIONS:', result)
result_2 = num_2.issuperset(num_1)
print('16. SUPERSET IN UNIONS: - ', result_2)

string_set_1 = {'abc', 'd', 'f', 'y'}
string_set_2 = {'a', 'f', 'd'}
string_set_3 = {'abcd'}  # the same as {'a','b','c'}
print('17.1 intersection of ANY SEQUENCE:', string_set_2.intersection(string_set_1))
print('17.2 intersection of ANY SEQUENCE - list, string, tuple:', string_set_1.intersection('abcd'), string_set_1.intersection(['a','b','c', 'd']))
print('17.3 intersection of ANY SEQUENCE - HERE IS SOMETHING I DO NOT UNDERSTAND:', string_set_1.intersection(string_set_3))

print('18 DIFFERENCE:', string_set_2.difference(string_set_1), string_set_3 - string_set_2)

string_set_1.discard('d')
print('19.1 DISCARD:', string_set_1)

string_set_1.discard('w')
print('19.2 DISCARD of not existent element:', string_set_1)

string_set_1.remove('abc')
print('20. REMOVE element:', string_set_1)

# string_set_1.remove('w')
# print('20. REMOVE of not existent element:', string_set_1) #ERRROR

print('21. COPY set')

copied_set = new_set_1.copy()
print(copied_set)
copied_set.add('z')
new_set_1.add('l')
print(copied_set - new_set_1)

print('21. SYMMETRIC DIFFERENCE - объединение минус пересечение')
print(new_set_1.symmetric_difference(copied_set))
print((new_set_1 | copied_set) - (new_set_1 & copied_set))

a = 10 #a and 10 - operands. = operator

#operators: arifmetics, compare, logical
# assignment operator (=), sum  operator (+), match operator(is)

b = [1, 2] # lists are changeble objects
c = [1, 2]

print(b == c) #True
print(b.__eq__(c)) #True

print('1. Convert to number')

my_num = 10
print(+my_num)
my_bool = True
print(+my_bool)

print('2. Negation of value')

my_num_1 = 1
print(not my_num_1)
my_num_2 = 0
print(not my_num_2)

print('3.Binary operators')
#a = 5 assignment
#a + b arifmetic
#a +=5 increment
#a == b comparison
#a and b


print('4.In, Not, In')

my_car = {
    'brand': 'Toyota',
    'price': 10000
}

print('brand' in my_car) #True
print('year' in my_car) #False
print('year' not in my_car) #True


print('5. Priority in operators')

aa = 1
bb = 2
cc = 3
dd = 2
ee = 1

f = aa + ((bb * cc) / (dd - ee))
print(f)


print('Task')

new_set_1 = {'Hello', 'world'}
new_set_2 = {'Hello', 'world'}

print(new_set_1 == new_set_2)
print(new_set_1 is new_set_2) #Python Identity Operators

print(dir(new_set_1))


print('6. Falsy values')

print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(None))

my_dic = {}
my_list = []
my_tuple = ()
my_set = set()
my_range = range(0)
my_str = ""
print(bool(my_str), not not(my_tuple), bool(my_set), bool(my_dic), bool(my_list), bool(my_range))

my_list_2 = [1,2]
print(not my_list_2)
print(not not my_list_2)

my_list_2 = [1, 2]
print(len(my_list_2) > 0)

if len(my_list_2) > 0:
    print('Yes')

if my_list_2:
    print('Yes-2 ')


print('7. Logical operators - not') #not

#not 10 False - if we deny true, we get false
#not 0 True
#not 'abc' False
#not '' True
#not True False
#not None True


#not not 10 True - if we deny true, we get false
#not not 0 False
#not not 'abc' True
#not not '' False
#not not True True
#not not None False

print('8. Logical operators - and')

# Выражение 1 and Выражение 2 - если выражение 1 ложно, то выражение 2 игнорируется. Возвращается 1
# истинно, если оба истины, ложны, если оба ложны. Если хотя бы одно ложно, то все ложно.

# a and b and c and d


print('9. Logical operators - or')

# Выражение 1 and Выражение 2 Если выражение 1 истино, то все истино. Если 1 ложно, то идем дальше смотреть.
# Результат 2 какой будет, такое и все выражение. Если оба ложны, то все будет ложно.
# Если 1 истино, то все истино.
# a or b or c or d - как только найдет правдивое, то остановится и отдаст это значение

my_list_3 = [1, 2]
other_list = [3, 4]
my_dic_2 = {}
print(not not my_list_3) #True

print(my_list_3 or other_list) #1,2
print(len(my_list_3) > 0 or other_list) # True
print(len(my_list_3) < 0 or other_list) # [3, 4]
print(my_list_3 and my_dic_2)

my_dic_3 = {1, 3}
my_dic_4 = {1, 2}

if my_dic_3 == my_dic_3:
    print('Dictionaries are equal')





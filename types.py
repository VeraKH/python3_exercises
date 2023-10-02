print('\nTYPES TOPIC') #STRINGS

#TYPES in PYTHON - all vars in python are objects
#There are mutable (int, string, boolean, float, tuple,NoneType, Range) and immutable objects (list, dict, set, user classes)

#VARUABLE - is link to the object
my_count = 12
print(id(my_count)) #4342194792

#There can be situation when different vars links to one objectn

my_number = 10
print(id(my_number)) #4384055848 every time there gonna be new ID. New run = new object
other_number = my_number
print(id(other_number)) #4384055848

print('\nSTRINGS TOPIC') #STRINGS

long_str = 'This is a short string'
print(type(long_str))
print(id(long_str))

long_str_other = '''This is 
                    a 
                    short string'''
print(long_str_other)
print(len(long_str))
print(long_str .replace('short', 'long'))
print(long_str.count(' '))
print(long_str.count( 's'))
print(long_str.count('is'))
print(long_str[-1])
print(long_str[2:7])


print('\nINTEGERS TOPIC')
#INT
num = 1_000_000
print(type(num), num)
input_var = input('Enter any number: ')
print(input_var)
print(type(input_var))
str_to_int = int(input_var)
print(type(str_to_int))
new_int = int(input('Enter any number: '))
print(type(new_int), new_int)

base = 3
power = 3
print(pow(base, power))



print('\nFLOAT TOPIC')

average_price = 17.25
print(round(average_price))
average_price_int = int(average_price)
print(average_price_int)
average_price_string = '17.23'
average_price_string_to_float = float(average_price_string)
print(type(average_price_string_to_float),average_price_string_to_float)


print('\nCOMPLEX')
complex_a = 10 +3j
complex_b = 5 +5j

print(complex_a+complex_b) #(15+8j)
print(complex_a-complex_b) #(5+-2j)


print('\nBOOL TOPIC')

print(100 >5)
print(-5 > 2)
print('Long string' > 'Long')
print([1, 2, 3] == [1, 2, 3])

db_is_available = True
print(db_is_available)
print(type(db_is_available))
db_is_available = False
print(db_is_available)

print('\nConvert to BOOL task')
print(1, bool(base))
print(2, bool(10))
print(3, bool('abc'))
print(4, bool([]))
print(5, [] == [])
print(6, {'a': 3} == {'a': 5})
print(7, bool(True))
print(8, bool(None))
print(9, bool([1, 2]))


print('\nCONVERT TYPES TOPIC')

# '10' + 5 #ERROR
# 10 + '5' #ERROR
print(1, 10 + int('5'))  #15

print(2, 10 + 10.5) #15
print(3, True + 7)  #8

print(4, 10.5 + 10) #15
print(5, 7 + True)  #8

print(6, 10.5.__radd__(10)) #Magical methods for floats

print('\nMAGICAL METHODS') #are internal classes methods

float_num = 50.7
int_num = 7
str = 'abc'

print(1, float_num.__mul__(int_num)) #354.90000000000003 NotImplemented
print(2, int_num.__mul__(float_num)) #NotImplemented
print(3, str * int_num) #7 times of str
print(4, str.__rmul__(int_num)) #7 times of str
print(5, int_num.__rmul__(str)) #NotImplemented

print(dir(bool))
print(help(list.__eq__))


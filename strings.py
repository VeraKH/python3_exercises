print('\nSTRINGS TOPIC')  # STRINGS

long_str = 'This is a short string'
print(type(long_str))
print(id(long_str))

long_str_other = '''This is 
                    a 
                    short string'''
print(long_str_other)
print(len(long_str))
print(long_str.replace('short', 'long'))
print(long_str.count(' '))
print(long_str.count('s'))
print(long_str.count('is'))
print(long_str[-1])
print(long_str[2:7])

print('2. Concatanation with +')

# Concatanation +

a = 'Hello'
b = 'Python'
c = a + ' ' + b
print(c)
print('Hello' + ' Python')

print('3. F-strings')

greet = f"{a} {b}"
print(greet)

print('3. Practics +')

my_name = 'vera'
my_hobby = 'travel'
time = 8

info = my_name + ' likes to ' + my_hobby + ' ' + str(time)
print(info)

info_2 = f"{my_name} likes to {my_hobby} {time} to {' '.join(['Moscow', 'Tomsk'])}".title()
print(info_2)


#info_2_list = info_2.split(' ')
#info_2_list = [i.title() for i in info_2_list]
#print(' '.join(info_2_list))






print('TASK 1')

def route_info(my_dict):
    if my_dict.get('distance'):
        return f"Distance is {my_dict['distance']}"
    if my_dict.get('speed') and my_dict.get('time'):
        return f"Distance is {my_dict['speed']*my_dict['time']}"
    else:
        return f"No info about distance"


my_dict_1 = {'route': 100}
my_dict_2 = {'route': 100, 'distance': 200}
my_dict_3 = {'speed': 80, 'time': 2}


print(route_info(my_dict_1))
print(route_info(my_dict_2))
print(route_info(my_dict_3))

print('TASK 2')

my_image_2 = ('1920', '1080')

if len(my_image_2) == 2:
    print(f"{my_image_2[0]}x{my_image_2[1]}")
else:
    print('Incorrect image formated')


print('TASK 3')
my_string = 'ekfhskjdfhksdjhflsdhfls'

print(f"{my_string} is long") if len(my_string) > 70 else print('The string is short')
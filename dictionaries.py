my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}
print('1. How to create dict: ', my_motorbike)

# nested dictionary
my_motorbike_2 = {
    'price_info': {
        'is_available': True,
        'price': 25000,
    },
    'engine_vol': 1.2,
    'brand': 'Ducati'
}

my_motorbike_3 = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati',
    'color': 'red'
}

print('2. COMPARE dictionaries: ', my_motorbike == my_motorbike_2)

print('3. COMPARE dictionaries: ', my_motorbike == my_motorbike_3)

print('4. GET VALUE of the key: ', my_motorbike['brand'])

print('5. GET ATTRIBUTES of dict: ', dir(my_motorbike))

my_motorbike['brand'] = 'Honda'

print('6. CHANGE VALUE for the key: ', my_motorbike['brand'])

my_motorbike['is_new'] = True
print('7. ADD NEW KEY-VALUE: ', my_motorbike)

del my_motorbike['engine_vol']

print('8. DELETE A KEY-VALUE: ', my_motorbike)

year = 2020
brand = 'Ducati'
color = 'red'
price = 2500

my_motorbike[year] = 2020
print('9. GET VALUE OF THE KEY USING a vars: ', my_motorbike)

print('10. GET VALUE OF THE KEY in NESTED dict: ', my_motorbike_2['price_info']['price'])


def motobike_speed():
    speed = 20 + 20
    return speed


my_motorbike_3 = {
    'price': price,
    'brand': brand,
    'color': color,
    'speed': motobike_speed()
}

print('11. Vars and defs as values for the keys: ', my_motorbike_3)

print('12. LEN of dicts - how many pairs key-value ', len(my_motorbike_3))

# print('13. GET value for not existed key: ', my_motorbike_3['model'])

print('14. GET value without errors if key is not existed: ', my_motorbike_3.get('model'))

print('15. GET value and set error if key is not existed: ', my_motorbike_3.get('model', 'Not excisted'))

my_dict = {}
print(my_dict.__doc__)

print('16. Output dict in the view of tuple: ', my_motorbike_3.items(), 'type: ', type(my_motorbike_3))

print('17. convert to list: ', 'type: ', type(list(my_motorbike_3.keys())))

print('17. convert list to dict:')

my_list = [0, True, 'abc']
my_string = 'Hello world'
# list_to_dic = dict(my_string) #ERRORS
# list_to_dic = dict(my_list) #ERRORS
my_list_2 = [('1', 0), ['2', True], ['3', 'abc']]
my_list_to_dic = dict(my_list_2)
print('17.1 CONVERT LIST or TUPLE TO DICT', my_list_to_dic)

print('18. Pop last key-value - NOT GOOD FOR USAGE: ', my_motorbike_3.popitem())
print(my_motorbike_3)

my_motorbike_4 = my_motorbike_3.copy()
my_motorbike_4['size'] = 'large'
print(my_motorbike_3, my_motorbike_4)
print('19. COPY dictionary', id(my_motorbike_3), id(my_motorbike_4))

print('19. Pop last key-value - NOT GOOD FOR USAGE: ', my_motorbike_3.popitem())

print('20. Unpack dictionary')

button = {
    'width': 200,
    'text': 'red',
    # 'color': 'green'
}

red_button = {
    **button,
    'color': 'red'
    # **button,
}

print(button)
print(red_button)

print('20. Combine dictionaries')

button_info = {
    'type': 'save'
}

my_button = {
    **button_info,
    **button,
}

# my_button_2 = button_info | button


print(my_button)
# print(my_button_2 )


print('21. Unpacking dictionary in function')

user_profile = {
    'user_name': 'Vera',
    'comments_qty': 23,
}


def user_info(user_name, comments_qty=0):
    if not comments_qty:
        return f"{user_name} has no comments"
    return f"{user_name} has {comments_qty} comments"


dct = user_info(**user_profile)  # Call the function with unpacked dictionary
print(dct)

# print('1', user_info(user_profile))
# print('2', user_info(user_profile['user_name'], user_profile['comments_qty']))
# print('3', user_info(user_name=user_profile['user_name'],
#                       comments_gty=user_profile['comments_qty']))
#
# name, comments_qty = user_profile
# print('4', name)
# print('5', comments_qty)§

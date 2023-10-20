my_dict_list = [
    {
        'user_id': 123,
        'user_name': 'Vera'
    },

    {
        'user_id': 321,
        'user_name': 'Dima'
    },

    {
        'user_id': 567,
        'user_name': 'Lev'
    }

]

user_1, user_2, user_3 = my_dict_list
print('User 1: ', user_1)
print('User 2: ', user_2)
print('User 3: ', user_3)


def unpack_dict(user_id, user_name):
    return f"This is user {user_name} with id {user_id}"


print(unpack_dict(**user_1))
print(unpack_dict(**user_2))
print(unpack_dict(**user_3))

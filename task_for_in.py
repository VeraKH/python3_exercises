def dic_to_list(my_dict):
    list_of_tuples = []
    for item in my_dict.items():
        list_of_tuples.append(item)
    return list_of_tuples


my_dict_1 = {
    'id': '1234',
    'color': 'red',
    'model': 'BMV'
}

print(dic_to_list(my_dict_1))

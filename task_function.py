print('1. First task')


def merge_lists_to_dict(list_1, list_2):
    list_1 = list_1.copy()
    list_2 = list_2.copy()
    merged_list = zip(list_1, list_2)
    converted_to_dict = dict(merged_list)
    return converted_to_dict


list_a = [0, 1, 2, 3]
list_b = ["Hello", 'Bye', 'Yes', 'No']

result = merge_lists_to_dict(list_a, list_b)
print(result)  # {0: 'Hello', 1: 'Bye', 2: 'Yes', 3: 'No'}

print('2. Second task')


def merge_lists_to_dict_2(index, value):
    list_1 = index.copy()
    list_2 = value.copy()
    merged_list = zip(list_1, list_2)
    converted_to_dict = dict(merged_list)
    return converted_to_dict


result = merge_lists_to_dict_2(value=list_b, index=list_a)
print(result)

result = merge_lists_to_dict_2(list_a, value=list_b)
print(result)

print('3. Third task')


def update_car_info(**cars):
    cars['is_available'] = True
    return cars


result_3 = update_car_info(brand='Toyota', price='12222')
print(result_3)

print('4. Callback function task')


def print_number_info(num):
    if (num % 2) == 0:
        print('Entered number is even')
    else:
        print('Entered number is odd')


def print_square_num(num):
    print('Square of number is:', num * num)


def process_number(num, callback_func):
    callback_func(num)


process_number(200, print_number_info)
process_number(3, print_square_num)

# use for list, dictionary, tuple, set, string

print('1. FOR IN list')
my_list = [True, 10, 'abc', {}]

for elem in my_list:
    print(f"{type(elem)}: {elem}")

print('2. List - Shortened')

all_nums = [-2, 3, -10]

absolute_nums = [abs(i) for i in all_nums]

# for i in all_nums:
#     absolute_nums.append(abs(i))

# for i in all_nums: absolute_nums.append(abs(i))

print(all_nums)
print(absolute_nums)

print('3. List - Shortened AND IF')

all_nums_2 = [-2, 3, -10, 5]
positives = [i for i in all_nums_2 if i > 0]

# for i in all_nums_2:
#     if i > 0:
#         positives.append(i)

print(positives)

print(dir())

print('4. FOR IN dict USUAL')

my_dict = {
    'x': 10,
    'y': True,
    'z': 'abc'
}

for key in my_dict:
    print(f"{key}: {my_dict[key]}")

my_dict = {
    'id': 10,
    'model': 'BMV',
    'color': 'red'
}

print('5. FOR IN dict Unpacking. Items()')

for item in my_dict.items():  # item is a tuple.
    # print(item)
    dict_key, value = item  # unpacking
    print(dict_key, ':', value)

print('6. FOR IN dict Unpacking. Items() short version')

for key, value in my_dict.items():  # item is a tuple.
    print(key, ':', value)

print('7. FOR IN in SET')

video_ids = {1234, 5678, 9101}

for video_id_element in video_ids:
    print(video_id_element)

print('8. FOR IN in STRING')

my_string = 'STRING'

for letter in my_string:
    print(letter)


print('8. FOR IN in RANGE-1')


for num in range(5):
    print(num)

print('8. FOR IN in RANGE-2')

for num_1 in range(3, 10, 2):
    print(num_1)
# 1. Создайте пустой словарь
#
# 2. Трижды попросите пользователя сначала
# ввести название ключа, а потом ввести
# значение для этого ключа. Всего должно быть
# 6 запросов на ввод текста.
#
# 3. Во время получения данных от пользователя
# добавляйте в словарь ключи с значениями
# согласно тому, что ввел пользователь
#
# 4. Выведите результирующий словарь в терминал

my_dict = {}
key_name_1 = input('Enter the name of the key: ')
key_name_2 = input('Enter the name of the key: ')
key_name_3 = input('Enter the name of the key: ')
key_name_4 = input('Enter the name of the key: ')
key_name_5 = input('Enter the name of the key: ')
key_name_6 = input('Enter the name of the key: ')


my_dict[0] = key_name_1
my_dict[1] = key_name_2
my_dict[2] = key_name_3
my_dict[3] = key_name_4
my_dict[4] = key_name_5
my_dict[5] = key_name_6

print(my_dict)
space = '\n'

#1  Как создать словарь
print('1. Как создать словарь', space)

shopping_list = {
    'молоко': 'milk', # Первый элемент словаря (в каждом элементе две части!)
    'сахар': 'sugar',  # Второй элемент словаря
    'мука': 'flour',  # Третий элемент
    'яйца': 'eggs',  # Четвёртый элемент
    'разрыхлитель': 'leaven',  # Пятый элемент
    'ваниль': 'vanilla'
} 

database = {
    'host': '192.168.0.10',
    'port': 5432,
    'user': 'Shrek',
    'password': 'My$wamp235'
} 

dump = {
    1: 'единица',               # Ключ - число, значение - строка.
    'земляника': 'ягода',       # И ключ, и значение - строки.
    'помидор': 'ягода',         # Значение 'ягода' - не уникально. Так можно.
    False: 0,                   # Ключ - булево значение, значение - число.
    'лук': ['овощ', 'оружие'],  # Ключ - строка, значение - список.
                                # Ключ - строка, а значение - словарь. Так тоже можно!
    'англо-русский словарь': {'молоко': 'milk', 
                              'сахар': 'sugar', 
                              'мука': 'flour'
                               }    
}

print(dump,space)


#2 Вызвать значение ключа
print('2. Вызвать значение ключа', space)
neighbours =  {
    11 : 'Александр',
    21 : 'Василий',
    26 : 'Антон',
    9 : 'Евгений'
}

print(neighbours[26],space)

#3 Изменить значение по ключу
print('3. Изменить значение по ключу', space)

neighbours =  {
    11 : 'Александр',
    21 : 'Василий',
    26 : 'Антон',
    9 : 'Евгений'
}
new = neighbours[21]='Лиза'

print('Теперь в квартире 21 живёт', new,space)


#4 Добавление элементов в словарь
print('4. Добавление элементов в словарь', space)
shopping_list = {
    'молоко': 'milk',
	'сахар': 'sugar',
    'мука': 'flour',
    'яйца': 'eggs',
	'разрыхлитель': 'leaven',
	'ваниль': 'vanilla'
}

# Создаём несколько новых элементов словаря с одинаковым ключом
shopping_list['лук'] = 'onion'  # Будет создан элемент с ключом 'лук'.
shopping_list['лук'] = 'bow'  # Значение под ключом 'лук' будет заменено.

print(shopping_list,space)


#5 Метод update
print('5. Метод update', space)

shopping_list = {
    'молоко': 'milk',
	'сахар': 'sugar',
    'мука': 'flour',
    'яйца': 'eggs',
	'разрыхлитель': 'leaven',
	'ваниль': 'vanilla'
}

additional_products = {'клубника': 'strawberries', 'малина': 'raspberries'}
shopping_list.update(additional_products)
print(shopping_list)
print(additional_products)


#6 Добавь в словарь neighbours новый элемент по ключу. Пусть нового жильца зовут Даниил, а его квартира — 47. 
# После этого напечатай словарь neighbours.
print('6. Добавление элемента по ключу', space)

neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей',
    2 : 'Толик',
    7 : 'Гена'
}
neighbours['47'] = 'Данил'
print(neighbours, space)

#7 Добавление по методу update
print('7. Добавление по методу update', space)

neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей',
    2 : 'Толик',
    7 : 'Гена'
}

new_neighbours =  {
    19 : 'Арсений',
    38 : 'Дима',
    3 : 'Никита'
}

neighbours.update(new_neighbours)
print(neighbours, space)

#8 Метод get и сообщение, если его нет
print('8. Метод get - получение по ключу, если не найдет, то выдаст предупреждение', space)

backpack = {
    'Большое отделение': 'Ноутбук',
    'Боковое отделение': 'Ключи',
    'Укреплённое отделение': 'Очки',
    'Малое отделение': 'Зарядное устройство'
}
s = backpack.get('Большое отделение')
print(backpack.get('Среднее отделение', 'Такого отделения нет'))
print(s,space)

#9 Потренируйся находить значения методом get(): выведи на экран жильцов 11-й и 9-й квартир.

neighbours = {
    11: 'Александр',
    21: 'Василий',
    26: 'Антон',
    9: 'Евгений'
}
print(neighbours.get(11))
print(neighbours.get(9))
print(neighbours.get(25, 'Такой квартиры нет'),space)

#10 Получить все ключи, значения 

shopping_list = {
    'молоко': 'milk',
	'сахар': 'sugar',
    'мука': 'flour',
    'яйца': 'eggs',
	'разрыхлитель': 'leaven',
	'ваниль': 'vanilla'
}

print(shopping_list.keys())
print(shopping_list.values(),space)

#10 Чтобы сделать из такой коллекции список, понадобится функция list():
print('10. Из коллекции создаем список', space)

shopping_list = {
    'молоко': 'milk',
	'сахар': 'sugar',
    'мука': 'flour',
    'яйца': 'eggs',
	'разрыхлитель': 'leaven',
	'ваниль': 'vanilla'
}

new_values = list(shopping_list.values())
new_keys = list(shopping_list.keys())
new = list(shopping_list)

print(new_values,new_keys, new, space)

#11 Задание на keys & values - Вывести ключ-значение в другом виде

print('11. Задание на keys & values - Вывести ключ-значение в другом виде', space)

neighbours =  {
    11 : 'Александр',
    21 : 'Лиза',
    26 : 'Антон',
    9 : 'Евгений',
    5 : 'Катя',
    33 : 'Сергей'
}

new_keys = list(neighbours.keys())
new_values = list(neighbours.values())
for k in new_keys:
    print(f'{k} - {neighbours[k]}')
print(space)

#12 Перебрать и ключи, и значения в цикле
print('12. Перебрать и ключи, и значения в цикле', space)


backpack = {
    'Большое отделение': 'Ноутбук',
    'Боковое отделение': 'Ключи',
    'Укреплённое отделение': 'Очки',
    'Малое отделение': 'Зарядное устройство'
}

for key, value in backpack.items():
    print(f'В {key} лежит {value}')
print(space)

#13 Перебрать ключи ИЛИ значения в цикле. Извлечём и напечатаем только значения (values) каждого элемента
print('13. Перебрать ключи или значения в цикле. Извлечём и напечатаем только значения (values) каждого элемента', space)


for value in backpack.values():
    print('Я взял с собой ' + value)

for item in backpack.keys():
    print('В моём рюкзаке есть ' +  item)

for item in backpack:
    print('В моём рюкзаке есть ' +  item)
print(space)

#14 Из двух списков делаем словарь
print('14. Из двух списков делаем словарь', space)

neighbours_names = ['Вася', 'Ира', 'Антон', 'Арина', 'Женя']
neighbours_flats = [4, 9, 12, 16, 19]
neighbours= {}
for i in range(0, len(neighbours_names)):    
        neighbours[neighbours_flats[i]] = neighbours_names[i]
for key, value in neighbours.items():
    print(f'В квартире {key} живет {value}')
print(space)

print('Метод питона из списков в словарь')
dictionary = {k: v for k, v in zip(neighbours_flats, neighbours_names)}
print(dictionary,space)

print('Метод как в практике!!!')
for i in range(0, len(neighbours_flats)):
    neighbours[neighbours_flats[i]] = neighbours_names[i]
    print(neighbours.get(neighbours_flats[i]) + ' живёт в квартире ' + str(neighbours_flats[i]))
print(space)


#print('Мой метод ПОЧЕМУ ТАК НЕЛЬЗЯ?')
#for flat in neighbours_flats:
#     for name in neighbours_names:
#          neighbours[neighbours_flats[flat]] = neighbours_names[name]
#print(neighbours,space)         

#15 Вывод списков-значений из словарей. Напечатай обо всех жильцах такое сообщение: <имена> живут в квартире <номер_квартиры>.
print('15. Вывод списков-значений в словарях', space)

neighbours =  {
    11 : ['Александр', 'Света'],
    21 : ['Лиза', 'Артём'],
    26 : ['Антон', 'Надя'],
    9 :  ['Евгений', 'Маша'],
    5 :  ['Катя', 'Костя'],
    33 : ['Сергей', 'Инга']
}

for key, value in neighbours.items():
    print(f'В квартире {key} живут {value[0]} и {value[1]}')
print(space)


#16 Тренировка вывода из словарей 
print('16. Тренировка вывода из словарей ', space)

# Выведи на экран, сколько людей живёт в квартире 11 (число)
print(len(neighbours[11]), space)

# Выведи на экран построчно всех жильцов квартиры 21
for key, value in neighbours.items():
    for i in value:
        if key == 21:
            print(i)
print(space)

# Выведи на экран имена всех вторых жильцов
for key, value in neighbours.items():
    print(value[1])
print(space)


#Проверка на наличие ключа в словаре - in 
print ('Проверка на наличие ключа в словаре - in')

shopping_list = {
    'молоко': 'milk',
	'сахар': 'sugar',
    'мука': 'flour',
    'яйца': 'eggs',
	'разрыхлитель': 'leaven',
	'ваниль': 'vanilla'
}
# Есть ли элемент 'разрыхлитель' в словаре shopping_list?
if 'разрыхлитель' in shopping_list:
    print('В словаре: нашлось!') 
else:
    print('В словаре: не нашлось :(')

#Проверка на наличие значения в словаре - values() и keys(). Есть ли элемент 'leaven' среди ключей ИЛИ значений словаря shopping_list?

if 'leaven' in shopping_list.keys() or 'leaven' in shopping_list.values():
    print('В словаре: нашлось!') 
else:
    print('В словаре: не нашлось :(') 

# Проверка на отсутствие в коллекции

if 'клубника' not in shopping_list:
    print('Не хватает клубники для украшения панкейков!',space) 

#ЗАДАЧА 1: отфильтровать фильмы по оценке. Оставь только те, у которых она больше или равна 8.5. 
# Отфильтрованные пары запиши в новый словарь filtered_movies и выведи его на экран.
print('Задача 1',space) 


movies = {'Игры разума': 8.3, 
          'Зеленая миля': 9.1, 
          'Леон': 8.5, 
          'Эффект бабочки': 8.2, 
          'Матрица': 8.6, 
          'Криминальное чтиво': 8.7
          }
filtered_movies= {}

for movie, rating in movies.items():
    if rating >= 8.5:
        filtered_movies[movie] = rating

print(filtered_movies)

#ЗАДАЧА 2:  наполнить словарь rainbow_dict парами ключ-значение. 
# Ключ — слово из списка mnemo, а значение — соответствующий слову цвет из списка colors.
print('Задача 2',space) 

mnemo = ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан']
colors = ['оранжевый', 'голубой', 'фиолетовый', 'красный', 'желтый', 'синий', 'зеленый']
rainbow_dict={}

rainbow_dict = {}
for i in mnemo:
    for n in colors:
        if i[0] == n[0]:
          rainbow_dict[i]= n
print(rainbow_dict)

#ЗАДАЧА 3: Создай словарь, где ключ — номер квартиры, а значение — списки с именами жильцов. 
# Каждая пара жильцов — это отдельный список.
print('Задача 3',space) 

new_neighbours = [['Вася', 'Катя'], ['Юра', 'Марина'], ['Лёша', 'Ира'], ['Петя', 'Надя'], ['Ваня', 'Света']]
flats=[1,2,3,4,5]
house_dict = {}

for i in range(0, len(new_neighbours)):
    house_dict[flats[i]] = new_neighbours[i]
print(house_dict,space)

house_dict = {flat: neighbours for flat, neighbours in zip(flats, new_neighbours)}
print(house_dict,space)
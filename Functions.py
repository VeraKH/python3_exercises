space = ('\n')

#1. Учимся объявлять функцию
print('1. Учимся объявлять функцию')

def check_story_points_sum():
    if sum(tasks) <= 80:
        print("Укладываемся в спринт")
    elif sum(tasks) >= 80:
        print('Задачи не влезают. Нужно что-то выкинуть')

tasks = []
tasks = [3, 3, 13, 8, 13, 2, 5, 5, 1, 13, 8, 2, 5]
check_story_points_sum()
tasks = [5, 3, 13, 5, 13, 2, 5, 5, 2, 13, 8, 1, 5]
check_story_points_sum()
tasks = [13, 13, 13, 8, 5, 2, 5, 2, 1, 5, 8, 2, 2]
check_story_points_sum()
print(space)


#2. Учимся объявлять функцию с параметрами
print('2. Учимся объявлять функцию с параметрами')

current_sprint = []
not_in_sprint = []

def add_task_to_sprint(story_points):
    if story_points < 8:
        current_sprint.append(story_points)
    else:
        not_in_sprint.append(story_points)

add_task_to_sprint(2)

add_task_to_sprint(5)

add_task_to_sprint(5)

add_task_to_sprint(13)

add_task_to_sprint(8)

add_task_to_sprint(1)

add_task_to_sprint(2)

# выведи сумму SP в спринте и сумму тех SP, которые не уместились в спринт
print (sum(current_sprint))
print (sum(not_in_sprint),space)


#3.  написать функцию, которая проверит, достаточно ли переданных данных для авторизации на сайте.
print('3.проверяем, достаточно ли переданных данных для авторизации на сайте')
def is_authorized_user(user):
    if user[0] and user[1] or user[2]:
        print('OK')
    else:
        print('no')

user_1 = ['login', 'password', '']
is_authorized_user(user_1)

user_2 = ['', '', 'token']
is_authorized_user(user_2)

user_3 = ['login', '', '']
is_authorized_user(user_3)

user_4 = ['', '', '']
is_authorized_user(user_4)


#4. Доработать функцию: Если состояния condition_a и condition_b совпадают, она возвращает True. Если состояния не совпадают — False.

def condition_check(condition_a, condition_b):
    if condition_a == condition_b:
        return True
    else:
        return False
    
print(condition_check('a', 'b'))   # False
print(condition_check(1, '1'))     # False
print(condition_check(['Кнопка 1', 'Поле 2'], ['Кнопка 1', 'Поле 1'])) # False
print(condition_check(['Кнопка 1', 'Поле 1'], ['Кнопка 1', 'Поле 1'])) # True
print(space)

#5. Доработать функцию, чтобы она определяла, палиндром перед ней или нет. Либо True, либо False.

def is_palindrome(string):
    string = string.replace(' ','')
    if string == string[::-1]:
        return True
    else:
        return False

print(is_palindrome('молебен о коне белом')) # True
print(is_palindrome('колобок'))  # False
print(is_palindrome('121'))  # True
print(space)

#5. Передать в функцию параметры
print('5.Передать в функцию параметры')

def is_authorized_user(login='нет', password='нет', token='нет'):
	# тело функции менять не нужно
	if login and password or token:
			print('OK')
                        

user_1 = ['', '', '']
is_authorized_user(user_1[0], user_1[1], user_1[2])

user_2 = ['login', 'password']
is_authorized_user(login=user_2[0],password=user_2[1])

user_3 = ['token']
is_authorized_user(token=user_3[0])

user_4 = ['login', '']
is_authorized_user(login=user_4[0])
print(space)

#5. Вызвать функцию рэндом
print('5.Передать в функцию параметры')

import random as rdm # Подключи библиотеку random и дай ей краткое имя
country_code = '+7'  # код страны пусть будет всегда +7
operator_code = rdm.randint(100, 999) # используй randint, чтобы сгенерировать трехзначный код оператора
last_digits = rdm.randint(1000000, 9999999) # используй randint, чтобы сгенерировать оставшиеся 7 цифр (без дефисов)
fake_number = country_code + str(operator_code) + str(last_digits)
print(fake_number,space)

#6. Вызвать функцию рэндом
print('6.Функция, которая определяет, есть ли у пользователя доступ к странице.')

     
def has_permission(page, user):
    if page == 'Управление':
        return is_admin(user)
#        if is_admin(user):
#           return True
#        else:
#             return False
    else:
         return True

def is_admin(user):
    return user == 'admin' 
#    if user == 'admin':
#         return True
#    else:
#       return False

print(has_permission(page='Рестораны', user='user_a'))
print(has_permission(page='Избранное', user='admin'))
print(has_permission(page='Управление', user='admin'))
print(has_permission(page='Управление', user='user_b'))


#7. Написать функцию 
print('6.Функция mail_checker принимает на вход три параметра: mail_to — кому отправить, mail_from — от кого, mail_text — текст письма. ',space)

def mail_checker(mail_to, mail_from, mail_text):
     print(f'Получатель: {mail_to}')
     print(f'Отправитель: {mail_from}')
     print(f'Текст письма: {mail_text}')

mail_checker(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')
print(space)

#7. Написать функцию 
print('7.функция выводит письма по получателям.')

mail_box = {}
def mail_checker(mail_to, mail_from, mail_text):
    if mail_box.get(mail_to)==None:
        mail_box[mail_to]=[{mail_from:mail_text}]
    else:
        mail_box[mail_to].append({mail_from:mail_text})



mail_checker(mail_to='john_connor@yandex.ru', mail_from='terminator@yandex.ru', mail_text='Привет, я вернулся!')
mail_checker(mail_to='john_connor@yandex.ru', mail_from='sarah_connor@yandex.ru', mail_text='Сынок, надень шапку')
mail_checker(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Правая рука чешется, не знаю, что и делать')
mail_checker(mail_to='luke_skywalker@yandex.ru', mail_from='darth_vader@yandex.ru', mail_text='Что бы сказал на это твой отец?')
print(mail_box,space)

#8. Написать функцию 
print('8.Функция, которая определяет, спам письмо или нет ')

mail_box = {}   # тут хранятся проверенные письма
spam = []   # сюда складываем спам
    
# проверка строки на наличие стоп-слов, используется внутри is_spam()
def str_contains_stop_words(string):
    stop_words = ['Без вложений', 'Скидки', 'Распродажа', 'Выгода', 'Гарантия']
    for w in stop_words:
        if w in string:
            return True
    return False


def is_http(mail_text):
    stop_rules = ['https', 'www']
    for w in stop_rules:
        if w in mail_text:
            return True
    return False


def is_uppercases(mail_text):
        mail_text= mail_text.split()
        for i in mail_text:
            if i.isupper():
                 return True
        return False

def is_spam(mail_text):
    return str_contains_stop_words(mail_text) or is_uppercases(mail_text) or is_http(mail_text)

def mail_checker(mail_from, mail_to, mail_text):
    if is_spam(mail_text):         
         spam.append({mail_from:mail_text})
    else:
         mail_box[mail_to]=[{mail_from:mail_text}]

mail_checker(mail_to='yoda_master@yandex.ru', mail_from='luke_skywalker@yandex.ru', mail_text='Магистр Йода, а в чём сила?')
mail_checker(mail_to='ilon_mask@yandex.ru', mail_from='trusted_mail@yandex.ru', mail_text='Скидки на акции Tesla, только у нас!')
mail_checker(mail_to='chandler_bing@yandex.ru', mail_from='ross_geller@yandex.ru', mail_text='Смотри, я открыл новый вид динозавра https://rossoceraptor.html')
mail_checker(mail_to='piter_parker@yandex.ru', mail_from='j_jonah_jameson@yandex.ru', mail_text='Паркер! Мне срочно нужны фото Паука!')
mail_checker(mail_to='neo@yandex.ru', mail_from='bad_matrix@yandex.ru', mail_text='РАСПРОДАЖА!!! ДВЕ КРАСНЫХ ТАБЛЕТКИ ПО ЦЕНЕ ТРЁХ СИНИХ')

print('Входящие:', mail_box, space)
print('Спам:', spam)
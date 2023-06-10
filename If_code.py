#1
count_password_symbols = 0
if count_password_symbols == 0:
    print('Поле пароля не может быть пустым!')

print('****')
#2
is_test_passed = 'False'
if is_test_passed == 'False':
    print('Тест не пройден!')

print('****')
#3
task_status_1 = 'Можно тестировать'
task_status_2 = 'Открыта'
task_status_3 = 'В работе'
task = task_status_3
if task ==task_status_1:
    print('Пора тестировать задачу!')
else: 
    print('Задача ещё не передана в тестирование!')

print('****')
#4
team1_wins = 3
team2_wins = 3
if team1_wins > team2_wins:
    print('Победила команда 1')
elif team1_wins < team2_wins:
    print('Победила команда 2')
else:
    print('Победила дружба')

print('****')
#5
if task_status_1 == 'Можно тестировать':
    print('Пора тестировать задачу!')
elif task_status_1 == 'Открыта':
    print('Задача ещё находится в работе')
else:
    print('Задача ещё не передана в тестирование!')

if task_status_2 == 'Можно тестировать':
    print('Пора тестировать задачу!')
elif task_status_1 == 'Открыта':
    print('Задача ещё находится в работе')
else:
    print('Задача ещё не передана в тестирование!')

print('****')
#6
button_color = 'розовый'
if button_color == 'синий':
    print('Это кнопка сохранения')
elif button_color == 'желтый':
    print('Это кнопка перехода на следующую страницу')
elif button_color == 'красный':
    print('Это кнопка закрытия страницы')
else:
    print('Такой кнопки на сайте нет!')

print('****')
#7
player1 = 20
player2 = 15
record = 21

if player1 > player2 and player1 > record:
    print('Игрок 1 занял первое место и поставил новый рекорд!')
elif player1 < player2 and player2 > record:
    print('Игрок 2 занял первое место и поставил новый рекорд!')
elif  player1 > player2:
    print('Игрок 1 занял первое место!') 
else:
    print('Игрок 2 занял первое место!') 

print('****')
#8
player1 = 22
player2 = 23
record = 21

if player1 > record or player2 > record:
    print('У нас новый рекорд!')
    if  player1 > player2:
        print('Игрок 1 занял первое место!') 
    else:
        print('Игрок 2 занял первое место!') 

print('****')
#9
tomatoes = True
meat = False
cream_souce = True
bacon = True

if (tomatoes and meat) or (cream_souce and bacon):
    if tomatoes and meat:
        print('Закажем болоньезе')
    else:
        print('Закажем карбонару')
else:
    print('Придётся заказать что-то ещё')
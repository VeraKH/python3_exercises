#1
names = ['Андрей', 'Игорь', 'Ольга', 'Василий', 'Елена']

for name in names:
    print(name)
print('\n')


#2
friends = ['Артём', 'Катя', 'Егор', 'Настя', 'Петя', 'Илья', 'Саша']
print('Завтра вечером у меня будет вечеринка!')
for friend in friends:
    print(friend + ', приглашаю завтра в гости!')
print('Будет весело!\n')



#3 В последовательность не входит последнее число диапазона.
friends = ['Артём', 'Катя', 'Егор', 'Настя', 'Петя', 'Илья', 'Саша']
for friend in friends:
    print(f'Имя {friend} состоит из {len(friend)} букв.\n')


#3
twenty = range(1,21)
for num in twenty:
    print(num) 
print('\n')    


#4 Если последовательность начинается с нуля, можно указать только конец диапазона.
twenty = range(21)
for num in twenty:
    print(num) 
print('\n')    


#5 Диапазон может включать в себя отрицательные числа.
around_zero = range(-2,2)
for num in around_zero:
    print(num) 
print('\n')    

#6 Можно указать шаг последовательности.
around_zero = range(-5,5,2)
for num in around_zero:
    print(num) 
print('\n') 


#7 Задать диапазон можно сразу в условии цикла.
for i in range(-8,5,2):
    print(i) 
print('\n') 


#8 В доме пять этажей. Ты хочешь подняться на каждый из них. Выведи на экран номер каждого этажа:

for i in range(1,6):
    print(f'Я сейчас на этаже {i}')
print('Я уже на самом верху!\n') 


#9 В этот раз нужно подняться со второго на четвёртый этаж.
for i in range(2,5):
    print(f'Этаж № {i}')
print('\n') 


#9 В этот раз нужно спуститься со четвёртого на второй этаж.
for i in reversed(range(2,5)):
    print(f'Этаж № {i}')
print('\n') 


#10 Так выглядит с reversed() обратное чтение списка:
seasons = ['зима', 'весна', 'лето', 'осень']
for season in reversed(seasons):
    print(season)
print('\n')


#11
for i in reversed(range(1,6)):
    print(f'Этаж № {i}')
print('\n') 

#12 Как создать срез
buttons = ['Отели', 'Авиа', 'Ж/д', 'Автобусы', 'Туры'] 
print(buttons[1:4:2])

#12 Краткая форма написания
buttons = ['Отели', 'Авиа', 'Ж/д', 'Автобусы', 'Туры'] 
#print(buttons[1:4:1])
print(buttons[1:4])


#13 Если индексы начала и конца среза совпадают с индексами 1 и последнего элемента списка, их не указывают. Это значения по умолчанию.
buttons = ['Отели', 'Авиа', 'Ж/д', 'Автобусы', 'Туры'] 
print(buttons[::2]) # Указали только величину шага. Срез будет включать первый элемент и каждый третий
print(buttons[1:]) # Указали начало среза 1, чтобы исключить первый элемент списка # Шаг автоматически = 1


#13 
notes = ['зелёный', 2023, 9*3*100, 'ёлка', 'коты — жидкость?', 36, 'Терминатор']
print(notes[1::3]) 
#Срез начнётся со второго элемента списка. У него индекс 1.
#Первый элемент среза 2023. После него в срез пойдёт каждый четвёртый элемент.
#Шаг равен трём. Это значит, в срез войдёт каждый четвёртый элемент после 2023.

#14!!!! Величина шага в срезе может быть отрицательным числом !!!!
buttons = ['Отели', 'Авиа', 'Ж/д', 'Автобусы', 'Туры'] 
print(buttons[::-2])

#15
floors = [1, 2, 3, 4, 5]
print('Я стою на 5 этаже')
for floor in floors[::-1]:
    print(f'Я спустился с {floor} на {floor-1}')
print('\n')

#16 На улице стоят 10 домов. Они записаны в список houses. Ты идёшь от десятого дома к первому. 
# С помощью обратного среза напечатай на экране свой путь.
#Обрати внимание: нулевого дома не существует. Учитывай это в решении.

houses = list(range(11)) # это короткий способ создать список из чисел от 0 до N
for house in houses[:0:-1]: #[11:0:-1]
    print(f'Пройден дом: {house}')
print('\n')


#16 Вложенные циклы
rooms_floor1 = ['Номер 1', 'Номер 2', 'Номер 3', 'Номер 4']
rooms_floor2 = ['Номер 5', 'Номер 6', 'Номер 7', 'Номер 8']
rooms_floor3 = ['Номер 9', 'Номер 10', 'Номер 11', 'Номер 12']

hotel_floors = [rooms_floor1, rooms_floor2, rooms_floor3]

for floor_rooms in hotel_floors: # Запустили внешний цикл по списку hotel_floors
    for room in floor_rooms:  #Создали вложенный цикл для хождения по списку номеров, который записан в переменную
        print('Убрать '+room)
    print('Подняться на этаж выше')
print('Все убрано\n')

#17 Вложенные циклы

streets_city1 = ['улица Строителей', 'улица Правды', 'улица Свободы']
streets_city2 = ['улица Строителей', 'улица Правды', 'улица Свободы']
streets_city3 = ['улица Строителей', 'улица Правды', 'улица Свободы']
cities = [streets_city1, streets_city2, streets_city3]

for city in cities:
    for street_city in city:
        print(street_city)
print('\n')


#18

num = 0
for i in range(0,11,2):
    if i < 8 and i !=4:
        num =+i
print(num)
print('\n')

#18 В базе данных есть записи о возрасте клиентов. Посчитай, сколько клиентов старше 21, но младше 60 лет.

clients = [19, 22, 42, 28, 69, 51, 18, 70]
count = 0
for client in clients:
    if client>21 and client<60:
       count +=1
print(count)
print('\n')

#19 Ключевые слова break в циклах

clients = [19, 22, 42, 28, 69, 51, 18, 70]
for client in clients:
    if client == 42:
        break
    print(client)
print('\n')


#19 Ключевые слова continue в циклах
for client in clients:
    if client == 42:
        continue
    print(client)
print('\n')

#20 
for i in range(1,5):
    print('Овца ', i)
    
    for j in range(1,10):
        print('Корова ', j)
        if j ==2:
            break

#21
for i in range(1,10):
    if i ==6:
        break
    print('Этаж', i)
print('\n')


#22 # напиши здесь цикл, который добавит в список lst все числа с 0 до 100 с 9 на конце
lst=[]
for i in reversed(range(101)):
    if i%10 == 9: 
      lst.append(i)
#lst = lst[::-1]
print (lst)
print('\n')


#23 В переменной st хранится строка а роза упала на лапу азора. 
# Это палиндром — фраза, которая читается одинаково слева направо и справа налево. 
# Попробуй написать код, который перевернёт её и запишет результат в другую переменную.
#С помощью цикла for запиши перевёрнутую строку st в переменную s.  
# Для этого используй функцию reversed() в условии цикла. Внутреннюю переменную назови i.


st = 'а роза упала на лапу азора'
s = []
for i in reversed(st):
    s.append(i)
print(s)

#24 В переменной st хранится строка а роза упала на лапу азора. 
lst = [18, 5, 44, 21, 9, 4, 19, 100, 23, 101, 27]
int_sum = 0

for n in lst:
    if n<20:
        continue
    elif n > 100:
        break
    else:
        int_sum=+n    
print(int_sum)
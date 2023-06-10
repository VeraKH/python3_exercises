from copy import deepcopy # импортировали метод deepcopy из модуля copy

print('*12*')
# ['Высокий', 'Средний', 'Низкий']
#['Блокирующий', 'Критический', 'Значительный', 'Незначительный', 'Тривиальный']

priority = ['Значительный', 'Средний', 'Тривиальный']
severity = ['Низкий', 'Незначительный', 'Блокирующий', 'Высокий', 'Критический']

priority.insert(0,severity.pop(-2))
priority.insert(3,severity.pop(0))
severity.insert(0,severity.pop(1))
severity.insert(1,severity.pop())
severity.insert(2, priority.pop(1))
severity.insert(4, priority.pop())
print(priority)
print(severity)


print('*11*')
paintings = ['Мона Лиза', 'Дама с Горностаем']
collection = deepcopy(paintings)
collection.append('Витрувианский человек')
print('В коллекции теперь:', collection)

print('*11*')
hobbits = ['Фродо', 'Cэм', ['Орёл 1', 'Орёл 2']]
new_hobbits_list = deepcopy(hobbits)
print(hobbits, new_hobbits_list)
new_hobbits_list.append('Бильбо')
new_hobbits_list[2].append('Орел 3')
print(new_hobbits_list)
print(hobbits)


print('*10*')
hobbits = []
hobbits.append('Фродо')
hobbits.insert(1,'Сэм')
print(hobbits)
hobbits=hobbits.pop()
print(hobbits)
print('Cэм' in hobbits)
print(hobbits)

print('*9*')
hobbits = ['Фродо', 'Смеагол', 'Сэм', 'Мерри', 'Пиппин']
hobbits.pop(1)
print(hobbits)
print('Смеагол' not in hobbits)
is_there = 'Смеагол' not in hobbits
print(is_there)

print('*8*')
#Из списка hobbits необходимо удалить всех хоббитов по одному, используя изученные методы.
hobbits = ['Фродо', 'Сэм', 'Мерри', 'Пиппин']
hobbits.pop(0)
print(hobbits)
hobbits.remove('Мерри')
hobbits.remove('Пиппин')
hobbits.pop()
print(hobbits)

print('*7*')
#Попробуй дописать код так, чтобы он удалил Фродо из lst и добавил его в начало списка hobbits. Используй метод insert().
hobbits = ['Cэм', 'Пиппин']
lst = ['Мерри', 'Фродо']

hobbits.insert(0,lst.pop())
print(hobbits)
print(lst)

print('*6*')
#Этим способом можно перенести Фродо из hobbits в список lst:
hobbits = ['Фродо', 'Cэм', 'Пиппин']
lst = ['Мерри']
lst.append(hobbits.pop(0))
print(lst)


print('*5*')
hobbits = ['Фродо', 'Cэм', 'Бильбо', 'Мерри', 'Пиппин']
hobbits.remove('Бильбо')
print(hobbits)

print('*4*')
hobbits = ['Фродо', 'Сэм']
# сначала включи в список «Мерри»
hobbits.append('Мерри')
hobbits.append('Пиппин')
print(hobbits)

#4
print('*4*')
severity_list = ['Блокирующий', 'Критический', 'Значительный', 'Незначительный', 'Тривиальный']
severity_len = len(severity_list)
print(f'Уровень критичности бага: {severity_list[severity_len-1]}')


#3
print('*3*')
# добавь числовые значения приоритетов по порядку, начиная с 1
priority = [1,2,3]
# укажи индекс среднего приоритета
medium_priority_index = 1
print('Баг с приоритетом:', priority[medium_priority_index])


#2
print('*2*')
print('Очередной баг на проде')
bug_report = ['Заголовок', 'Автор', 'Исполнитель', 'Версия', 'Описание', 'Критичность', 'Приоритет']
print(bug_report)


#1
print('*1*')
shopping_list = ['молоко', 'сахар', 'мука', 'яйца', 'разрыхлитель', 'ваниль']
print(len(shopping_list))










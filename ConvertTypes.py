
#1
number = 5
friends = ' друзей'
# преобразуем число в строку и проведём конкатенацию строк
print(str(number) + friends)

#2
twenty = '20'
twenty_two = '22'
# сложили две строки
print(int(twenty)+int(twenty_two))

#3
biscuit = 50
candies = '190'
print(biscuit+int(candies))

#4
total = 240
text = 'Сумма покупки составляет '
rubles = ' рублей'

#5
count = 5
print(f'Завершено {count} тестов')

#6
passed = 3
failed = '2'
count = passed + int(failed)

message_result  = f'Завершено тестов {count}'
message_detail = f'Успешно пройдено: {passed}, упало в ошибку {failed}.' 
#message_details = 'Успешно выполнено: ' + str(passed) + ', упало в ошибку: ' + failed
print(message_result)
print(message_detail)
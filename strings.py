space = '\n'

#1
s = 'строка'
print(len(s))
print(s[1])
print(s[-1])
print(s[-len(s)])
print(s[len(s) - 1],space)

#2 Срез подстроки
a = 'Жил-был в норе под землей хоббит'
b = a[0:3]
print(b)

#3 Сокращенная форма
с = a[:3]
print(b,space)

print(a[:-7])
print(a[:7])    # Жил-был 
print(a[:],space)

#4 Оператор in

s = '«Эх, как же хочется в Тамбов», — подумал мальчик'

print('»' in s) #True
print('К' in s) #False
print('тамбов' in s) #False
print(space)


#4 Метод split()
line = 'Волшебник никогда не опаздывает, Фродо Бэггинс.'
print(line.split(','))
print(line.split())
print(space)


#5 Метод split()

ips = []
string = '192.168.12.12 Илон Маск 115.253.1.1 noname 255.25.191.14 Лев Толстой 112.15.191.09 Курт Воннегут'
new_string = string.split()
for i in new_string:
    if '.'in i:
        ips.append(i)
print(ips,space)

#5 Метод replace()
quote = 'Нельзя просто так взять и войти в Мордор'
new_quote = quote.replace('Нельзя','Можно')
print(new_quote)
print(quote,space)

#6 Метод replace() - количество совпадений

quote2 = 'Из них вывозят и вывозят куда-то мебель, ковры, картины, цветы, растения.'
new_quote = quote2.replace('вывозят', 'выносят', 1)
print(new_quote,space)

#6 Метод replace() - удаление подстрок
new_quote = new_quote.replace(', растения', '')
print(new_quote, space)

#6 Метод replace() - много разных замен (но читать не удобно)
s = 'http://www.practicum.yandex.com/%20profile/'
new_s = s.replace('http', 'https').replace('www.', '').replace('com', 'ru').replace('%20', '')
print(new_s, space)

#7 #Как replace() работает с циклом

string_to_replace = '1000€ 345₽ 7738£ 984$ 345€ 4455¥ 34₽ 668$ 6284$ 145€'
replaced_symbols = ['€', '$', '£', '¥']
rub = '₽'
for s in replaced_symbols:
    string_to_replace = string_to_replace.replace(s, rub)
print(string_to_replace,space)

#8
phones = '996 934 85 92;9109676472;(920)751-61-12;9159143161;910-951-51-15;(960)9400088'
phones = phones.replace('(','').replace('-','').replace(')','').replace(' ','')
print(phones, space)

#9
replaced_symbols = ['(', ')', '-', ' '] 
for s in replaced_symbols:
    phones = phones.replace(s, '')
print(phones)

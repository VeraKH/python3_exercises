# 1. Создайте набор с нескольких элементов типа int
# 2. Добавьте в него ещё один элемент
# 3. Создайте ещё один набор с несколькими элементами, причём некоторые должны быть такими же как в первом наборе
# 4. Найдите общие элементы в двух наборах и поместите их в новый набор
# 5. Конвертируйте результирующий набор в список и выведите список в терминал


a = {4, 8, 9, 10, 12}
b = {4, 2, 9, 2, 1}
a.add(12)
d = a & b
print(d)
print(list(d))
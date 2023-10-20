try:
    print(10 / 0)
except ZeroDivisionError:
    print('Error - Division by zero')

print('Continue')

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(type(e))
    print(dir(e))
    print(e)

print('Continue...')

try:
    print(10 / 2)  # ('10'/2)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('There was no error')  # if there is no exepted errors
finally:
    print('Continue')  # Output in any way

try:
    print(10 / 0)
except Exception as e:
    print(e)
else:
    print('There was no error')  # if there is no exepted errors
finally:
    print('Continue')  # Output in any way

try:
    print(10 / 0)
except:
    print('Some error')
else:
    print('There was no error')  # if there is no exepted errors
finally:
    print('Continue')  # Output in any way

print('Creating errors')


def devide_nums(a, b):
    if b == 0:
        raise TypeError("Second arg can't be zero")
    return a / b


try:
    devide_nums(10, 0)
# except ZeroDivisionError as e:
#    print(e)
except TypeError as e:
    print(e)
finally:
    print('Continiue')

print('Task')


def image_info(my_diction):
    if 'id' or 'title' not in my_diction:
        raise TypeError('No id or title')
    return f"Image my {my_diction['title']} has {my_diction['id']}"


my_dict = {
    #'title': 'Vasya',
    'color': 'black',
    'id': '121212'
}

aba = image_info(my_dict)
print(aba)
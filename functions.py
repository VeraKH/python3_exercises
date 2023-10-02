import datetime

# FUNCTIONS is an object.

a = 4
b = 2
c = a + b
print(c)

a = 8
b = 2
c = a + b
print(c)


def sum_1(r, e):
    d = r + e
    print(d)


print('1. CALL the functions')

sum_1(3, 2)
sum_1(7, 7)

print('2. FUNCTIONS is an object.', type(sum_1))

print('3. We can change values of the function inside it:')


def sum_1(a, b):
    a = a + 1
    c = a + b
    return c


result = (sum_1(2, 4))
print(sum_1(2, 4), result)

print('4. Return None if no word return:')


def sum_2(a, b):
    a = a + 1
    c = a + b


print(sum_2(10, 2))

print('5. The shortest function in python, created not fiiled functions')


def my_fn():
    pass  # keyword that func is not empty.


print(my_fn())

print('6. Give to function non changeable objects. '
      'Inside the function we cannot change outside objects')

num_one = 10
num_two = 5


def sum_2(a, b):
    a = a + 1
    c = a + b
    return c


res = sum_2(num_one, num_two)
print(res)
print(num_one)

print('7. Give to function changeable objects. We give parameters to function by link'
      'It changes outside vars. IT iS NOT Recommended'
      )


def increase_person_age(person):
    person['age'] += 1
    return person


person_one = {
    'name': 'Bob',
    'age': 21
}

increase_person_age(person_one)
print(person_one['age'])

print('8. How to avoid changing of the object? To create a copy of it')


def increase_person_age_two(person):
    person_copy = person.copy()  # copy for unchangeble objects. for changeble is deepcopy
    person_copy['age'] += 1
    return person_copy


person_copy = increase_person_age_two(person_one)

print(person_copy['age'])
print(person_one['age'])

print('9. Function can take any quantity of arguments? Yes, if we combine them to tuple.')


def sum_sum(*args):
    print(args)
    print(type(args))

    print(args[0])
    return sum(args)


print(sum_sum(2, 3, 5))

print('10. Argument position is important!')


def get_posts_info(name, post_qty):
    info = f"{name} wrote{post_qty}"
    return info


info = get_posts_info('Bogdan', 25)
print(info)

print('11. agruments with Key words - positioning is not important')
info = get_posts_info(post_qty=25, name='Bogdan')
print(info)

print('12. Key words and positioning')
info = get_posts_info('Bogdan', post_qty='25')
print(info)

print('13. Agruments dict')


def get_posts_info(**person):
    print(person)
    print(type(person))

    info = (
        f"{person['name']} wrote "
        f"{person['post_qty']} posts"
    )
    return info


info = get_posts_info(post_qty=25, name='Bogdan')
print(info)

print('14. Agruments dict')


def get_posts_info_2(**person):
    info = f"{person['name']} wrote {person['post_qty']} posts"
    print(person)
    print(type(person))
    return info


info = get_posts_info_2(post_qty=25, name='Bogdan', tel='23232')
print(info)

print('15. Default values')


def mult_by_factor(value, multiplier=1):
    return value * multiplier


print(mult_by_factor(2, 3))
print(mult_by_factor(2))


def get_weekday():
    return datetime.date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 1,
    'author': 'Vera'
}


post = create_new_post(initial_post)
print(post)
print(initial_post)

print('16. Callback function')


def other_fn():
    pass


def fn_with_callback(callback_fn):
    callback_fn()


fn_with_callback(other_fn())






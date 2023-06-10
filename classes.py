space = ('\n')

#1 Объявление класса и создание объекта
print('1.Объявление класса и создание объекта')

class Dog:
    tail = 1
    paws = 4

    def __init__(self, name, color):
        self.dog_name = name
        self.dog_color = color

dod_1 = Dog('Барбос','Желтый')
dod_2 = Dog('Липа','Черный')

print(dod_1.dog_name, dod_2.dog_color,space)

#2 Задание  - создание кнопки
print('2.Задание  - создание кнопки')

class Button:
    width = 50
    height = 200

    def __init__(self, color, text):
            self.button_color = color
            self.button_text = text

button_1 = Button('желтый', 'Купить')
button_2 = Button('красный','Удалить')

print(button_1.width) # выведи ширину жёлтой кнопки
print(button_1.button_color)  # выведи цвет жёлтой кнопки
print(button_2.width) # выведи ширину красной кнопки
print(button_2.button_color) # выведи цвет красной кнопки
print(space)


#3 Методы 
print('3.Объявление и вызов метода')

def bark(self):
     print('гав-гав')


class DogDog():
    tail = 1
    paws = 4

    def __init__(self, name, color):
        self.dog_name = name
        self.dog_color = color

    def bark(self):  #объявляем метод, чтобы выводить «гав-гав»
        print('гав-гав')  

dod_1 = DogDog('Барбос','Желтый')
dod_1.bark()
print(space)


#4 Метод dict для отображения объекта в читаемой форме
print('4. Метод dict для отображения объекта в читаемой форме')

print(dod_1.__dict__)
print(space)

#4 Задание Вызвать метод другого класса (класс Dog)
print('4.Задание Вызвать метод другого класса ')


class DogOwner():
    def __init__(self, name, dog):
        self.name = name
        self.my_dog = dog

    def ask_dog_to_bark(self):
        self.my_dog.bark()
    
    def say_dogs_color(self):
        print('у меня собака',self.my_dog.dog_color)
         
    def call_my_dog_name(self):
        print('Ко мне, ',self.my_dog.dog_name)


class MyDog():
    def give_dog_food(self):
        self.satiety += 10
        print(self.name, 'сыт на', self.satiety, 'процентов!')
    
    def pet_dog(self):
        self.satiety += 25
        print(self.name, 'доволен на', self.satiety, 'процентов!')


"""
    Итераторы

Объекты, элементы которых можно перебирать в цикле for, содержат в себе объект итератор,
для того, чтобы его получить необходимо использовать функцию iter(),
а для извлечения следующего элемента из итератора – функцию next().
"""
num_list = {1, 2, 3, 4, 5}

for i in num_list:
    print(i)
# Приведенный выше код мы также можем написать так:
itr = iter(num_list)
print(next(itr))  # 1
print(next(itr))  # 2
print(next(itr))  # 3
print(next(itr))  # 4
print(next(itr))  # 5

# print(next(itr))
# если количество итераций больше, чем доступно, то мы увидим исключение StopIteration
#
# Traceback (most recent call last):
#   File "C:/Users/mango/PycharmProjects/python-lessons/lesson08.py", line 18, in <module>
#     print(next(itr))
# StopIteration

"""
    Создание собственных итераторов

Создадим класс, объект которого будет итератором, выдающим определенное количество единиц,
которое пользователь задает при создании объекта.
Такой класс будет содержать конструктор, принимающий на вход количество единиц и метод __next__(),
без него экземпляры данного класса не будут итераторами.
"""


class SimpleIterator:
    def __init__(self, limit=10):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


s_iter1 = SimpleIterator(3)

print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))

# print(next(s_iter1))
# снова исключение StopIteration


"""
    Генераторы

Генераторы позволяют значительно упростить работу по конструированию итераторов.
В предыдущих примерах, для построения итератора и работы с ним, мы создавали отдельный класс.
Генератор – это функция, которая будучи вызванной в функции next()
возвращает следующий объект согласно алгоритму ее работы. Вместо ключевого слова return
в генераторе используется yield
"""


def simple_generator(val):
    while val > 0:
        val -= 1
        yield val


# Данная функция будет работать точно также, как класс SimpleIterator из предыдущего примера.
gen_iter = simple_generator(6)

"""
    List comprehension
В русской терминологии нет общепризнанного перевода list comprehension.
Гугл его переводит как списковое включение или абстракция списков.
Хотя наиболее часто можно встретить фразу генератор списков,
но мне кажется это не совсем правильно, так как в Python есть отдельное понятие генератора.
По моему, возможно наиболее подходящий перевод был бы представление списков.
"""
some_list = [1, 2, 3, 4]
new_list = [x ** 2 for x in some_list if x % 2 == 0]  # представление списка
# print(new_list)

new_generator = (x ** 2 for x in some_list if x % 2 == 0)  # выражение - генератор
new_generator_list = []

for x in new_generator:
    if x % 2 == 0:
        x *= 2
        new_generator_list.append(x)

# print(new_generator_list)


sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

"""
    Лябда функции(однострочные функции)
lambda x: x

приведенном выше примере выражение состоит из:
Ключевое слово: lambda
Связанная переменная: x
Тело: х

(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3

Лямбда-функция является выражением, оно может быть именована,
поэтому вы можете написать предыдущий код следующим образом:
"""
add_one = lambda x: x + 1
add_one(2)  # 3


# Вышеупомянутая лямбда-функция эквивалентна написанию этого:
def add_one(x):
    return x + 1


new_some_list = [1, 2, 3]

# some_gen = lambda: x for x in new_some_list
# print(some_gen)

"""
    map

Функция map применяет функцию к каждому элементу последовательности и возвращает итератор с результатами.
Например, с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:
"""
list_of_words = ['one', 'two', 'list', '', 'dict']
list_of_words = list(map(str.upper, list_of_words))

# или вычислить число в какой либо степени с помощью pow()
print(list(map(pow, [1, 2, 3], [11, 22, 33])))

# тоже самое с помощью цикла
some_list = []
for x, y in zip([1, 2, 3], [11, 22, 33]):
    some_list.append(pow(x, y))
print(some_list)


# Также мы можем использовать в map свои функции

def convert_to_str(x):
    return str(x)


print(list(map(convert_to_str, [lambda x: x in new_some_list])))

# или можем использовать встроенную функцию питона
print(list(map(str, [lambda x: x in new_some_list])))


"""
  П/З
  
1 Создать функцию которая принимает два аргумента и возвращает их сумму c помощью lambda
2 c помощью map использовать функцию для каждого элемента списка some_list
3 с помощью iter() проитерировать и печатать каждый элемент при вызове next()
# результат вывода будет примерно таким: 2, 16, 30, 44, 58, 72, 86, 100, 114, 128, 142, 156, 170, 184, 198...

"""
some_list = range(1, 1000, 7)

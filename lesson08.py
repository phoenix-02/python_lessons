# Итераторы

num_list = {1, 2, 3, 4, 5}


for i in num_list:
    print(i)


# Объекты, элементы которых можно перебирать в цикле for, содержат в себе объект итератор,
# для того, чтобы его получить необходимо использовать функцию iter(),
# а для извлечения следующего элемента из итератора – функцию next().

itr = iter(num_list)
print(next(itr)) #1
print(next(itr)) #2
print(next(itr)) #3
print(next(itr)) #4
print(next(itr)) #5

# print(next(itr))

# Traceback (most recent call last):
#   File "C:/Users/mango/PycharmProjects/python-lessons/lesson08.py", line 18, in <module>
#     print(next(itr))
# StopIteration


# Создание собственных итераторов


# Создадим класс, объект которого будет итератором, выдающим определенное количество единиц,
# которое пользователь задает при создании объекта.
# Такой класс будет содержать конструктор, принимающий на вход количество единиц и метод __next__(),
# без него экземпляры данного класса не будут итераторами.
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


#
s_iter1 = SimpleIterator(3)


print(next(s_iter1))
print(next(s_iter1))
print(next(s_iter1))
# print(next(s_iter1))


# Генераторы


# Генераторы позволяют значительно упростить работу по конструированию итераторов.
# В предыдущих примерах, для построения итератора и работы с ним, мы создавали отдельный класс.
# Генератор – это функция, которая будучи вызванной в функции next()
# возвращает следующий объект согласно алгоритму ее работы. Вместо ключевого слова return
# в генераторе используется yield


def simple_generator(val):
    while val > 0:
        val -= 1
        yield val


gen_iter = simple_generator(6)

# Данная функция будет работать точно также, как класс SimpleIterator из предыдущего примера.


some_list = [1, 2, 3, 4]
new_list = [x ** 2 for x in some_list if x % 2 == 0]  # генератор списка
print(new_list)

new_generator = (x ** 2 for x in some_list if x % 2 == 0)  # выражение - генератор
new_generator_list = []

for x in new_generator:
    print(x)
    new_generator_list.append(x)

print(new_generator_list)


# Лябда функции(однострочные функции)
# lambda x: x

# приведенном выше примере выражение состоит из:
# Ключевое слово: lambda
# Связанная переменная: x
# Тело: х

# (lambda x: x + 1)(2) = lambda 2: 2 + 1
#                      = 2 + 1
#                      = 3

# Поскольку лямбда-функция является выражением, оно может быть именована.
# Поэтому вы можете написать предыдущий код следующим образом:
# add_one = lambda x: x + 1
# add_one(2)
# 3
# Вышеупомянутая лямбда-функция эквивалентна написанию этого:
def add_one(x):
    return x + 1


new_some_list = [1, 2, 3]

# some_gen = lambda: x for x in new_some_list
# print(some_gen)


# map

# Функция map применяет функцию к каждому элементу последовательности и возвращает итератор с результатами.
# Например, с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:
list_of_words = ['one', 'two', 'list', '', 'dict']
list_of_words = list(map(str.upper, list_of_words))

# или вычислить число в какой либо степени с помощью pow()
print(list(map(pow, [1, 2, 3], [11, 22, 33])))

# тоже самое с помощью цикла
some_list = []
for x,y in zip([1,2,3],[11,22,33]):
    some_list.append(pow(x,y))
print(some_list)


# Также мы можем использовать в map свои функции

def add_2(x):
    return str(x)

print(list(map(add_2, [lambda x: x in new_some_list])))

# П\З
# 1 Создать функцию которая принимает два аргумента и возвращает их сумму c помощью lambda
# 2 c помощью map использовать функцию для каждого элемента списка some_list
# 3 с помощью iter() проитерировать и печатать каждый элемент при вызове next()
some_list = range(1, 1000, 7)

# результат вывода будет примерно таким: 2, 16, 30, 44, 58, 72, 86, 100, 114, 128, 142, 156, 170, 184, 198...
print(list(map(lambda x,y:x+y,some_list, some_list )))





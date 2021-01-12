# Урок 6
########

# Работа с модулями

# import our_module
#
# print(sys.path)
# sys.path.append('C:/Users/mango/PycharmProjects/python-lessons')
# y = input('введите')
# our_module.new_func(y)

# import our_module
# import wrongmodule
# os.oprst()
# our_module.sum(6, 666)

# l = dir(our_module)
# print(l)
# import builtins  # встроенные, всегда доступные ф-ии
# print(dir(builtins))

# import pyautogui as gui
# import our_module as om
# import our_module
#
#
# om.sum(123,123)
# our_module.sum(123,123)

# from os import listdir as spisok_faylov
# spisok = spisok_faylov('lesson05_data')
# print(spisok)
# ['users', 'test.txt', 'data.pickle', 'data.json']
#
# from our_module import sum as summa
# summa(1,1)
# sum2('12','123')
# from our_module import *
# our_module.sum
# sum()
# sum2()
# sum(3, 4)
# test_method()
# import our_module as om

# from our_module import *
# module_test()

# Пакеты модулей - Packages

# from our_package import submodule
# from our_package import *  # указанные в __all__
# submodule.sub_test()
# other_module.method_of_other_module()
# import our_package as p
# print(dir(p))
# p.subpackage.subsubmodule.subsubtest()
# import lesson05_data as p




# from mymath import our_module as om
# om.os.listdir()
# print(dir(ss))
# ss.subsubtest()


# пз - создать пакет mymath, добавить в него подпакет operations
# в operations должны быть модули arithmetic с ф-ями add/subtract, trigonometric c ф-ями sin/cos
# sin = a/c
# cos = b/c
#            /|
#         c / |
#          /  | a
#         /___|
#           b
# также добавить в пакет mymath модуль other c ф-ями min, max, round
# # Должен нормально отрабатывать следующий код:
# from mymath import other
# other.round()
# import mymath as m
# m.operations.arithmetic.add()
# import mymath.operations.trigonometric as trig
# trig.sin()
#
# a = 3
# b = a
# c = a
# a = 'hello'
# print(a)

# import keyword
# import builtins #показти список вбудованих функціцй
# print(keyword.kwlist)
# print(dir(builtins))

# x = '5.4'
# x = float (x)
# print(type (x))

# x = 10
# y = 10
# print(id(x))
# print(x is y)

# a, b, c = 4 #множинне присвоення
# x, y = 2, 3 #множинне присвоення

# a = bool('')
# print(a)
# b = bool(0)
# print(b)
# c = bool('d')
# print(c)

# z = 3 + 2 #лівий і правий операнти

# x = -6 //4
# print(x)

# x = 1
# x = x + 1
# print(x)

# z = 1 + 3 #бінарний оператор
# y = -z #унарний оператор

# z = 24 / 6 / 3 #операція відбувается з ліван на право

# # Аналогічний запис
# y = (1 + 2 + 3 + 4)
# print(y)
#
# z = 1 + 2 + \ #перніс на наступний рядок
#     3 + 4
# print(z)


# a = int(input('Введіть двозначнне число:'))
# print(a//10) #перше число
# print(a%10) #друге число

# a = int(input('Введіть тризначне число:'))
# first = (a//100)
# second = (a//10%10)
# third = (a%10)
# print(first)
# print(second)
# print(third)
# print(first + second + third)

# a = int(input('Введіть число 1:'))
# b = int(input('Введіть число 2:'))
# print(f'{a}{b}')


# c = int(input('введіть температуру в цельсії:'))
# f =c * 9/5 + 32
# print (f'{c} --> {f} {int(f)}' )


# import math
# x = math.pi
# y = math.cos(x)
# print(y)
# print(x)

# from math import * #імпорт всіх функцій
# x=pi
# print(x)


from math import log, e, exp, sqrt

x = 1
y = 2
F = (3 * y**2+sqrt(y+1)) / (log(x+y)+exp(x))
Y = round(F, 2)
print(F)
print(Y)
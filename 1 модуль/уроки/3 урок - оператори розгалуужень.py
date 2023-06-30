# # логічні вирази та оператори
# books = 5
# print(books < 1)
# print(books >= 3)
# cond = books < 1
# print(cond)

#                логічні операції

# not - заперечення
# and  - логічне 'і' або конюкція
# or - логічне або або дизюнкція
# is -

# Пріорітет операцій: not, and, or

# 3>1 and 2==5
# 3>1 or 2==5
# print(not 3<1)

# x = 1
# # y = x < 5
# y = x != 3
# print(y)

# x > 0 and x < 5
# 0 <= x <= 5

# x = True
# y = z = 1
# flag = x == 1 and not 2*3 < 2 and 'a' < 'z' or y is not z
# print(flag)


# a = int(input('ведіть число a: '))
# b = int(input('ведіть число b: '))
# c = int(input('ведіть число c: '))
#
# flag = (a < b and b < c) or (c < b and c < a)
# print(flag)


# year = int(input('ведіть рік: '))
# res = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)      # рік ділиться на 4 and не ділиться на 100 or ділиться на 400
# # print(res)
#
# if year == True:
#     print('Рік високосний')
# else:
#     print("Невисокосний рік")

# x = 5
# y = 7
# if x > y:
#     print('x is greeater')
#     x = x - y
# else:
#     print('x <= y')
#     x = x + y
# print('x =', x)

# множинне (каскадне) галуження if, elif, else

# x = 5
# y = 5
# if x > y:
#     print('x is greeater')
#     x = x - y
# elif x < y:
#     print('x <= y')
#     x = x + y
# elif x == y:
#     print('x is equal to y')
#
# print('x =', x)

# month = int(input('Введіть номер місяця: '))
# if month == 1 or month == 2 or month == 12:
#     massage = 'Зима'
# elif month == 3 or month == 4 or month == 5:
#     massage = 'Весна'
# elif month == 6 or month == 7 or month == 8:
#     massage = 'Літо'
# elif month == 9 or month == 10 or month == 11:
#     massage = 'Осінь'
# else:
#     massage= 'Такої пори року немає'
#
#
# print(f'{month} місяць це - {massage}')

x = 2 if 3 < 1 else 5
print(x)

# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# c = int(input("Введіть трете число: "))
# print()
# print('''Якщо хочете отримати суму трьох чисел введіть - 1
# Якщо хочете отримати добуток трьох чисел введіть - 2''')
# print()
# d = int(input('Яку операцію ви хочете виконати, введіть число: '))
# print()
# if d == 1:
#     print(f'Суму трьох чисел = {a + b + c}')
# elif d == 2:
#     print(f'Добуток трьох чисел = {a * b * c}')
# else:
#     print('Ви ввели некоректне число для виконання операції')
#
# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# c = int(input("Введіть трете число: "))
# print()
# print('''Якщо хочете отримати максимальне число із трьох введіть - 1
# Якщо хочете отримати мінімальне число із трьох введіть - 2
# Якщо хочете отримати середньоарифметичне трьох чисел введіть - 3''')
# print()
# d = int(input('Яку операцію ви хочете виконати, введіть число: '))
# print()
# if d == 1:
#     print(f'Максимальне число із трьох = {max(a, b, c)}')
# elif d == 2:
#     print(f'Мінімальне число із трьох = {min(a, b, c)}')
# elif d == 3:
#     print(f'Середньоарифметичне трьох чисел = {round((a + b + c) / 3, 2)}')
# else:
#     print('Ви ввели некоректне число для виконання операції')
#
# meter = int(input('Введіть кількість метрів: '))
# print()
# print('''Якщо хочете отримати результат у милях введіть - 1
# Якщо хочете отримати результат у дюймах введіть - 2
# Якщо хочете отримати результат у ярдах введіть - 3''')
# print()
# d = int(input('Яку операцію ви хочете виконати, введіть число: '))
# print()
# if d == 1:
#     print(f'{meter} метр = {meter * 0.000621371} милі')
# elif d == 2:
#     print(f'{meter} метр = {meter * 39.3701} дюйма')
# elif d == 3:
#     print(f'{meter} метр = {meter * 1.09361} ярди')
# else:
#     print('Ви ввели некоректне число для виконання операції')

# date_number = int(input('Введіть номер дня тижня, від 1 до 7: '))
# if date_number == 1:
#     print("Понеділок")
# elif date_number == 2:
#     print("Вівторок")
# elif date_number == 3:
#     print("Середа")
# elif date_number == 4:
#     print("Четвер")
# elif date_number == 5:
#     print("Пʼятниця")
# elif date_number == 6:
#     print("Субота")
# elif date_number == 7:
#     print("Неділя")
# else:
#     print('У неділі всьго сім днів, перезапустіть додаток і ведіть число від 1 до 7')

# month = int(input('Введіть номер місяця, від 1 до 12: '))
# if month == 1:
#     print("Січень")
# elif month == 2:
#     print('Лютий')
# elif month == 3:
#     print('Березень')
# elif month == 4:
#     print('Квітень')
# elif month == 5:
#     print('Травень')
# elif month == 6:
#     print('Червень')
# elif month == 7:
#     print('Липень')
# elif month == 8:
#     print('Серпень')
# elif month == 9:
#     print('Вересень')
# elif month == 10:
#     print('Жовтень')
# elif month == 11:
#     print('Листопад')
# elif month == 12:
#     print('Грудень')
# else:
#     print('Такого місяця не існуе')

# number = int(input('Введіть число: '))
# if number > 0:
#     print('Number is positive')
# elif number < 0:
#     print('Number is negative')
# elif number == 0:
#     print('Number is equal to zero')

number1 = int(input('Введіть перше число: '))
number2 = int(input('Введіть друге число: '))
res = number1 == number2

if res == False:
    print(f'{min(number1, number2)} {max(number1, number2)}')
else:
    print('Числа рівні')

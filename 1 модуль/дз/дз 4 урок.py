# number = int(input('Введіть ціле чотиризначне число: '))
#
# while number < 1000:
#     print(f'Помилка, число {number} не чотиризначне!')
#     number = int(input('Введіть ціле чотиризначне число: '))
#
#     number1 = number // 1000
#     number2 = number // 100 % 10
#     number3 = number // 10 % 10
#     number4 = number % 10
#
# if (number1 + number2) == (number3+number4):
#         print(f'{number} — щасливе число, оскільки {number1} + {number2} = {number3} + {number4}')
# else:
#         print(f'{number} — нещасливе число.')

# height = float(input('Введіть зріст (у метрах): '))
# weight = float(input('Введіть масу тіла (у кілограмах): '))
# mass_body_index = round((weight / (height * height)), 2)
#
# if mass_body_index < 18.5:
#     print(f'Your body mass index is: {mass_body_index}, that is underweight.')
# elif 18.5 <= mass_body_index <= 24.9:
#     print(f'Your body mass index is: {mass_body_index}, that is normal weight.')
# else:
#     print(f'Your body mass index is: {mass_body_index}, that is overweight.')


# number_software_packages = int(input('Введіть кількість придбаних комплектів програмного забезпечення: '))
# print('''Напишіть любий символ окрім цифри 0, якщо у Вас є карта постійного клієнта.
# Якщо у Вас немає карти постійного клієнта, залиште данній рядок порожній.
#  ''')
# loyalty_card = input('Введіть символ: ')
#
#
# discount = 0
# if number_software_packages >= 10 and number_software_packages < 20:
#     discount = 10
# elif number_software_packages >= 20 and number_software_packages < 50:
#     discount = 20
# elif number_software_packages >= 50 and number_software_packages < 100:
#     discount = 30
# elif number_software_packages >= 100:
#     discount = 40
#
# if loyalty_card:
#     print(f'Cума знижки за {number_software_packages} пакет ПО становить {0}, загальну суму становить {number_software_packages * 1000}')
# elif loyalty_card != '' and discount == 10:
#     print(f'Cума знижки за {number_software_packages} пакет ПО становить {(number_software_packages * 1000) * 0.1}, загальну суму становить {(number_software_packages * 1000) - ((number_software_packages * 1000) * 0.1)}')
# elif loyalty_card != '' and discount == 20:
#     print(f'Cума знижки за {number_software_packages} пакет ПО становить {(number_software_packages * 1000) * 0.2}, загальну суму становить {(number_software_packages * 1000) - ((number_software_packages * 1000) * 0.2)}')
# elif loyalty_card != '' and discount == 30:
#     print(f'Cума знижки за {number_software_packages} пакет ПО становить {(number_software_packages * 1000) * 0.3}, загальну суму становить {(number_software_packages * 1000) - ((number_software_packages * 1000) * 0.3)}')
# elif loyalty_card != '' and discount == 40:
#     print(f'Cума знижки за {number_software_packages} пакет ПО становить {(number_software_packages * 1000) * 0.4}, загальну суму становить {(number_software_packages * 1000) - ((number_software_packages * 1000) * 0.4)}')
# else:
#     print(f'Cума знижки за {number_software_packages} пакет ПО становить {100}, загальну суму становить {900}')


# k = int(input('Введіть день року: '))
# day = (k - 1) % 7 #range(6, 255, 7)) range(7, 255, 7))
# if day == 5 or day == 6:
#     massage = 'Вихідний'
# else:
#     massage = 'Робочий день'
#
# print(massage)

# a = int(input("Введіть перше ціле число a: "))
# b = int(input("Введіть друге ціле число b: "))
#
# if a < b:
#     if a % 2 == 0:
#         start = a
#     else:
#         start = a + 1
#     step = 2
#     end = b + 1
# else:
#     if a % 2 == 0:
#         start = a
#     else:
#         start = a - 1
#     step = -2
#     end = b - 1
#
# for num in range(start, end, step):
#     print(num, end = ' ')

# n = int(input("Введіть ціле число n в діапазоні від 1 до 1000: "))
# summ = 0
# quantity = 0
# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         summ += i
#         quantity += 1
#         print(i, end=' ')
#
# print()
# print(f'''сумa = {summ}
# кількість цих чисел = {quantity}''')


# print('Програмп підраховує додатні і від’ємні числа, а також нулі, для зупинки підрахунку чисел введіть команду "stop"')
#
# positive = 0
# negative = 0
# zero = 0
#
# while True:
#     inp = input('Введіть 0, додатне або від’ємні числачисло: ')
#     if inp == 'stop':
#         break
#
#     number = int(inp)
#
#     if number > 0:
#         positive += 1
#     elif number < 0:
#         negative += 1
#     else:
#         zero += 1
#
# print(positive, negative, zero, end=' ')


# n = int(input('Введіть n чисел, кількість цілих чисел яку Ви хочете обробити: '))
# count_zero = 0
# max_number = 1
#
# for i in range(n):
#     numbers = int(input("Введіть число: "))
#     if numbers == 0:
#         count_zero += 1
#
#     if numbers > max_number:
#         max_number = numbers
#
# print(f'Кількість цифр які дорівнюють нулю = {count_zero}')
# print(f'Максимальне із цих чисел = {max_number}')

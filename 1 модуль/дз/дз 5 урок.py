# first_number = int(input('Введіть перше число: '))
# second_number = int(input('Введіть друге число: '))
#
# sum_even_num = 0
# count_even_num = 0
# sum_not_even_num = 0
# count_not_even_num =0
# sum_multiples_9 = 0
# count_multiples_9 = 0
#
# for i in range(first_number, second_number+1):
#     if i % 2 == 0:
#         sum_even_num += i
#         count_even_num += 1
#
#     if i % 2 != 0:
#         sum_not_even_num += i
#         count_not_even_num += 1
#
#     if i % 9 == 0:
#         sum_multiples_9 += i
#         count_multiples_9 += 1
#
#
# print(f'Cуму парних чисел: {sum_even_num}, середнє арифметичне {sum_even_num/count_even_num}')
# print(f'Cуму непарних чисел: {sum_not_even_num}, середнє арифметичне {sum_not_even_num/count_not_even_num}')
# print(f'Cуму непарних чисел: {sum_multiples_9}, середнє арифметичне {sum_multiples_9/count_multiples_9}')

# n = int(input('Введіть довжину лінії: '))
# symbol = input('Введіть символі: ')
#
# for i in range(n):
#     print(symbol)

# while True:
#     n = int(input('Enter a number: '))
#     if n == 7:
#         break
#
#     if n > 0:
#         print(f'Number {n} is positive')
#
#     if n < 0:
#         print(f'Number {n} is negtive')
#
#     if n == 0:
#         print(f'Number {n} is equal to zero')
#
# print('Good bye!')

# summ = 0
# max_num = None
# min_num = None
# while True:
#     n = int(input('Enter a number: '))
#     if n == 7:
#         break
#
#     if n:
#         summ += n
#     if min_num is None or min_num < n:
#         min_num = n
#
#     if max_num is None or max_num > n:
#         max_num = n
#
# print(f'Сума введених чисел: {summ}')
# print(f'Максимальне число: {max_num}')
# print(f'Мінімальне число: {min_num}')
# print('Good bye!')

# x = int(input('Введіть число х: '))
# n = int(input('Введіть число n: '))
#
# degree = 1
# for i in range(1, n+1):
#     degree *= x
#
# print()
# print(f'{x} в степені {n} = {degree}')

# a = int(input('Введіть число a: '))
# b = int(input('Введіть число b: '))
# count = 0
# for i in range(a, b + 1):
#     digit1 = i // 100
#     digit2 = (i // 10) % 10
#     digit3 = i % 10
#
#     if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
#         count += 1
#
# print(f'Кількість цілих чисел у діапазоні від {a} до {b} включно, в яких є дві однакові цифри = {count}')

# n = int(input('Введіть кількість днів роботи системи: '))
# errors = 0
# error_free_days = 0


# for i in range(n):
#     m = int(input(f'Введіть кількість помилок у {i+1} день: '))
#     errors += m
#
#     if m == 0:
#         error_free_days += 1
#
# print(f'Загальна кількість помилок: {errors}')
# print(f'Кількість днів без помилок: {error_free_days}')


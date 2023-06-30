# n = int(input('Введіть довжину лінії: '))
# symbol = input('Введіть символі: ')
# #
# # for i in range(n-1):
# #     print(symbol, end='-')
# # print(symbol)
#
# # аналогічно
# for i in range(n):
#     if i != n-1:
#         print(symbol, end='-')
#     else:
#         print(symbol)
#
# # аналогічно
# for i in range(n):
#     if i != n-1:
#         print(symbol, end='-')
#         continue
#     print(symbol)

## 2 step

# n = int(input('Введіть число: '))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#
# print(factorial)

## методом while
# n = int(input('Введіть число: '))
# d = 1
# i = 1
# while i <= n:
#     d = d * i
#     print(i, d)
#     i = i + 1
#
# print(f'{n}! = {d}')


# import random
#
# random_number = random.randint(1, 50)
# # random_number = 5
#
# count = 0
# while True:
#     number = int(input('Введіть число: '))
#     count += 1
#
#     if number == 0:
#         print(f'Ви програли, кількість спроб = {count}')
#         break
#
#     if number == random_number:
#         print(f'Ви вгадали число, кількість спроб = {count}')
#         break
#
#     elif number < random_number:
#         print('Число більше')
#
#     elif number > random_number:
#         print('Число менше')
#
# import random
#
# random_number = random.randint(1, 50)
# # random_number = 5
#
# count = 0
# while True:
#     number = int(input('Введіть число: '))
#     count += 1
#
#     if number == 0:
#         print(f'Ви програли, кількість спроб = {count}')
#         break
#
#     if number == random_number:
#         print(f'Ви вгадали число, кількість спроб = {count}')
#         break
#
#     elif number < random_number:
#         print('Число більше')
#
#     elif number > random_number:
#         print('Число менше')

## підрахунок середньої оціни

# n = int(input('Введіть число: '))
# s = 0
# count = 0
# for i in range(n):
#     while True:
#         score = int(input(f'Введіть оцінку {i+1}: '))
#         if 0 < score <= 5:
#             break
#         print('Введіть оцінку від 1 до 5')
#
#     s = s+score
#     if score < 3:
#         count = count + 1 #кількысть незадовыльних оцынок (2 і нижче)
#
# print(f'Середня оцінка: {s/n}')
# print(f'Кількість незадовільних оцінок {count}')

## 5 завдання
# sum_digits = 0
# count_digits = 0
# sum_not_digits = 0
# count_not_digits = 0
# min_value = None
# min_count = 0
#
# output = ''
# while True:
#     x = int(input('Введіть ціле число: '))
#     if x == 0:
#         print('Bye!')
#         break
#
#     if x // 10 == 0:
#         print(f'number {x} is digit')
#         sum_digits += x
#         count_digits += 1
#     else:
#         print(f'number {x} is not digit')
#         sum_not_digits += x
#         count_not_digits += 1
#     if min_value is None or min_value > x:
#         min_value = x
#         min_count = 1
#     elif min_value == x:
#         min_count += 1
#
#     output = output + ' ' + str(x)
#
# avg_digits = sum_digits / count_digits if count_digits != 0 else 0
# avg_not_digits = sum_not_digits / count_not_digits if count_not_digits != 0 else 0
#
# print(output)
# print(f'Cередне арефметичне введених цифр {avg_digits}')
# print(f'Cередне арефметичне введених не цифр {avg_not_digits}')
# print(f'Мінімальне із введених чисел {min_value}, Кількість чисел які є мінімальними {min_count}')

## 6 task
# n = 12345
# count = 0
# d = 1
# while n > 0:
#     i = n % 10  # бере остане число
#     print(i)
#     count += 1
#     d *= i
#     n = n // 10  # забирае остане число
#
# print(f'Кількість цифр = {count}')
# print(f'Добуток цифр = {d}')

n = 153456
m = n
count = 0
while n > 0:
    i = n % 10  # бере остане число
    print()
    print(f'i={i}')
    print()
    m = n // 10
    while m > 0:
        j = m% 10
        print(i,j)
        if i == j:
            print('Числа однакові')
            count += 1
        m = m//10


    n = n // 10  # забирае остане число

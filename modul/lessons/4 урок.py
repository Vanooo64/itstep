## визначає чи є день понеділком

# k = int(input('Введіть день року: '))
# if k % 7 == 2: #((k -2)% 7 == 2)
#     massage = 'Понеділок'
# else:
#     massage = 'Не є понеділок'
#
# print(massage)

# 2 task

# n = int(input('Введіть двоцифрове число: '))
# first = n // 10
# second = n % 10
# summa = first + second
# flag = True if (summa // 10 == 1) else False #аналогычно True if (summa // 10) else False
# print(f'Двоцифрова сумма: {flag}')

# n = int(input('Введіть двоцифрове число: '))
# first = n // 10
# second = n % 10
# summa = first + second
# flag = bool (summa//10)
# print(f'Двоцифрова сумма: {flag}')

# num1 = int(input('Введіть перше число: '))
# num2 = int(input('Введіть друге число: '))
# num3 = int(input('Введіть трете число: '))
#
# if num1 == num2 == num3:
#     print('3')
# elif num1==num2 or num1==num3 or num2 == num3:
#     print('2')
# else:
#     print('0')

# Завдання 4. В університеті використовується наступна шкала для інтерпретації результатів тестування студентів:
# 90 балів і вище (A), 80-89 (B), 70-79 (C), 60-69 (D), 50-59 (E), нижче 50 (F). Напишіть програму, яка дозволить
# студенту ввести тестовий бал, а потім відобразити оцінку для цього балу. Якщо користувач ввів некоректне число,
# виведіть повідомлення про помилку.

# a = int(input('Введіть кількість годин: '))
# b = float(input('Введіть заробітну плату за годину: '))
# if a <= 40:
#     print(f'Заробітна плата становить: {a * b}')
# elif a > 40:
#     print(f'Заробітна плата становить: {((a - 40) * (b * 1.5)) + (40 * b)}')

# тернарний оператор
# hours = int(input('Введіть кількість годин: '))
# rate = float(input('Введіть заробітну плату за годину: '))
#
# total_pay = (hours * rate) if (hours <= 40) else ((hours - 40) * hours * 1.5) + (40 * hours)
# print(f'Заробітна плата становить: {total_pay}')


#           цикл while

# x = 5
# while x < 25:
#     x = x + 4
# print(f'x = {x}')
#
# x = 0
# while x < 10:
#     x = x + 1
#     print(f'x = {x}', end = ", ")

# x = 0
# while x < 10:
#     if x == 2:
#         x = x + 1
#         continue
#     print(f'x = {x}', end=", ")
#     x = x + 1
#
# else:
#     print()
#     print('Цикл виконовся успішно')
#
# print(x)


# x = 0
# while x < 10:
#     if x == 2:
#         x = x + 1
#         break
#     print(f'x = {x}', end=", ")
#     x = x + 1
#
# else:
#     print()
#     print('Цикл виконовся успішно')
#
# print(x)

# x = 0
# while True:
#     print(f'x = {x}', end=", ")
#     x = x + 1
#     if x == 3:
#         break
# else:
#     print()
#     print('Цикл виконовся успішно')
#
# print(x)


# for i in range(1, 10, 2): #не обовʼязково задавати крок (за замовченням 1), необовʼязково задавати перше число за замовченням 0
#     print(i)

# n = int(input('Enter n = '))
# s = 0
# for i in range(n):
#     x = int(input(f'Enter x_{i+1}= '))
#     s = s + x
#
# print(f'suma = {s}')

# n = int(input('Enter n = '))
# s = 0
# for i in range(1,n + 1):
#     x = int(input(f'Enter x_{i}= '))
#     s = s + x
#
# print(f'suma = {s}')


# n = int(input('Enter n = '))
# s = 0
#
# for i in range(1,n + 1):
#     x = int(input(f'Enter x_{i}= '))
#     if i == 1:
#         max_value = x
#     if x > max_value:
#         max_value = x
#
#     s = s + x
#
# print(f'suma = {s}')
# print(f'max_value = {max_value}')

# n = int(input('Enter n = '))
#
# i = 1
# s = 0
# while i <= n:
#     if (i % 10 == 1) and (i % 3 == 0):
#         print(i, end=" ")
#         s += i
#     i = i + 1
#
# print(s)

# n = int(input('Enter n = '))
#
# s = 0
# for i in range(1, n + 1):
#     if (i % 10 == 1) and (i % 3 == 0):
#         print(i, end=' ')
#         s = s + 1
#
# print()
# print(f's = {s}')

# ## 2 tasc
# a = 3
# b = 7
# start = min(a, b) + 1
# end = max(a, b)
#
# s = 0
# count = 0
#
# for i in range(start, end):
#     print(i, end=' ')
#     s += i
#     count += 1
#
# print()
# print(f's = {s}')
# print(f'count = {count}')
# print(f'avg = {s / count}')

task 5

count = 0
while True:
    x = int(input('Enter x = '))
    if x % 2 == 0 and x != 0:
        count = count + 1

    if x == 0:
        break
print(f'count = {count}')
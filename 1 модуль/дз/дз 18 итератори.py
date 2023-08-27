# # Завдання 1
# # Створіть функцію-генератор, яка повертає всі непарні числа в діапазоні від a до b включно. Функція приймає
# # початок і кінець діапазону як параметри. Протестуйте роботy функції-генератора в дії
#
# def func_generator(a, b):
#     res = (i for i in range(a, b+1) if i % 2 != 0)
#     return res
#
# result = func_generator(1, 11)
# print(type(result))
# print(*result)

# # Завдання 2.
# # •	Побудуйте ітератор за допомогою генератор-функції, який буде перебирати всі парні числа в діапазоні від start до end включно з деяким кроком step.
# # •	*Побудуйте ітератор за допомогою генератор-виразу, який буде перебирати всі парні числа в діапазоні від start до end включно з деяким кроком step.
# # •	(x for i, x in enumerate(start, end, step) if i step)
# #
# # Приклади:
# # start=2 end=52 step=1  ->  2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52
# # start=2 end=52 step=2 ->   2 6 10 14 18 22 26 30 34 38 42 46 50
# # start=1 end=53 step=5 ->   2 12 22 32 42 52
#
# def even_num_generator(start, end, step):  # •	Побудуйте ітератор за допомогою генератор-функції, який буде перебирати всі парні числа в діапазоні від start до end включно з деяким кроком step.
#     current = start if start % 2 == 0 else start+1
#     while current <= end:
#         yield current
#         current += step * 2
#
# start, end, step = 2, 52, 1
# generator = even_num_generator(start, end, step)
# print(*generator)
#
# start, end, step = 2, 52, 2
# generator = even_num_generator(start, end, step)
# print(*generator)
#
# start, end, step = 2, 52, 5
# generator = even_num_generator(start, end, step)
# print(*generator)
#
# start = int(input("Введіть початкове число: "))   # •	*Побудуйте ітератор за допомогою генератор-виразу, який буде перебирати всі парні числа в діапазоні від start до end включно з деяким кроком step.
# end = int(input("Введіть кінцеве число: "))
# step = int(input("Введіть крок: "))
#
# iter_gen = (x for x in range(start, end+1, step*2) if x % 2 == 0)
# print(*iter_gen)


# # Завдання 3.
# # Напишіть функцію-генератор для генерації послідовності всіх цілих додатних чисел менших за певне задане
# # число n, які діляться на 3 або на 5. Протестувати роботу за допомогою циклу.
#
# def generation_smaller_number(n):
#     curret = 1
#     while curret < n:
#         if curret % 3 == 0 or curret % 5 == 0:
#             yield curret
#         curret += 1
#
#
# n = int(input("Введіть число n: "))
# res = generation_smaller_number(n)
# for i in res:
#     print(i, end= ' ')


# # Завдання 4.
# # 1.	Написати безкінечний генератор послідовності простих чисел. Створити об’єкт цієї генератор-функції
# # та перебрати 10 перших елементів послідовності за допомогою функції next. Перебрати ці елементи іншим
# # способом без next за допомогою циклу for і break.
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# def prime_generator():
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
#
# # Створення генератора простих чисел
# primes = prime_generator()
# primes1 = prime_generator()
#
# # Вивід послідовності простих чисел
# for _ in range(10):  # Виводимо перші 10 простих чисел
#     print(next(primes))
#
# # Перебір перших 10 простих чисел за допомогою циклу for і break
# count = 0
# for i in primes1:
#     print(i)
#     count+=1
#     if count == 10:
#         break

# 2.	Створіть функцію-генератор, яка генерує усі прості числа менші за певне задане число. Протестувати
# роботу ітератора, що повертає дана функція-генератор

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def gen_prime_numbers(n):
    for i in range(1, n):
        if is_prime(i):
            yield i

res = gen_prime_numbers(40)
print(*res)


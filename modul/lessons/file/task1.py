# Завдання 1
#
# Напишіть програму для запису послідовності у текстовий файл і зчитування її з файлу.
#
# Вхідні дані:
# Python Ruby C++ C Java Go JavaScript
# Вихідні дані:
# Файл output.txt з вмістом
#
# Python
# Ruby
# C++
# C
# Java
# Go
# JavaScript
#
# # 1 спосіб запис файлу
# strg = 'Python Ruby C++ C Java Go JavaScript'.split()
# print(strg)
#
# file = open('output.txt', mode='w') #відкривае фйл на запис
# for row in strg:
#     file.write(f'{row} \n')
#
# file.close()
#
#
# # 2 спосіб запис файлу
# strg = 'Python Ruby C++ C Java Go JavaScript'.split() #['Python', 'Ruby', 'C++', 'C', 'Java', 'Go', 'JavaScript']
# print(strg)
#
# strq2 = [x+'\n' for x in strg]
# print(strq2) # ['Python\n', 'Ruby\n', 'C++\n', 'C\n', 'Java\n', 'Go\n', 'JavaScript\n']
#
# file = open('output.txt', mode='w') #відкривае
# file.writelines(strq2)
# file.close()
#
# # Зчитування файлу
# filу = open('output.txt', mode='r')
# read = filу.read()
# print(read)
#
# # Зчитування файлу а допомогою менеджера with
# with open('output.txt', mode='r') as file:
#     read = file.read()
#     print(read)
#
# # # Зчитування файлу за допомогою менеджера with (зчитае перші 5 символів, нумерація починаеться з 0)
# with open('output.txt', mode='r') as file:
#     read = file.read(5)
#     print(read)
#
# # # Зчитування файлу за допомогою менеджера with (зчитае перші 5 символів, нумерація починаеться з 0)
# with open('output.txt', mode='r') as file:
#     read = file.read(15)
#     print(read)
#
#     print('pos=', file.tell()) #вказуе на якій позиції зараз находиться зчитувач
#
# # # Зчитування файлу за допомогою менеджера with (зчитае перші 5 символів, нумерація починаеться з 0)
# with open('output.txt', mode='r') as file:
#     read = file.read(15)
#     print(read)
#
#     print('pos=', file.tell())  # вказуе на якій позиції зараз находиться зчитувач
#     file.seek(0) # преносить зчитувач на позицію,яка Вам потрібна
#     read = file.read()
#     print(read)
#
# # Зчитування файлу за допомогою менеджера with (зчитае перші 5 символів, нумерація починаеться з 0)
#
# from  pprint import pprint #видалить \n
# with open('output.txt', mode='r') as file:
#     for line in file:
#         pprint(line)
#
#
# with open('output.txt', mode='r') as file:
#     for line in file:
#         print(line.rstrip()) #видалить \n
#
# from pprint import pprint
# with open('output.txt', mode='r') as file:
#     lines = file.readlines() # додасть все в список
#     print(lines)
#     file.seek(0)
#     for line in file:
#         print(line.rstrip())
#
#
#
# with open('output.txt', mode='r') as file: #перебір ітератором
#     while file:
#         try:
#             line = next(file)
#             print(line.rstrip())
#         except StopIteration:
#             break
#
#
# with open('output.txt', mode='r') as file: # відкрие перші 3
#     for _ in range(3):
#         print(file.readline().rstrip())
#
# # аналогічно з функціею
# def perform(name):
#     with open(name, mode='r') as file: # відкрие перші 3
#         print(file.readable()) # перевірка на режим зчитування
#         for _ in range(3):
#             print(file.readline().rstrip())
#
# perform('output.txt')
#
#
# def perform(name):
#     with open(name, mode='r') as file, open('output3.txt', mode='w') as w_file:  # відкрие перший файл на читання, другий на запис
#         print(file.readable())  # перевірка на режим зчитування
#         for count, line in enumerate(file, 1):
#             print(f'{count}:{line.rstrip()}')
#             line = f'{count}:{line.rstrip()}\n'
#             w_file.write(line) # записуемо в другий файл
#
#
# perform('output.txt')
#
# def perform(name):
#     with open(name, mode='r') as file, open('output3.txt', mode='a') as w_file:  # відкрие перший файл на читання, другий на запис
#         print(file.readable())  # перевірка на режим зчитування
#         for count, line in enumerate(file, 1):
#             print(f'{count}:{line.rstrip()}')
#             line = f'{count}:{line.rstrip()}\n'
#             w_file.write(line) # записуемо в другий файл
#
#
# perform('output.txt')

# for i in range(1, 10):  # від 1 до 100
#     if i % 2:
#         continue
#
#     print(i, end = ' ')
#
# for i in range(101, 1,-1):  # від 100 до 1
#     if i % 2:
#         continue
#
#     print(i, end = ' ')

# task 1

# # Введіть перше число діапазону: 1
# # Введіть друге число діапазону: 10
# # Введіть число для перевіки у діапазоні: 5
# # 1 2 3 4 !5! 6 7 8 9 10

# a = int(input('Введіть перше число діапазону: '))
# b = int(input('Введіть друге число діапазону: '))

# while True:
#     namber = int(input('Введіть число для перевіки у діапазоні: '))
#     if namber > a and namber < b:
#         for i in range(a, b + 1):
#             if i == namber - 1:
#                 print(i, end=' !')
#             elif i == namber:
#                 print(i, end='! ')
#             else:
#                 print(i, end=' ')
#         break


# while (namber := int(input('Введіть число для перевіки у діапазоні: '))): #якщо 0 то False любе число True
#
#     if namber > a and namber < b:
#         for i in range(a, b + 1):
#             if i == namber - 1:
#                 print(i, end=' !')
#             elif i == namber:
#                 print(i, end='! ')
#             else:
#                 print(i, end=' ')
#         break

# 2 task
# # Введіть число: 5
# # 1
# # 22
# # 333
# # 4444
# # 55555

# n = int(input('Введіть число: '))
# for i in range(1,n+1):
#     print(str(i)*i)

# # 3 Task
# # Введіть висоту прямокутника: 4
# # Введіть ширину прямокутника: 5
# # *****
# # *****
# # *****
# # *****
# #
# #
# # *****
# # *   *
# # *   *
# # *****
#
#
#
# h = int(input('Введіть висоту прямокутника: '))
# v = int(input('Введіть ширину прямокутника: '))
# st = '*' * v
#
# for _ in range(h):
#     print(st)
#
# print()
# print()
#
# for i in range(h):
#     if i == 0 or i == h-1:
#         print(st)
#     else:
#         st1 = "*" + " " * (v-2) + "*"
#         print(st1)

# # Введіть число: 5
# # ##
# # # #
# # #  #
# # #   #
# # #    #
#
# n = int(input('Введіть число: '))
# for i in range(n):
#     st = '#' + ' '* i + '#'
#     print(st)


# n = int(input('Введіть число: '))
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             print(0, end= '\t')
#         elif i<j:
#             print(1, end="\t")
#         else:
#             print(-1, end = "\t")
#     print()

# # task 6
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # 5 x 4 = 20
# # 5 x 5 = 25
# # 5 x 6 = 30
# # 5 x 7 = 35
# # 5 x 8 = 40
# # 5 x 9 = 45
# # 5 x 10 = 50
#
# n = int(input('Введіть число: '))
# for i in range(1,11):
#     output = f'{n} x {i} = {n*i}'
#     print(output)


# task 7
# 0X	2	3	4	5	6	7	8	9
# 2	4	6	8	X0	X2	X4	X6	X8
# 3	6	9	X2	X5	X8	2X	24	27
# 4	8	X2	X6	20	24	28	32	36
# 5	X0	X5	20	25	30	35	40	45
# 6	X2	X8	24	30	36	42	48	54
# 7	X4	2X	28	35	42	49	56	63
# 8	X6	24	32	40	48	56	64	72
# 9	X8	27	36	45	54	63	72	8X
# count = 21


# count = 0
# for i in range(1, 10):
#     for j in range(1, 10):
#
#         if (i * j % 10 == 1):
#             count += 1
#             st = str(i * j // 10) + 'X'
#             print(st, end='\t')
#
#         elif (i * j // 10 == 1):
#             count += 1
#             st = 'X' + str(i * j % 10)
#             print(st, end='\t')
#
#         elif i*j % 5 == 0:
#             print('$', end='\t')
#
#         else:
#             print(i * j, end="\t")
#
#     print()
# print(f'count = {count}')

# coun = 0
# for i in range(1, 10):
#     for j in range(1, 10):
#         if j == 5 or i == 5:
#             if i * j // 10 == 1:
#                 coun += 1
#             print("$", end='\t')
#             continue
#         if j * i % 10 == 1 :
#             coun += 1
#             st = str(i * j // 10) + "X"
#             print(st, end='\t')
#             continue
#         if j * i // 10 == 1:
#             coun += 1
#             st = "X" + str(i * j % 10)
#             print(st, end='\t')
#             continue
#         print(i * j, end="\t")
#     print()
# print(f'count = {coun}')



# print('*****Старт роботи*****')
# while True:
#     print("Оберіть опцію:")
#     print("1. Конвертувати USD в UAH")
#     print("2. Конвертувати UAH в USD")
#     print("3. Вихід")
#
#     choice = input("Введіть номер опції: ")
#
#     if choice == '1':
#         usd = float(input('Введіть суму в USD: '))
#         print(f'{usd} USD = {usd*35.5}')
#
#     elif choice == '2':
#         uah = float(input('Введіть суму в UAH: '))
#         print(f'{uah} USD = {round((uah/35.5),2)}')
#
#     elif choice == '3':
#         print('Кінець роботи')
#         break
#     else:
#         print('Некоректний ввід')

d = 15
while d < 19:
    if d % 2 == 0:
        print(d)
        d += 1

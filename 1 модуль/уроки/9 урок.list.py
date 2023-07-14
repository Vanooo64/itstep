# lst = ['Sdkfksjdf', 'Sdlkfjhsldjhjlfsd', 'Sdjkfhkljshdf']
# st = " ".join(lst)
# print(st)
# print(st.split(' '))

# lst = [0] * 10
# print(lst)

# lst = list(range (3,29,5))
# print(lst)

# lst=(list('PycharmProjects'))
# print(lst)

# lst = [1, 7, 12, 3]
# lst.append(5)
# lst.extend([57,8]) #додати в кінець списка декілька символів
# print(lst, id(lst))
# lst.reverse()
# print(lst, id(lst))
#
#
# # lst.remove(7) видалить першуу ліву 7
# # del lst[1] видаляе по ындексу
# # lst.pop() видалить лстане число
# # x = lst.pop(1) видаляе по ынидексу
# # print(x)
#
# lst.sort() #сортуе у зростанні
# lst.sort(reverse=True) #сортуе на спадання
# l = lst[::-1]
# print(l)
# print(lst, id(lst))

# lst = [1, 7, 12, 3, 5, 57, 8, 8.9]
# lst1 = lst.copy #зробити копію з різними ИД
# print(id(lst), id(lst1))
#
# lst2 = sorted(lst) функція яка сортуе
# print(lst2)

# lst = [1, 7, 12, 3, 5, 57, 8]
# lst2 = [x * 2 for x in lst]
# lst3 = [str(x) for x in lst]
# lst4 = [int(x) for x in lst if int(x) % 2] #виведе кожне парне число
# print(lst)
# print(lst2)
# print(lst3)
# print(lst4)


# lst = [i for i in range(3, 59, 5) if i % 3 == 0]
# print(lst)


# lst = [1, 2, [3, 4, 5, 'axz'], 'abc']
# print(lst[2][-1][0])


# 1   2   3
# 4   5   6
# 7   8   9
# lst = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 6, 9]]
# for row in lst:
#     for x in row:
#         print(x)
#     print()

# lst = [[1, 2, 0],
#        [4, 0, 6],
#        [7, 0, 9]]
# for i in range(len(lst)):
#     for j in range (len(lst[i])):
#         if lst[i][j] == 0:
#             lst[i][j] == 1
#         print(lst[i][j], end=' ')
#     print()

# Вивести середній бал кожного студента
# studScores = [['Bob', 11, 8, 10, 12, 10],
#               ['Jane', 12, 11, 11, 11],
#               ['Kate', 7, 8, 9, 9],
#               ['Ivan', 3, 5, 7, 3, 10]]

# for lst in studScores:
#     avg = sum(lst[1:]) / len(lst[1:])
#     print(lst[0], '=', avg)

# for lst in studScores:
#     ma = max(lst[1:]) # максимальна оцінка
#     print(lst[0], '=', ma)

# score = [ [lst[0], sum(lst[1:]) / len(lst[1:])] for lst in studScores]
# for i in score:
#     print(i)
# print(score)


# bob = studScores[0]
# bob1 = bob[1:]
# bob1_sr = sum(bob1) / len(bob1)
# print(f'Cередній бал студента {studScores[0][0]} = {bob1_sr}')

# Практичні завдання до роботи №16 Списки

# task 1
# Вводиться список цілих чисел в одному рядку через пропуск, а потім деяке число x.
# Підрахуйте, скільки разів це число зустрічається у списку.
# Необхідно підрахувати суму всіх елементів у списку та їх середнє арифметичне.
# Cформуйте і виведіть список, в якому всі елементи початкового списку помножено на число x.

# lst = input('Вводиться список цілих чисел в одному рядку через пропуск: ').split()
# lst_int = [int(x) for x in lst] # Необхідно підрахувати суму всіх елементів у списку та їх середнє арифметичне.
#
# num = input('Вводиться деяке число x: ')
# print(lst, lst_int)
# count = lst_int.count(num) #Підрахуйте, скільки разів це число зустрічається у списку.
# print(f'{count = }')
# print(sum(lst_int), sum(lst_int) / (len(lst_int)))
#
# lst_num = [int(x)*num for x in lst]
# print(lst_num)



# lst = [int(x) for x in input('Вводиться список цілих чисел в одному рядку через пропуск: ').split()] # Необхідно підрахувати суму всіх елементів у списку та їх середнє арифметичне.
# lst = list(map(int, input('Вводиться список цілих чисел в одному рядку через пропуск: ').split()))
#
# num = input('Вводиться деяке число x: ')
# print(lst, lst)
# count = lst.count(num) #Підрахуйте, скільки разів це число зустрічається у списку.
# print(f'{count = }')
# print(sum(lst), sum(lst) / (len(lst)))
#
# lst_num = [int(x)*num for x in lst]
# print(lst_num)

# 4 task
# У списку цілих, заповненому випадковими числами, розрахуйте:
# ■ Суму від’ємних чисел.
# ■ Суму непарних чисел.
# ■ Добуток елементів з індексами, кратними 3.
# ■ Добуток елементів між мінімальним та максимальним елементом.
# ■ Суму елементів, що знаходяться між першим та останнім додатним елементом.

from random import randint, seed
seed(36)  # фіксація результату

n = 10  # розмір масиву
lst = [randint(-9, 9) for _ in range(n)] #У списку цілих, заповненому випадковими числами, розрахуйте:
# # lst_neg = [x for x in lst if x < 0] # ■ Суму від’ємних чисел.
# s = sum([x for x in lst if x < 0]) # ■ Суму від’ємних чисел.
# print(lst)
# # print(lst_neg, sum(lst_neg))
# print(s)
#
# d = 1
# for i in range(0, n, 3): #Добуток елементів з індексами, кратними 3.
#     print('----', i, lst[i])
#     d = d * lst[i]
# print(f'{d = }')


# ■ Суму елементів, що знаходяться між першим та останнім додатним елементом.

m = min(lst)
M = max(lst)

d = 1
m_index = lst.index(m)
M_index = lst.index(M)
start = min(m_index, M_index)
end = min(m_index, M_index) +1
print(f'{m_index=} {M_index=}')

for x in lst[start:end]:
    d = d*x
print(f'{d= }')

# # Завдання 5.
# # Маємо список заповнений випадковими числами.
# # Використовуючи дані цього масиву створіть список цілих, що містить лише:
# # парні числа з списку;
# # додатні числа з списку
# # сформуйте список, в якому відсортуйте першу половину заданого списку за спаданням, другу половину — за зростанням.
#
# lst = [1, -8, -9, 0, -7, -9, 7, -4, -2, -1]
# new_lst = sorted(lst[:5]) + sorted(lst[5:], reverse=True)
# print(lst)
# print(new_lst)

# # task 6
# # Визначте, скільки різних слів у введеному рядку.
# # Наприклад, у рядку "New Delhi New York Paris Prague York York " їх є 5.
#
# st = "New Delhi New York Paris Prague York York "
# unique_words = []
# lst = st.split()
# print(lst)
#
# for word in lst:
#     if word not in unique_words:
#         unique_words.append(word)
# count = len(unique_words)
# print(unique_words)
# print(f'{count = }')
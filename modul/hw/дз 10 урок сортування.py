# 1 task
# Напишіть програму «Книги». Створіть два списки з даними. Один список зберігає назви книг, другий — роки випуску.
# Реалізуйте меню для користувача:
# ■ відсортувати за назвою книг в алфавітному порядку;
# ■ відсортувати за рокам випуску за спаданням;
# ■ вивести список книг з назвами та роками випуску;
# ■ вихід.
#
# При сортуванні не використовувати готові рішення для списків як метод sort() та функцію sorted.
# При виводі вказати який спосіб сортування було реалізовано і використано.

# print('          *****«Книги»*****     ')
# print()
## book_titles = list(map(str, input('Введіть перелік книг через пробіл: ').split()))
## years_written = list(map(int, input('Введіть рік випуску книг через пробіл: ').split()))
# print()
# print('''          *****Виберіть операцію*****
# 1 - відсортувати за назвою книг в алфавітному порядку;
# 2 - відсортувати за рокам випуску за спаданням;
# 3 - вивести список книг з назвами та роками випуску;
# 4 - вихід''')
# print()
# result_selection = int(input('Виберіть операцію, цифру від 1 до 4: '))
# print()
#
# book_titles = ["Жотий князь",
#                "Убити пересмішника",
#                "Великий Гетсбі",
#                "Майстер і Маргарита",
#                "Маленькі жінки",
#                "Гаррі Поттер і філософський камінь",
#                "Той, хто біжить по лезу",
#                "Прокляття чорної перлини",
#                "Тихий Дон",
#                "Вбивство у Східному експресі"
#                ]
#
# years_written = [1961, 1960, 1925, 1938, 1868, 1997, 1968, 2003, 1928, 1934]
# lst = []
#
# if result_selection == 1:
#     for run in range(len(book_titles) - 1):
#         for i in range(len(book_titles) - 1):
#             if ord(book_titles[i][0]) > ord(book_titles[i + 1][0]):
#                 book_titles[i], book_titles[i + 1] = book_titles[i + 1], book_titles[i]
#     print(f'Відсортувані за назвою книг в алфавітному порядку: {book_titles}')
#
#
# if result_selection == 2:
#     for run in range(len(years_written) - 1):
#         for i in range(len(years_written) - 1):
#             if years_written[i] < years_written[i + 1]:
#                 years_written[i], years_written[i + 1] = years_written[i + 1], years_written[i]
#     print(f'Відсортуваний список за роками випуску за спаданням: {years_written}')
#
#
# if result_selection == 3:
#     for i in range(len(book_titles)):
#         lst.append([book_titles[i], years_written[i]])
#
# for i in lst:
#     print(f'Книга "{i[0]}" написана у {i[1]} році')
#
# if result_selection == 4:
#     print('Кінець')

# 2 task
# Напишіть програму для сортування списку методом удосконаленого бульбашкового сортування за спаданням
# Удосконалення полягає в тому, щоб аналізувати кількість перестановок на кожному кроці.
# Якщо ця кількість дорівнює нулю, то продовжувати сортування немає сенсу — список відсортовано.

# lst = [1961, 1960, 1925, 1938, 1997, 1968, 2003, 1928, 1934]
# count = 0
# for run in range(len(lst) - 1):
#     count = 0
#     for i in range(len(lst) - 1 - run):
#         if lst[i] < lst[i + 1]:
#             lst[i + 1], lst[i] = lst[i], lst[i + 1]
#             count+=1
#
#     if count==0:
#         break
#
# print(lst)

# task 1
from random import randint, seed

seed = (6)

lst = [randint(1, 100) for i in range(20)]
print(f'Початкойвий список: {lst}')
print()
# Cортування вибором (selection sort)

selection_sort_comparisons = 0
selection_sort_swaps = 0
for num in range(len(lst)):
    min_value = num

    for i in range(num, len(lst)):
        selection_sort_comparisons += 1
        if lst[min_value] < lst[i]:
            min_value = i
            selection_sort_swaps += 1

    lst[num], lst[min_value] = lst[min_value], lst[num]

print(f'''Відсортованний список методом (selection sort) 
{lst}''')
print(f'Кількість порівнянь С = {selection_sort_comparisons} та перестановок E елементів = {selection_sort_swaps}')
print()
# Сортування вставкою  (Insertion sort)

insertion_sort_comparisons = 0
insertion_sort_swaps = 0

n = len(lst)
for i in range(1, n):
    for j in range(i, 0, -1):
        insertion_sort_comparisons += 1
        if lst[j] > lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            insertion_sort_swaps += 1

        else:
            break

print(f'''Відсортованний список методом (Insertion sort) 
{lst}''')
print(f'Кількість порівнянь С = {insertion_sort_comparisons} та перестановок E елементів = {insertion_sort_swaps}')

# 1. Сортування вибором. Selection sort.
# 2. Сортування бульбашкою (bubble sort)
# 3. Сортування вставкою (insertion sort)
# 4. Сортування Шелла
# 5. Сортування злиттям (рекурсивно, нерекурсивно (ітеративно)
#
# ____________________________________________________________
# 1. Сортування вибором. Selection sort.
# ____________________________________________________________
# arr = [-3, 5, 0, -8, 1, 10]
# n = len(arr)
# for i in range(n - 1):  # пробегает от первого до передостаннього
#     min_value = arr[i]  # зберігае мінімальне значення
#     index = i  # індекс мінімального значення
#     for j in range(i + 1, n):  # пошук мінімального
#         if min_value > arr[j]:
#             min_value = arr[j]
#             index = j
#
#     if index != i:  # обмін значеннями, якщо був знайдений мінімальний не в і-й позиції
#         t = arr[i]
#         arr[i] = arr[index]
#         arr[index] = t
#
# print(arr)
#
# аналогично
# def selection_sort(lst):
#     for i in range(len(lst)): # проходимо по всім елементам послідовності
#         min_value = i # присвоюемо текущее значення індексу змінній min_value
#
#         for j in range(i, len(lst)): #
#             if lst[min_value] > lst[j]: # порівнюемо мінімальне значечення з текущим
#                 min_value = j # якщо мінімальне значечення більше за поточне змінній min_value присвоюемо значення j
#
#         lst[i], lst[min_value] = lst[min_value], lst[i] #міняемо поточне значення і мінімальне місцями
#     return lst
#
# lst = [12,34,25,15,67,23,11,5,86]
# print(selection_sort(lst))
#
# ____________________________________________________________
# 2. Сортування бульбашкою (bubble sort)
# ____________________________________________________________
#
# arr = [5, 7, 4, 3, 8, 2]
# n = len(arr)
# count = 0
# for run in range(n - 1):  # робимо на 1 менше обходів списку чим кількість елементів
#     for i in range(n - 1 -run):  # порівнюемо поточний емент з наступним і віднімаемо пузр який всплив за рахунок -run
#         if arr[i] > arr[i + 1]:  # якщо поточний більше за мастпний
#             count += 1
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]  # міняемо їх місцями
#
# print(arr)
# print(count)
#
# ____________________________________________________________
# 3. Сортування вставкою (insertion sort)
# ____________________________________________________________
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current_value = arr[i]  # текущий елемент
#         position = i  # індекс текущего елемента
#
#         while position > 0 and arr[position - 1] > current_value:  # сортирует внутри подмасива елементі, работает пока текуший індекс елемента >0 і пока последние елемент данног омасива больше текущего елемента
#             arr[position] = arr[position - 1]
#             position -= 1
#         arr[position] = current_value
#
#     return arr
#
# arr = [14, 33, 34, 25, 15, 167, 23, 11, 5, 86, 10, 35, 27]
# print(insertion_sort(arr))
#
# arrey = [4, 3, 2, 10, 12, 1, 5, 6]
# n = len(arrey)
#
# for i in range(n):
#     element = arrey[i]
#     j = i
#     while (j > 0 and arrey[j - 1] > element):
#         arrey[j] = arrey[j - 1]
#         j = j - 1
#     arrey[j] = element
#
# print(arrey)
#
# аналогично
# arrey = [4, 3, 2, 10, 12, 1, 5, 6]
# n = len(arrey)
#
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if arrey[j - 1] > arrey[j]:
#             arrey[j], arrey[j - 1] = arrey[j - 1], arrey[j]
#         else:
#             break
#     print(i, arrey)
# print(arrey)
#
# ____________________________________________________________
# 4. Сортування Шелла
# ____________________________________________________________
# def shell_sort(arr):
#     gap = len(arr)//2
#
#
#     while gap > 0:
#         for value in range(gap, len(arr)):
#             curent_value = arr[value]  # створюеме змінну і призначаемо її значення поточного єлементу
#             position = value  # значення індексу елементу
#
#             while position >= gap and arr[
#                 position - gap] > curent_value:  # поки значення індексу >= числу gap і елемент порівювальний з поточним значенням буде більне нього
#                 arr[position] = arr[position - gap]  # міняемо елементи місцями
#                 position -= gap
#                 arr[position] = curent_value
#
#         gap //= 2
#     return arr
#
# arr = [18, 27, 32, 17, 6, 20, 22, 2, 5, 31, 1, 8, 19, 8, 20, 48, 42, 3, 40, 5]
# print(f'Відсортований масив методом Шелла: {shell_sort(arr)}')
#
#
# ____________________________________________________________
# 5. Сортування злиттям (merege sort) (рекурсивно, нерекурсивно (ітеративно)
# ____________________________________________________________
# def merge_two_list(a, b):
#     c = []
#     i = j = 0  # i,j вказують на перші елементи списку а і b
#     while i < len(a) and j < len(b):  # поки і,j небуде перевишувати довижини списку а, b
#         if a[i] < b[j]:  # якщо поточний елемент списку а менший, тоді
#             c.append(a[i])  # додаемо його до списку с
#             i += 1  # пересуваемо показник і на 1
#         else:  # якщо поточний елемент списку b менший, тоді
#             c.append(b[j])  # додаемо його до списку с
#             j += 1  # пересуваемо показник j на 1
#
#     if i < len(a): #робимо перевірку, якшо і недосяг кінця
#         c += a[i:] #додаемо все що залишилось у данному списку в список с
#     if j < len(b):
#         c += b[j:]
#     return c
#
# def merge_sort(lst):  # дана функція виконуе сортування
#     if len(lst) == 1:  # якщо довжиша списку == 1, це означае що список відсортованний
#         return lst
#     midle = len(lst) // 2  # знаходимо середину
#     left = merge_sort(lst[:midle])  # предаемо функції merge_sort ліву частину списку
#     right = merge_sort(lst[midle:])  # предаемо функції merge_sort праву частину списку
#     return merge_two_list(left, right)  # за допомогої функції merge_two_list обеднуемо ці дві частини
#
# lst = [6, 3, 4, 2, 99, 5, 13, 25, -5]
# print(merge_sort(lst))
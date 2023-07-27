# from random import randint, seed
# seed(13)
# lst = [randint(0,20) for i in range(13)]
# lst1 = lst[ : ]
# lst2 = lst[ : ]
#
# step = len(lst1) // 2
# n = len(lst1)
# print(f'{step=} initial list: {lst1}')
# count = 0
# count_insert = 0
#
# # Сортування Шелла
# while step > 0:
#     for i in range(step, n):  # Від середини списку до кінця
#         current_value = lst1[i]  # Значення списку
#         position = i  # Індекси
#
#         while position >= step and lst1[position - step] < current_value:
#             lst1[position] = lst1[position - step]
#             position -= step
#             count += 1
#
#         lst1[position] = current_value
#
#     step = step // 2
#     print(f'{step=} output list: {lst1}')
# print(f'Кількість обмінів у процесі впорядкування Шелла = {count}')
#
# # Сортування вставкою
#   # Створення копії списку
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if lst2[j - 1] < lst2[j]:
#             lst2[j], lst2[j - 1] = lst2[j - 1], lst2[j]
#             count_insert += 1
#         else:
#             break
#
# print(f'Впорядкований список простим алгоритмом вставки: {lst2}')
# print(f'Кількість обмінів у процесі впорядкування простим алгоритмом вставки = {count_insert}')

# 2 task

# def quick_sort(lst):
#     if len(lst) == 1 or len(lst) == 1:
#         return lst
#
#     if len(lst) > 1:
#         n = len(lst) // 2
#         pivot = lst[n]
#         left = [item for item in lst if item < pivot]
#         center = [item for item in lst if item == pivot]
#         right = [item for item in lst if item > pivot]
#
#         return quick_sort(left) + center + quick_sort(right)
#     return lst
#
# lst = [7, 29, 15, 36, 24, 20, 18, 30, 12]
#
# res = quick_sort(lst)
# print(res)

# 1 task
# from random import randint,seed
# seed (9)
#
# lst = [randint(1,20) for i in range(15)]
# print(f'Початковий рандомний список: {lst}')
#
# # Рекрсивно відсортуваний список методом злиття
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
# print(f'Рекрсивно відсортуваний список методом злиття: {merge_sort(lst)}')
#
# # Ітеративно відсортуваний список методом злиття
# def merge_sort(lst):
#     if len(lst) <= 1:
#         return lst
#
#     def merge(left, right):
#         merged = []
#         left_index, right_index = 0, 0
#
#         while left_index < len(left) and right_index < len(right):
#             if left[left_index] < right[right_index]:
#                 merged.append(left[left_index])
#                 left_index += 1
#             else:
#                 merged.append(right[right_index])
#                 right_index += 1
#
#         merged.extend(left[left_index:])
#         merged.extend(right[right_index:])
#         return merged
#
#     # Ітеративно ділимо масив на менші частини
#     sorted_arrays = [[val] for val in lst]
#
#     while len(sorted_arrays) > 1:
#         new_sorted_arrays = []
#         for i in range(0, len(sorted_arrays) - 1, 2):
#             merged_array = merge(sorted_arrays[i], sorted_arrays[i + 1])
#             new_sorted_arrays.append(merged_array)
#
#         if len(sorted_arrays) % 2 == 1:
#             new_sorted_arrays.append(sorted_arrays[-1])
#
#         sorted_arrays = new_sorted_arrays
#
#     return sorted_arrays[0]
#
#
# sorted_lst = merge_sort(lst)
# print(f'Ітеративно відсортуваний список методом злиття: {sorted_lst}')


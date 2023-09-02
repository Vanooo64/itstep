# О нотація ???
# рекурсія
# регулярні вирази

# selection sort = O(n**2)

# # сортування вибором
# arrey = [12, 29, 25, 8, 32, 17, 40]
# n = len(arrey)
#
# for i in range(n - 1):
#     min_index = i
#     min_value = arrey[i]
#     for j in range(i + 1, n):
#         if arrey[j] < min_value:
#             min_index = j
#             min_value = arrey[j]
#     print(f'{i=} : min_element = {min_value}')
#     if min_index != i:
#         arrey[min_index] = arrey[i]
#         arrey[i]= min_value

# print(arrey)

# сортування бульбашкою (bubble sort)
# array = [6, 9, 4, 1, 5, 3, 7]
# n = len(array)
#
# for i in range(n - 1):
#     for j in range(n-1-i):
#         if array[j] > array[j+1]:
#             print(f'{i=}, {j} : {array}')
#             # swap
#             array[j], array[j + 1] = array[j+1], array[j]
#
# print(array)

# сортування вставкою (insertion sort)

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

# arrey = [4, 3, 2, 10, 12, 1, 5, 6]
# def inseert_sort(array):
#     n = len(arrey)
#
#     for i in range(n):
#         element = arrey[i]
#         j = i
#         while (j > 0 and arrey[j - 1] > element):
#             arrey[j] = arrey[j - 1]
#             j = j - 1
#         arrey[j] = element
#     return arrey
#
# inseert_sort(array)
# print(arrey)
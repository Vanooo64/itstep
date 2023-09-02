lst = [-4, 3, -2, 10, -12, 1, 5, -6]

# def get_arr(lst):
#     result = list()
#     for item in lst:
#         if item > 0:
#             result.append(item)
#
#     print(result)
#     return result
#
#
# new_arr = get_arr(lst)
# print(new_arr)

# def myfunc(lst):
#     result = [item for item in lst if item > 0 ]
#     return result
#
#
# arr_1 = myfunc([1,-3,2,3,2,6,-4])
# arr_2 = myfunc(lst)
# print(arr_1, arr_2)

# сортування Шелла

# lst = [33, 31, 40, 8, 12, 17, 25, 42]
# print(lst)
# l = len(lst)
# step = l // 2
#
# while step > 0:
#     print(f'{step = }')
#     for i in range(step, l):
#         j = i
#         while j - step >= 0 and lst[j - step] > lst[j]:
#             lst[j], lst[j - step] = lst[j - step], lst[j]
#             j = j - step
#             print(f'{i=} {j=}', lst)
#     step = step // 2
#
# print()
# print(lst)

#                           рекурсія
# def factorial(n):
#     print('Виклик при {n=}')
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
#
# result = factorial(5)
# print(result)



# Сортування злитям (merge sort)

# def merge(left, right):
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
#
# def mergeSort(arr):
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]
#     if len(left) > 1:
#         left = mergeSort(left)
#     if len(right) > 1:
#         right = mergeSort(right)
#
#     merged_list = merge(left, right)
#     return merged_list
#
#
# arr = [64, 34, 25, 12, 22, 11, 90]
# arr_sorted = mergeSort(arr)
# print(arr_sorted)

# швидке сортування
def quick(arr):
    if len(arr) == 1:
        return arr

    pivot = arr[-1]
    left = [item for item in arr if item < pivot]
    center = [item for item in arr if item == pivot]
    right = [item for item in arr if item > pivot]
    return quick(left) + [center] + quick(right)


arr = [9, 12, 9, 2, 17, 1, 6]

res = quick(arr)
print(res)

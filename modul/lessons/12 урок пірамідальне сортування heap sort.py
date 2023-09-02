#                       heap sort пірамідальне сортування
#
# def heapify(arr, size_heap, root):  # size_heap -  довжина масиву, root - індекс батькіского елемента
#     # build max_heap будуе максимальну піраміду
#     largest = root #найбільший індекс корень
#     left,  right  = 2 * root + 1, 2 * root + 2
#
#     if left < size_heap and arr[left] > arr[largest]:
#         largest = left
#     if right < size_heap and arr[right] > arr[largest]:
#         largest = right
#
#     if largest != root:
#         arr[root], arr[largest] = arr[largest], arr[root]
#         heapify(arr, size_heap, largest)
#
#
# def heap_sort(arr):
#     # ініціалізація масиву init heap and max_heap
#     n = len(arr)  # довжина масиву
#     for i in range(n // 2 - 1, -1, -1):  # від середини до 0 з кроком -1
#         heapify(arr, n, i)
#
#     # 2 крок міняемо останій елемент з першим а перший заносимо в кінець списку arr
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#
#
# arr = [81, 89, 9, 11, 14, 76, 54, 22]
# print(arr)
#
# heap_sort(arr)
# print(arr)

#                           лінійний пошук (linear search)

# def linear_search(arr, key):
#     for item in range(len(arr)):
#         if key == arr[item]:
#             return item
#     return -1
#
# lst = [81, 89, 9, 11, 14, 76, 54, 22]
# search_item = 51
# print(f" індекс {linear_search(lst,search_item)}")

#                   повертае максимальний індеск максимального числа в списку

# def linear_max(arr):
#     max_value = arr[0]
#     max_index = 0
#     for item in range(len(arr)):
#         if arr[item] > max_value:
#             max_value = arr[item]
#             max_index = item
#     return max_index
#
# lst = [81, 89, 9, 11, 14, 76, 54, 89, 22]
# print(f" максимальний індекс = {linear_max(lst)}")

#                       бінарний пошук binary search працюе тільки з впорядкованним масивовом



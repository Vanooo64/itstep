# ids = list(map(int, input('Введіть ідентифікаційні коди для користувачів: ').split(',')))
# phones = list(map(str, input('Введіть телефонні номери для користувачів в тому ж порядку що і ідентифікаційні коди: ').split(',')))
# print(ids)
# print(phones)
#
# #тест
# # ids = [102, 42, 57, 16, 89]
# # phones = [555-1234, 555-9876, 555-5678, 555-2468, 555-8888]
#
# def heap_sort(arr, reverse=False):
#     def heapify(arr, n, i):
#         largest = i
#         left_child = 2 * i + 1
#         right_child = 2 * i + 2
#
#         if left_child < n and (arr[i] < arr[left_child] if reverse else arr[i] > arr[left_child]):
#             largest = left_child
#
#         if right_child < n and (arr[largest] < arr[right_child] if reverse else arr[largest] > arr[right_child]):
#             largest = right_child
#
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)
#
#     n = len(arr)
#
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
# def display_records(ids, phones):
#     for i in range(len(ids)):
#         print(f"ID: {ids[i]}, Phone: {phones[i]}")
#
#
# while True:
#     print("\nМеню:")
#     print("1. Відсортувати за ідентифікаційними кодами за зростанням")
#     print("2. Відсортувати за номерами телефонів за спаданням")
#     print("3. Вивести список користувачів з кодами та телефонами")
#     print("4. Вихід")
#
#     choice = input("Виберіть опцію: ")
#
#     if choice == '1':
#         heap_sort(ids)
#         print("Список користувачів за ідентифікаційними кодами:")
#         display_records(ids, phones)
#     elif choice == '2':
#         heap_sort(phones, reverse=True)
#         print("Список користувачів за номерами телефонів:")
#         display_records(ids, phones)
#     elif choice == '3':
#         print("Список користувачів:")
#         display_records(ids, phones)
#     elif choice == '4':
#         print("До побачення!")
#         break
#     else:
#         print("Невірний вибір. Спробуйте ще раз.")

# # Домашня робота №24 Алгоритми пошуку
# # Завдання 1.
# # Список задається рандомно довжини 20 із цілих чисел з відрізку [0,9].
# # Із використанням лінійного пошуку знайдіть індекс останнього входження елемента
# # у цьому списку, введене користувачем. Якщо такого елемента нема або список порожній,
# # то поверніть None.
# #
# # Наприклад, заданий список [2,3,7,3,3,2,5,6].
# # Тоді для введеного елемента key = 3, index = 4.
#
# from random import randint, seed
#
# seed(9)
# arr = [randint(0, 9) for _ in range(20)]
# key = int(input((f'Введіть елемент, індекс останнього входження якого ви хочете знайти у списку {arr}: ')))
#
#
# def linear_searhc(arr, key):
#     for item in range(len(arr)-1, -1, -1):
#         if key == arr[item]:
#             return item
#         if len(arr) == 0:
#             return None
#     return None
#
# index = linear_searhc(arr, key)
# print(f'Для введеного елемента {key = }, {index = }.')

# Завдання 2.
# Список задається рандомно довжини 20. Відсортуйте список деяким алгоритмом (оберіть самі).
# Далі із використанням бінарного пошуку знайдіть індекс елемента у цьому списку, введене
# користувачем. Якщо такого елемента нема або список порожній, то поверніть None.

from random import randint, seed

seed(45)
arr = [randint(1, 50) for _ in range(20)]
print(f'Початковий масив створено рандомно: {arr}')

def shell_sort(arr):
    gap = len(arr)//2


    while gap > 0:
        for value in range(gap, len(arr)):
            curent_value = arr[value]  # створюеме змінну і призначаемо її значення поточного єлементу
            position = value  # значення індексу елементу

            while position >= gap and arr[
                position - gap] > curent_value:  # поки значення індексу >= числу gap і елемент порівювальний з поточним значенням буде більне нього
                arr[position] = arr[position - gap]  # міняемо елементи місцями
                position -= gap
                arr[position] = curent_value

        gap //= 2
    return arr

sor_arr = shell_sort(arr)
print(f'Відсортований масив методом Шелла: {sor_arr}')
print()
key = int(input(f'Введіть число, індекс якого Ви хочете знайти у відсортованому списку: '))


def binary_searhc(sor_arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if sor_arr[mid] == key:
            return mid
        elif sor_arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return None

index = binary_searhc(arr, key)
print(f'Індекс елемента "{key}" у відсортованому списку = {index}')

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


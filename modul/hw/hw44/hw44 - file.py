
# # Завдання 1.
# # Напишіть функцію, яка виводить розмір кожного файлу в заданому  каталозі, його значення в байтах, дату/час створення
# # та зміни. Якщо каталога із вказаним ім’ям немає, генерується виняток. Використайте модулі os і time.
#
# import os
# from datetime import datetime
#
# def get_info_file(path):
#     try:
#         for item in os.listdir(path): #повертае списко файлів які знаходяться у директорії
#             if os.path.isfile(item): #відкидає всі папки, бере тільки файли
#                 size_bytes = (os.path.getsize(item))
#                 get_time = os.path.getmtime(item)
#                 creation_time = datetime.fromtimestamp(get_time)
#                 print(f"Файл {item} важить {size_bytes} байти, дату та час створення та зміни: {creation_time}")
#     except FileNotFoundError:
#         print(f"Файл або директорія не знайдена: {path}")
#     except PermissionError:
#         print(f"Немає прав доступу для отримання інформації про файли в директорії: {path}")
#     except Exception as e:
#         print(f"Сталася помилка: {str(e)}")
#
# path = os.getcwd() #повертае повний шлях в якому знаходиться файл
# get_info_file(path)


# # Завдання 2.
# # Функція приймає розширення файлів, директорію-1 і директорію-2, і  робить резервну копію усіх файлів із цими
# # розширеннями із директорії-1 у директорію 2. Можна скористатись `shutil.copy2()`.
#
# import os
# import shutil
#
# def backup_files_by_extension(extension, source_dir, target_dir):
#     try:
#         for filename in os.listdir(source_dir):
#             if filename.endswith(extension) and os.path.isfile(os.path.join(source_dir, filename)): #Перевірка, чи файл має розширення .txt та чи є це файл (а не папка).
#                 source_file_path = os.path.join(source_dir, filename) #Формування повного шляху до файлу у вихідній директорії.
#                 target_file_path = os.path.join(target_dir, filename) #Формування повного шляху для файлу у директорії резервних копій.
#                 shutil.copy2(source_file_path, target_file_path) #Використання копіювання файлу з source_file_path у target_file_path.
#                 print(f'Копіювання файлу {source_file_path} в {target_file_path} завершено.')
#     except FileNotFoundError:
#         print(f'Директорія {source_dir} або {target_dir} не знайдена.')
#     except PermissionError:
#         print(f'Немає прав доступу для копіювання файлів в директорію {target_dir}.')
#     except Exception as e:
#         print(f'Сталася помилка під час копіювання файлів: {str(e)}')
#
# # Папка, яку потрібно зробити резервну копію
# source_dir = '/Users/ivansavchenko/PycharmProjects/itstep/modul/hw/hw44'
# # Шлях та ім'я архіву резервної копії
# target_dir = '/Users/ivansavchenko/PycharmProjects/itstep/modul/hw/backup_path_hw44'
# # def backup_files_by_extension(extension, source_dir, target_dir):
# extension = '.txt'
#
# backup_files_by_extension(extension, source_dir, target_dir)

# Завдання 3.
# Розрахувати загальний розмір та кількість усіх файлів у заданій директорії та її піддиректоріях. Використати функцію os.walk()
import os

def total_size_and_count(path):
    total_size = 0
    total_count = 0

    for dirpath, dirnames, filenames in os.walk(path): #повертае списко файлів які знаходяться у директорії
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size_bytes = (os.path.getsize(fp))
            total_size += size_bytes
            total_count += 1
    print(f"Загальна кількість усіх файлів у папці {path} = {total_count}, їх розмір - {total_size}")

path = os.getcwd()
total_size_and_count(path)











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
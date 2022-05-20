'''
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:
|--my_project
    ...
    |--templates
    |   |--mainapp
    |   |    |--base.html
    |   |    |--index.html
    |   |--authapp
    |       |--base.html
    |       |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.
'''
import Task_7_1
import os
from glob import glob
import shutil

##можно задать людой словарь и по нему создать папки обратившись к ранее созданной функции###
# folder_dict = {'my_project':
#                    [
#                        {'mainapp': ['base.html', 'index.html'],
#                         'authapp': ['base.html', 'index.html']
#                        }
#                    ]
#             }
# path = os.getcwd()
# Task_7_1.make_dir_from_dict(folder_dict, path)

def collect_file(path, trash_files):
    for root, folders, files in os.walk(path):
        # print(f'Root {root} folders {folders} files {files}')
        # print(os.listdir(trash_files), files)
        if files:
            for el in files:
                if el in os.listdir(trash_files):
                    print(f'Файл {el} из папка {root} не может быть скопирован, так как файл'
                          f' с таким именем уже существует')
                else:
                    shutil.copy(os.path.join(root, el), trash_files)
            #shutil.copytree(os.path.join(path, root), trash_files, dirs_exist_ok=True)


if __name__ == "__main__":
    path = os.getcwd()
    if os.path.exists('all_files'):
        print('Удаляем ранее созданную папку all_files и создаём новую')
        shutil.rmtree('all_files')
    os.makedirs(os.path.join(path, 'all_files'), exist_ok=True)
    trash_files = os.path.join(path, 'all_files')
    collect_file(os.path.join(path, 'my_project'), trash_files)
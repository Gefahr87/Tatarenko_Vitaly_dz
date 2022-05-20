"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
данные о вложенных папках и файлах (добавлять детали)?

"""
import os

def make_dir_from_dict(folder_dict, path):
    for element, below_element in folder_dict.items():
        #print(f'ключ: {element}, значение: {below_element}')
        if isinstance(element, str):
            os.makedirs(os.path.join(path, element), exist_ok=True)
        if isinstance(below_element, list):
            #print(f'Значение - список: {below_element}')
            for name_below_element in below_element:
                if isinstance(name_below_element, dict):
                    make_dir_from_dict(name_below_element, os.path.join(path, element))
                elif name_below_element.find('.') != -1:
                    f = open(os.path.join(path, element, name_below_element), 'w')
                    f.close()
                else:
                    os.makedirs(os.path.join(path, element, name_below_element), exist_ok=True)
        elif isinstance(below_element, dict):
            for key in below_element:
                print('Do somthing')
                make_dir_from_dict(key, os.path.join(path, element))
        elif isinstance(below_element, str):
            #print(f'Below_element - str: {below_element}')
            if below_element.find('.') != -1:
                    f = open(os.path.join(path, element, below_element), 'w')
                    f.close()
            else:
                os.makedirs(os.path.join(path, element, below_element), exist_ok=True)
    return

folder_dict = {'my_project': ['settings', 'tst.py','mainapp', 'adminapp', 'authapp'],
               'test_file':
                   [
                       {'super_test': ['test_iq', 'test_fps', 'test.py'],
                        'easy_test':
                            [
                                {'firts': ['sum_to_10', 'sum_to_100', 'sum.html'],
                                 'second':
                                     [
                                         {'second_one': ['comparison', 'comp.css'],
                                            'second_two': 'brrr.zip',
                                            'secon_three': ['free_folder', 'free.file']
                                         }
                                     ]
                                 }
                            ],
                        'hard_test': ['fourier_series', 'find_genius', 'logical', 'lg.jpg']
                        }
                   ]
               }
if __name__ == "__main__":
    path = os.getcwd()
    make_dir_from_dict(folder_dict, path)

'''
ввёл свой словарь, что бы работало для папок и файлов. пример, разобранного задания на вебинаре очнь помог,
но хотелось это же реализовать через dict.items(). Из-за появления нескольких уровней вложенностей запустался в if - 
- elif. Срипт протестировал на разных словарях, пытаясь добиться универсальности. Можно задавать любую нужную иеархию.
Как я понял ограничений во вложенности нет.
'''
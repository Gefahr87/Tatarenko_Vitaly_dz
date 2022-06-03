'''
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
    return x ** 3
a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)
'''

def tuper_ligger(func):
    def wrapper(*args, **kwargs):
        res = []
        if len(args) == 1 and type(*args) == int:
            res = func(*args)
            info_about_args = args[0]
        elif len(args[0]) != 1:
            info_about_args = list(args[0])
            for arg in list(*args):
                res.append(func(arg))
        for key, value in kwargs.items():
            print(f'Ключ {key} имеет тип {type(key)}. Значение ключа {value} имеет тип {type(value)}')
        return f'\n{str(func)[10:19]}({info_about_args}: {type(info_about_args)})\nРезультат работы функции: {res}\n'
    return wrapper

@tuper_ligger
def calc_cube(x):
    res = x ** 3
    return res

# list_of_numbers = [x for x in range(100)]
numbers = 20235
print(calc_cube(numbers, test=[12, 45, 444], test_2=55, dct={3: 2}))
numbers = (2, 10, 100, 555, 666)
print(calc_cube(numbers))

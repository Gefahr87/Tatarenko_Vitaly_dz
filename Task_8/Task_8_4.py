'''
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
    a = calc_cube(5)
125
    a = calc_cube(-5)
Traceback (most recent call last):
raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
'''

def val_checker(func):
    def wrapper(*args):
        res = []
        for arg in args[0]:
            if arg > 0:
                res.append(func(arg))
            try:
                if arg < 0:
                    raise ValueError
            except:
                print(f'ValueError: wrong val {arg}')

        return res
    return wrapper

@val_checker
def calc_cube(x):
    return x ** 3

numbers = (2, 10, -100, 555, 666)
print(calc_cube(numbers))

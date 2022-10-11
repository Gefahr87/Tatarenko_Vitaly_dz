"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""
from random import randint


def guess(number: int, attempt=None) -> str:
    attempt = int(input('Какое число было загадано?\n'))
    if number == attempt:
        return 'В точку!'
    elif attempt > number:
        print('Загаданное число меньше')
    elif attempt < number:
        print('Загаданное число больше')
    return guess(number, attempt)


if __name__ == '__main__':
    number = randint(0, 100)
    print(guess(number))
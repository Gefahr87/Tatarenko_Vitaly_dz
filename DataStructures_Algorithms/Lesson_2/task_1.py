"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def custom_sum(number_1: int, number_2: int) -> int:
    return number_2 + number_1


def custom_sub(number_1: int, number_2: int) -> int:
    return number_1 - number_2


def custom_mult(number_1: int, number_2: int) -> int:
    return number_2 * number_1


def custom_divis(number_1: int, number_2: int) -> int or str:
    if number_2 == 0:
        return print('Деление на ноль запрещено')
    else:
        return number_2 / number_1


def check_number(is_it_number: str) -> int or str:
    try:
        return int(is_it_number)
    except ValueError:
        return print('Вы ввели не число')


def calc(number_1: str, number_2: str, operation: str) -> int or str:
    if operation == '+':
        return custom_sum(number_1, number_2)
    elif operation == '-':
        return custom_sub(number_1, number_2)
    elif operation == '*':
        return custom_mult(number_1, number_2)
    elif operation == '/':
        return custom_divis(number_1, number_2)
    else:
        return 'Такая операция не продусмотрена'


def main():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода):')
    if operation == '0':
        return print('Ну и не надо')
    else:
        number_1 = check_number(input('Введите первое число:'))
        number_2 = check_number(input('Введите второе число:'))
        print(calc(number_1, number_2, operation))
    return main()


if __name__ == '__main__':
    main()

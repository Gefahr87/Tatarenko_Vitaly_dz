'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из
  этого списка, сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.)
'''

def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    print('Для массива:', my_list, sep='\n')
    acc_cifr = 0
    result = 0
    #print('Элементов в списке: ', len(my_list))
    for i in range(len(my_list)):
        cifr = my_list[i]
        while cifr != 0:
            acc_cifr += cifr % 10
            #print('Сумма =', acc_cifr)
            cifr = (cifr // 10)
            #print(cifr)
        if acc_cifr % 7 == 0:
            result += my_list[i]
            #print('Промежуточная сумма = ', result)
        acc_cifr = 0
    print('Результат = ', end="")
    return result  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    for i in range(len(my_list)):
        my_list[i] += 17
    result = sum_list_1(my_list)
    return result  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    ''' не знаю какой цикл for будет лечше, оставил с доп. параметрами вместо:
        for idx in range(1000):
           if (idx + 1) % 2 == 0:
               my_list.append(idx ** 3)
        print(my_list)
    '''
    for idx in range(1, 1000, 2):
        my_list.append(idx ** 3)
    #print(my_list)
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)

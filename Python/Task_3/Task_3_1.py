'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:
//>>> num_translate("one")
"один"
//>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.
'''

"""
Ход мысли:
Написать словарь соответсвия, где ключ - слово на английском, а значение слово на русском. Чтобы не было ошибки
воспользовать get, только вот вопрос где, можем при выводе?. А как сделать перевод в обе стороны и исключить ошибку 
по вводу заглавных букв + выввести слово с заглавной буквы 
"""


def num_translate(number: str):
    translate_dict_to_en = {}
    translate_dict_to_ru = {
        'one': 'один',
        'zero': 'ноль',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    for key, value in translate_dict_to_ru.items():
        translate_dict_to_en[value] = key
    if translate_dict_to_en.get(number.lower()):
        return translate_dict_to_en[number.lower()].capitalize()
    else:
        return translate_dict_to_ru.get(number.lower()).capitalize()


if __name__ == "__main__":
    print(num_translate('one'))
    print(num_translate('eight'))



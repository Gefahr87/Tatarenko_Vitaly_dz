'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
//>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''
import random


def get_jokes(k):
    ouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный",
                      "мягкий"]
    result = []
    for i in range(k):
        result.append(f'{random.choice(ouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return  result


if __name__ == "__main__":
    print(get_jokes(2))

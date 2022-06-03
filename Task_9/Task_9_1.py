'''
Создать класс TrafficLight (светофор):
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
'''

import time
from time import sleep

class TrafficLight():
    _color = None
    __time_of_color = {1: {'green': 5}, 2: {'yellow': 2}, 3: {'red': 7}}

    def running(self, color, repeat):
        i = 0
        repeat *= 3
        for key, value in self.__time_of_color.items():
            for clr, dl in value.items():
                if clr == color:
                    number_of_light = key
                    color = clr
                    delay = dl

        while i < repeat:
            print(f'Горит {color}')
            time.sleep(delay)
            if number_of_light == 3:
                number_of_light = 1
            else:
                number_of_light += 1
            color, delay = zip(*self.__time_of_color[number_of_light].items())
            color, delay = color[0], delay[0]
            i += 1

flash = TrafficLight()
flash.running('yellow', 3)

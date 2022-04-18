'''
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на
экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов
списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
'''

employes = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(employes)):
    employes[i] = employes[i].split(' ')
    employes[i][-1] = employes[i][-1].lower().capitalize()
    print(f'Привет, {employes[i][-1]}!')
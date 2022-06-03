# Ну, начнём-с

'''
Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
'''

mlt_plication = 15 * 3
division = 15 / 3
integer_division = 15 // 3
remndr_division = 15 % 3

print(f'Тип при операции 15*3: {type(mlt_plication)}', f'Тип при операции 15/3: {type(division)}',
      f'Тип при операции 15//2: {type(integer_division)}', f'Тип при операции 15%2: {type(remndr_division)}', sep='\n')

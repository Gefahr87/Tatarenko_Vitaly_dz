"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class Task_meneger():
    new_task = []
    to_check_task = []
    done_task = []

    def __init__(self, number_task: int, status=None) -> 'quantity of task':
        #status: 'int: 1 - done, 2 - to_check'
        self.number_task = number_task
        self.status = status
        self.add_new()

    def add_new(self):
        Task_meneger.new_task.insert(0, self.number_task)

    @staticmethod
    def work_on_task(status):
        if status == 1:
            Task_meneger.done_task.append(Task_meneger.new_task.pop())
        elif status == 2:
            Task_meneger.to_check_task.append(Task_meneger.new_task.pop())


if __name__ == '__main__':
    task_1 = Task_meneger(1)
    task_2 = Task_meneger(2)
    task_3 = Task_meneger(3)
    task_4 = Task_meneger(4)
    print(Task_meneger.new_task)
    Task_meneger.work_on_task(1)
    Task_meneger.work_on_task(2)
    print(f'Задачи в очреди {Task_meneger.new_task}')
    print(f'Выполненные задачи {Task_meneger.done_task}')
    print(f'Задачи на доработку {Task_meneger.to_check_task}')









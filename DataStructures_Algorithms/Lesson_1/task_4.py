"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def user_verification_v1(login: str, passwrd: str, auth_dict: dict) -> bool:                        # O(n)
    for user in auth_dict:                                                                          # O(n)
        if auth_dict[user]['login'] == login and auth_dict[user]['password'] == passwrd:            # O(1)
            print(f'Пользователь с логином {login} существует и пароль введён верно')               # O(1)
            if auth_dict[user]['activate_status'] == False:                                         # O(1)
                print('Необходима активации учётной записи, обратитесь к неизвестному существу')    # O()
                return False                                                                        # O(1)
            else:                                                                                   # O(1)
                print('Вы залогинены')                                                              # O(1)
                return True                                                                         # O(1)
    print(f'Связка логин и пароль не существует для пользователя {login}')                          # O(1)
    return False                                                                                    # O(1)

def user_verification_v2(login: str, passwrd: str, auth_dict: dict) -> bool:                        # O(n^2)
    for user, param in auth_dict.items():                                                           # O(n^2)
        flag = 0                                                                                    # O(1)
        for key, val in param.items():                                                              # O(n)
            if val == login:                                                                        # O(1)
                print('Login существует')                                                           # O(1)
                flag = 1                                                                            # O(1)
            elif val == passwrd and flag == 2:                                                      # O(1)
                print('Пароль существует')                                                          # O(1)
            elif val and flag == 3:                                                                 # O(1)
                print('Успешная авторизация')                                                       # O(1)
                flag = 0                                                                            # O(1)
                return True                                                                         # O(1)
            elif val == False and flag == 3:                                                        # O(1)
                print('Необходима активации учётной записи, обратитесь к неизвестному существу')    # O(1)
                flag = 0                                                                            # 0(1)
                return False                                                                        # O(1)
            else:                                                                                   # O(1)
                flag = 0                                                                            # O(1)
            flag += 1                                                                               # O(1)
    print('Связка логин и пароль не существует')                                                    # O(1)
    return False                                                                                    # O(1)


if __name__ == '__main__':
    auth_dict = {'user_1': {'login': 'pipl_1', 'password': 'fhdjdjdj', 'activate_status': True},
                 'user_2': {'login': 'pipl_2', 'password': 'ftetsttst', 'activate_status': False},
                 'user_3': {'login': 'pipl_3', 'password': 'uiyiu', 'activate_status': True}
                 }
    user_verification_v1('pipl_2', 'ftetsttst', auth_dict)
    user_verification_v2('pipl_2', 'ftetsttst', auth_dict)

"""
Для решения задачи подходит v_1, сложность операций линейная и меньше операций по сравнению с v_2.
В version_2 сложность квадратичная.
"""
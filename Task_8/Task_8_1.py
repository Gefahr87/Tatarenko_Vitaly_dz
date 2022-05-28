'''
Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
    email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
    email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном
выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
'''
import re

user_name = []
dict_of_email = {}
str_of_email = 'edyth.schroeder@hotmail.com laurel6@yahoo.ru.com lexi.bednar@yahoo.com reilly_crona@yahoo.com ' \
                    '@yahoo.com crystel-kerluke73@yahoo.com elian12@yahoo.ru sabina16@hotmail.com ' \
                    'berniece3gmail.com raden_reilly@gmail jannie_schmitt@gmail.com trace.nolan@hotmail.com ' \
                    'gage.dickinson@yahoo.com guiseppe.kulas16@gmailcom octavia_hayes37@yahoo.com ' \
                    'arlene.schamberger38@gmail.com daniela69@yahoo.com.ru joanne_fisher94@gmail.com ' \
                    'ludie73@hotmail.com josianne_weissnat8@gmailcom test@test.net '

RIGHT_ADRESS = re.compile(r'[a-z0-9]*[\._-]*[a-z0-9]+@\w+\.\w+\s', re.IGNORECASE)

# lst_of_email = re.findall(RIGHT_ADRESS, str_of_email)
# print(*lst_of_email, sep='\n')
# print(len(lst_of_email))

RIGHT_ADRESS = re.compile(r'\w+\S\w+@\w+\.\w+$', re.IGNORECASE)
USER_NAME = re.compile(r'^[a-z0-9-]+[.\w-]+', re.IGNORECASE)
DOMAIN_NAME = re.compile(r'([a-z0-9-]+(\.[a-z]{2,})+)$', re.IGNORECASE)
i = 0
for email in str_of_email.split():
    if re.match(RIGHT_ADRESS, email):
        i += 1
        result = re.match(RIGHT_ADRESS, email)
        user_name = re.match(USER_NAME, result.group(0))
        domain_name = re.search(DOMAIN_NAME, result.group(0))
        dict_of_email[result.group(0)] = {'user_name': user_name.group(), 'domain_name': domain_name.group()}
        print(email, '\n', dict_of_email[result.group(0)])
print(i)


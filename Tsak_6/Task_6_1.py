'''
Не используя библиотеки для парсинга, распарсить (получить определённые данные)
файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'), ...
]
'''

import requests

def html_parsing(link, name_files):
    # 0 элемент - <remote_addr>
    # 5 элемент - <request_type>
    # 6 элемент - <requested_resource>
    next_split = []
    req_answer = requests.get(link)
    inform_content = str(req_answer.content)
    massive = inform_content.split('\\n')
    for el in massive:
        next_split.append(el.replace("b'", "").replace('"', "").split())
    with open(name_file, 'w', encoding='utf-8') as f:
        for i in range(len(next_split) - 1):
            next_split[i] = (next_split[i][0], next_split[i][5], next_split[i][6])
            f.write(str(next_split[i]))
            f.write('\n')
    return

if __name__=='__main__':
    link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    name_file = 'nginx_logs.txt'
    html_parsing(link, name_file)

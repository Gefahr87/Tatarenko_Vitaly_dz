'''
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов;
код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
'''
idx = 0
parsing_massive = []
max_spam = []
spam_dict = {}
sort_max_spam = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    data_file = f.readline()
    sym = ['(', ')', "'", ',']
    while data_file:
        for i in range(len(sym)):
            data_file = data_file.replace(sym[i], '')
        parsing_massive.extend(data_file.split())
        if parsing_massive[idx] not in spam_dict:
            spam_dict[parsing_massive[idx]] = 1
        else:
            spam_dict[parsing_massive[idx]] = spam_dict[parsing_massive[idx]] + 1
        # massive_dict[massive[idx]] = massive.count(massive[idx]) # надо заменить, очень грузит систему
        idx += 3
        data_file = f.readline()
max_spam = sorted(spam_dict.values(), reverse=True)
more_1000 = 0
for el in max_spam:
    if el >= 1000:
        more_1000 += 1
for idx in range(more_1000):
    for k, v in spam_dict.items():
        if v == max_spam[idx]:
            sort_max_spam[k] = v
print('Более 1000 запросов было от:', *sort_max_spam.items(), sep='\n')





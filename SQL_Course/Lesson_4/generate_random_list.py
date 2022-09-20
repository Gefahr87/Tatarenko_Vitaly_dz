import random as rndm
import datetime


##################################### Вычсление случайной даты в диапозоне #############################################
def list_of_date(start: list = [2000, 1, 1], end: list = [2099, 12, 31], amount_date: int = 20) -> list:
    list_of_random_date = []
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)
    time_interval = end_date - start_date

    first_date = datetime.date(1970, 1, 1)
    second_from_firstdate = (
            start_date - first_date).total_seconds()  # вычисляем сколко секунд прошло с 1970 по начальный
    # интервал star_date, чтобы случанйая дата всегда была
    # в нужном интервале

    for _ in range(amount_date):
        new_interval_sec = rndm.randint(0, int(time_interval.total_seconds()))
        # list_of_random_date.append(datetime.date.utcfromtimestamp(second_from_firstdate + new_interval_sec))
        list_of_random_date.append(datetime.date.fromtimestamp(second_from_firstdate + new_interval_sec))
    return list_of_random_date


########################################################################################################################

image_id = list(range(1, 14))
image_id.append('Null')
user_id = list(range(314, 334))
[user_id.append(el) for el in (1, 2, 45, 55)]
post_access = list(range(1, 5))
gender = ['f', 'm', 'x']
country = str('Бенин Вануату Великобритания Гвинея Греция Израиль Италия Кения Того Узбекистан').split(' ')
country.append('')
city = str('Вэйхай Кобе Кёльн Линьчжоу Ноябрьск Раджкот Сиань Сувон Цзямусы Эрбиль').split(' ')
city.append('')


# print(rndm.sample(user_id, 20))
# print(rndm.sample(image_id, 13))
# print(rndm.sample(post_access, 4))

# for _ in range(int(100 / 4)):
#     print(list(zip(rndm.sample(user_id, 20), rndm.sample(image_id, 13), rndm.sample(post_access, 4))))
#
# print(*list_of_date(), sep='\n')

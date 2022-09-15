import random as rndm
import datetime

start_date = datetime.date(2000, 1, 1)
end_date = datetime.date(2099, 12, 31)
time_interval = end_date - start_date
print(datetime.datetime.fromtimestamp(time_interval.total_seconds()))
print((start_date + time_interval))

# print(rndm.randint(1, time_interval))


# image_id = list(range(1, 14))
# user_id = list(range(314, 334))
# post_access = list(range(1, 5))
#
# [user_id.append(el) for el in (1, 2, 45, 55)]
#
# # print(rndm.sample(user_id, 20))
# print(rndm.sample(image_id, 13))
# print(rndm.sample(post_access, 4))
#
#
# for _ in range(int(100/4)):
#     print(list(zip(rndm.sample(user_id, 20), rndm.sample(image_id, 13), rndm.sample(post_access, 4))))
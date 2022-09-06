import random as rndm

image_id = list(range(1, 14))
user_id = list(range(314, 334))

[user_id.append(el) for el in (1, 2, 45, 55)]

print(rndm.sample(user_id, 20))
print(rndm.sample(image_id, 13))
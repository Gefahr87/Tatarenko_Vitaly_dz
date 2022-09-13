import random as rndm

image_id = list(range(1, 14))
user_id = list(range(314, 334))
post_access = list(range(1, 5))

[user_id.append(el) for el in (1, 2, 45, 55)]

print(rndm.sample(user_id, 20))
print(rndm.sample(image_id, 13))
print(rndm.sample(post_access, 4))

for _ in range(int(100/4)):
    print(list(zip(rndm.sample(user_id, 20), rndm.sample(image_id, 13), rndm.sample(post_access, 4))))
import random

ret=random.random()
print(ret)

print(random.randint(1,4))
print(random.randrange(1,4))
print(random.choice([1,4,11,2,23,44]))
print(random.sample([1,4,11,2,23,44], 2))

print(random.uniform(1,4))

ls = [1,4,11,2,23,44]
random.shuffle(ls)
print(ls)

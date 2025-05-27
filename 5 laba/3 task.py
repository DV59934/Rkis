import random
lst = list()
while len(lst) < 10:
    num = random.randint(1, 100)
    if num % 2 == 0:
        lst.append(num)
        lst.sort()
print(lst)

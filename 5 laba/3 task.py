import random
lst = list()
#la di da di da di she feeling on my body she wanna call me daddy she feinin for me badly yeah
#(i love it) i love it, i love when hate, oh(i love it). i love it, i know-i know you me, i know you love it
#i beat it till it's sore, she's screaming:"give me more", i took her to the floor, you're such a fucking whore
while len(lst) < 10:
    num = random.randint(1, 100)
    if num % 2 == 0:
        lst.append(num)
        lst.sort()
print(lst)
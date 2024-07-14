import itertools

words = "1234567890abcdefghijklmnopqrstuvwxyz"
r = itertools.product(words, repeat=8)

with open("pwd.txt", "a") as dic:
    for i in r:
        dic.write("".join(i) + "\n")

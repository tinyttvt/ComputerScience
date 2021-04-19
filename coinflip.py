import random

for i in range(1, 201):
    number = random.randint(1, 2)
    if number >= 2:
        print("heads")
    else:
        print("tails")
    
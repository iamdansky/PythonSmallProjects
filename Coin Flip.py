import random
def coin_flip():
    i = random.randint(1, 2)
    return print("Heads") if i == 1 else print("Tails")
coin_flip()

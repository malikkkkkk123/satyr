import random

def gen_pass(pass_length):
    variabel = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(variabel)

    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
    


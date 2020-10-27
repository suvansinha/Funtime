import random

coin = ["Heads","Tails"]
toss = random.choice(coin)

your_call = input("Heads or Tails: ")

if your_call == toss:
    print("It is",toss,",you win!")
else:
    print("It is",toss,",you lose!")
    
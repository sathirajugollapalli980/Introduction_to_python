import random

secret = random.randint(1,50)
attempts = 0

while attempts < 7:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Bravo! Found in", attempts, "attempts")
        break

if attempts == 7 and guess != secret:
    print("You lost! The secret number was", secret)
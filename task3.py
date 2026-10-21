import random
secret = random.randint(1, 20)
attempts = 0
MAX_ATTEMPTS = 5
while attempts < MAX_ATTEMPTS:
    attempts += 1

    guess = int(input("Guess a number between 1 and 20: "))

    if guess == secret:
        print(f"Wowww Correct! You took {attempts} guesses.")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

else:
    print(f"Opps!! Sorry You ran out of attempts. The answer was {secret}.")
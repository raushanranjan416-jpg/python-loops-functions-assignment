import random

random_num = random.randint(1, 100)
guess_number = 0
while True:
    try:
        if guess_number == 0:
            print(f"Guess the number between 1 to 100.")
            guess_number = int(input("Guess the number between 1 to 100."))
        elif guess_number > random_num: 
            print(f"Too High:  {guess_number}, Guess the number again between 1 to 100.")
            guess_number = int(input("Too High, Guess the number again between 1 to 100."))
        elif guess_number < random_num:
            print(f"Too Low {guess_number}, Guess the number again.")
            guess_number = int(input("Too Low, Guess the number again between 1 to 100."))
        elif guess_number == random_num:
            print(f"Bingo, you guess it correct.")
            break
    except ValueError:
        print("Error: Please enter a valid number")

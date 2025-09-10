""" def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True    """
    
    
import random
easy_level = 10
hard_level = 5
# def for checking the user against the answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
# function for set difficulty      
def set_difficulty():
    level = input("Choose a difficulty. type 'easy' or 'hard': ") .lower()
    if level == "easy":
        return easy_level
    else:
        return hard_level
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    answer = random.randint(1, 100)
    
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make guess: "))
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You run out of guessing. You lose.")
            return
        elif guess != answer:
            print("Guess again.\n")

game()               
  
               
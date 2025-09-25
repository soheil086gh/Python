import random

# Sample data (replace with full dataset like in the course)
data = [
    {"name": "Instagram", "follower_count": 600, "description": "Social media platform"},
    {"name": "Cristiano Ronaldo", "follower_count": 580, "description": "Footballer"},
    {"name": "Ariana Grande", "follower_count": 350, "description": "Musician"},
    {"name": "Dwayne Johnson", "follower_count": 340, "description": "Actor"},
]

def get_random_account():
    return random.choice(data)
def format_account(account):
    return f"{account['name']}, {account['description']}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_account(account_a)}")
        print("VS")
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, a_followers, b_followers)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
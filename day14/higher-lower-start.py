import random
import art
from game_data import data


def get_random():
    return random.choice(data)


def is_correct(option, option_a, option_b):
    if option_a > option_b:
        return option == 'a'
    else:
        return option == 'b'


def game():
    print(art.logo)
    points = 0
    is_over = False
    option_b = get_random()

    while not is_over:
        option_a = option_b
        option_b = get_random()

        while option_a == option_b:
            option_b = random.choice(data)

        print(f"Option A: {option_a['name']}, a {option_a['description']}, from {option_b['country']}")
        print(art.vs)
        print(f"Option B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
        select_option = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct = is_correct(select_option, option_a['follower_count'], option_b['follower_count'])

        print(art.logo)
        if correct:
            points += 1
            print(f"You're right! Current score: {points}.")
        else:
            is_over = True
            print(f"Sorry, that's wrong. Final score: {points}")


game()

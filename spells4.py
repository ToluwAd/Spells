"""
This program awards a user points depending on how fast he types a spell
Author: Adejumo Toluwani
When: February 17th, 2023.
"""
import random
import time


def read_spells(filename):
    """
    Reads spells from a file and returns a list of spells.
    """
    with open(filename, 'r') as file:
        spells = [line.strip() for line in file]
    return spells


def get_random_spell(spells):
    """
    This function picks out a spell at random from the file
    """
    spell = random.choice(spells)
    return spell


def display_header():
    """
    This function displays the header for the output
    """
    asterisks = "*" * 60
    Statement = "Harry Potter Keyboard Trainer"
    print(f"{asterisks} \n{Statement} \n{asterisks}")


def display_instructions():
    """
    This function displays the instructions of the user's task
    """
    file = open('instructions.txt', 'r')
    text = file.readlines()
    for i in text:
        print(i, end="")
    print("")


def feedback(spell: str, user_input: str):
    """
    This function checks if the user's input was right or wrong
    """
    if spell.strip().lower() == user_input.lower():
        print("Correct!", end="")
        return True
    else:
        print(f"Incorrect! \nThe spell was: {spell}", end="")
        return False
    pass


def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time


def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    target_typing_time = round(len(spell) * 0.3, 2)
    return target_typing_time


def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
    target_time = get_target_time(spell)
    time_ratio = user_time / target_time
    if user_input == spell:
        if time_ratio <= 1:
            return 10
        elif time_ratio <= 1.5:
            return 6
        elif time_ratio <= 2:
            return 3
        else:
            return 1
    else:
        return -5


def play_again():
    """
    Asks the user if they want to play again.
    Returns True if the user wants to play again, False otherwise.
    """
    response = input("Do you want to play again? (y/n)\n")
    return response.lower() == "y"


def main():
    """
    This function prints out the users score based on his response time.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    score = 0
    play_game = True
    while play_game:
        spell = get_random_spell(spells).lower()
        user_input, user_time = get_user_input(spell)
        points = calculate_points(spell, user_input.lower(), user_time)
        score += points
        if points > 0:
            print("Correct!")
        else:
            print(f"Incorrect!\nThe spell was: {spell}.")
        print(f"You got {points} points! Your score is {score}")
        play_game = play_again()
    print(f"Your final score is: {score}")


main()

"""
This program awards the user points for getting a spell correct and docks points for a wrong spell
Author: Adejumo Toluwani
When: February 17th, 2023.
"""
import random


def read_spells(filename: str):
    """This function reads the contents of a file into a list"""
    file = open(filename, 'r')
    text = file.readlines()
    return text


def get_random_spell(spells):
    """
    This function picks out a spell at random from the file
    """
    spells = random.choice(spells)
    return spells


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


def get_user_input(spells: str):
    """
    This function gets the user's spell input
    """
    print(f"Type the following spell: {spells}", end="")
    user_input = input("")
    return user_input


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


def play_again():
    """
    This function asks the user if he would like to plat the game again
    """
    while True:
        user_question = input("Do you want to practice more? (y/n)\n").lower()
        if user_question.lower() == 'y':
            return True
        elif user_question.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'")


def main():
    """
    This function prints out all the previously mentioned functioned plus a scoring system
    """
    spells = read_spells("spells.txt")
    display_header()
    display_instructions()
    score = 0
    play_game = True
    while play_game:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        score_change = feedback(spell, user_input)
        if score_change == True:
            score += 10
            print(f"\nYou get 10 points! Your score is: {score}")
        else:
            score -= 5
            print(f"You lose! Your score is: {score}")
        play_game = play_again()
    print(f"Your final score is {score}")


main()

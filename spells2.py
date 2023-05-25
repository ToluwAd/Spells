"""
This program checks if a user's spell matches the spell chosen at random
Author: Adejumo Toluwani
When: February 10th, 2023.
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


def get_user_input(spells: str):
    """
    This function gets the user's spell input
    """
    print(f"\nType the following spell: {spells}", end="")
    user_input = input("")
    return user_input


def feedback(spell: str, user_input: str):
    """
    This function checks if the user's input was right or wrong
    """
    if spell.strip().lower() == user_input.strip().lower():
        print("Correct!")
    else:
        print(f"Incorrect! \nThe spell was: {spell}")


def main():
    """
    This function prints out all the previously mentioned functioned
    """
    spells = read_spells("spells.txt")
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    feedback(spell, user_input)


main()

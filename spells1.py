"""
This program prints out a random spell from a list
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


def main():
    """
    This function prints out the spell gotten at random
    """
    spells = read_spells("spells.txt")
    print("Harry Potter Keyboard Trainer")
    spell = get_random_spell(spells)
    print(spell)


main()

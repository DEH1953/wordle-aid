# tools.py
import re


def display_menu():
    print("\n\n            Wordle Helper")
    print("----------------------------------------")
    print("Q - Quit Program")
    print("D - Display Current Wordle Word List")
    print("L - Reduce Wordle List to words with ")
    print("      Located letters")
    print("E - Remove words from Wordle List that")
    print("      have eliminated letters")
    print("----------------------------------------\n")
    response = input("What would you like to do?\n(Q, D, L, E):  ")
    return response.upper()


def reduce_list_by_located_letters(current_list):
    print("================================================================")
    print("Enter the RegEx search pattern as follows:")
    print("For every unused letter, enter a period")
    print("and for every located letter enter the actual letter.")
    print("\nFor example, if the guess was THICK and the answer was TWINS,")
    print("the RegEx search pattern would be T.I..")
    print("================================================================")
    pattern = input("\nEnter the RegEx pattern to match (?????):\n").upper()

    new_list = []
    for word in current_list:
        if re.search(pattern, word):
            new_list.append(word)
    return new_list


def display_current_words(current_list):
    print("\n========= CURRENT WORDS ============")
    for word in current_list:
        print(word)
    print("====================================\n\n")
    return


def OLD_reduce_list_of_eliminated_letters(current_list):

    possible_words = []

    print("\n====================================\n\n")
    print("Enter the eliminated letter followed by ")
    print("the position of the letter in the word.")
    print("Remember, position begins with zero.")
    resp = input(":  ").upper()
    letter = resp[0]
    position = int(resp[1])

    for word in current_list:
        if word[position] == letter:
            print(f"Eliminating: {word}")
        else:
            print(f"Keeping: {word}")
            possible_words.append(word)
    return(possible_words)


def reduce_list_of_eliminated_letters(current_list):
    possible_words = []

    print("\n====================================\n\n")
    print("Enter the letter to be eliminated")
    print("Next enter a pattern for letter elimination")
    print("Use a period to allow that letter to appear")
    print("in that position. Use a ? to delete the ")
    print("letter from all words with it in that position")
    print("For example: to disallow words using the letter e")
    print("in all positions except for the middle spot")
    print("you would enter ??.?? as the pattern.")

    letter = input("What is the letter:  ").upper()
    pattern = input("What is the deletion pattern:   ")

    for position in range(5):
        if pattern[position] == "?":
            for word in current_list:
                if word[position] == letter:
                    print(f"Eliminating: {word}")
                    current_list.remove(word)

    return(current_list)

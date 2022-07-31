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


def reduce_list_by_located_letters(orig_string):
    print("================================================================")
    print("Enter the RegEx search pattern as follows:")
    print("For every unused letter, enter a period")
    print("and for every located letter enter the actual letter.")
    print("\nFor example, if the guess was THICK and the answer was TWINS,")
    print("the RegEx search pattern would be T.I..")
    print("================================================================")
    regex_str = input("\nEnter the RegEx pattern to match (?????):\n").upper()
    regex_str += ','

    search_results = re.findall(regex_str, orig_string.upper())
    new_string = ""
    if search_results:
      for item in search_results:
        new_string += item + " "
    return new_string


def display_current_words(word_string):
    word_str = list(word_string.split(", "))
    print("\n========= CURRENT WORDS ============")
    for word in word_str:
        print(word)
    print("====================================\n\n")
    return(word_str)


def reduce_list_of_eliminated_letters(current_string):
    print("Just a moment. Working")
    return(current_string)

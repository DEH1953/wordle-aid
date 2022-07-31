# wordle-aid.py

import re
from wordle_list import wordle_list
from wordle_list import wordle_string

# Program
# Loop until quit
# Make choices from menu
# Menu Content
# Quit
# Display word list
# Reduce list to only words with RegEx Matches
# Reduce list by removing all words that use eliminated letters

# Ask for located letters and reduce word list to only RegEx matches
# Keep track of position of located letters so that position can be skipped
# when reducing by eliminated letters
# Ask for eliminated letters and reduce word list by removing words that
# contain eliminated letters
# Loop until guesses > 6 or word is revealed.




response = input("Did your guess contain any letters used that were \nin the correct location? (Y/N)   ").lower()

if response == "y":
    print("================================================================")
    print("Enter the RegEx search pattern as follows:")
    print("For every unused letter, enter a period")
    print("and for every located letter enter the actual letter.")
    print("\nFor example, if the guess was THICK and the answer was TWINS,")
    print("the RegEx search pattern would be T.I..")
    print("================================================================")
    regex_str = input("\nEnter the RegEx pattern to match (?????):\n").upper()
    regex_str += ','

    search_results = re.findall(regex_str, wordle_string.upper())
    new_string = ""
    if search_results:
      for item in search_results:
        new_string += item + " "
      print(new_string)
else:
  print("No match")


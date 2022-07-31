# wordle-aid.py

import re
from wordle_list import wordle_list
from wordle_list import wordle_string

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
else:
  print("No match")

print(new_string)

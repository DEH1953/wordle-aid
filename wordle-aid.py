# wordle-aid.py

from wordle_list import wordle_list
from wordle_list import wordle_string
import tools

# prepare the system
orig_string = wordle_string.upper()
current_string = ""

running = True
response = tools.display_menu()

while running:
  if response == "Q":
    running = False
  elif response == "L":
    running = True
    current_string = tools.reduce_list_by_located_letters(orig_string)
    response = tools.display_menu()
  elif response == "D":
    running = True
    if current_string !="":
      current_string = tools.display_current_words(current_string)
    else:
      print("Empty Word List")
    response = tools.display_menu()
  elif response == "E":
    running = True
    if current_string !="":
      current_string = tools.reduce_list_of_eliminated_letters(current_string)
    else:
      print("Empty Word List")
    response = tools.display_menu()
  else:
    response = tools.display_menu()


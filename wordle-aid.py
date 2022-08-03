# wordle-aid.py

from wordle_list import wordle_list
import tools

# prepare the system
current_list = []
for word in wordle_list:
  current_list.append(word)

running = True
response = tools.display_menu()

while running:
  if response == "Q":
    running = False

  elif response == "L":
    running = True
    current_list = tools.reduce_list_by_located_letters(current_list)
    response = tools.display_menu()

  elif response == "D":
    running = True
    tools.display_current_words(current_list)
    response = tools.display_menu()

  elif response == "E":
    running = True
    current_list = tools.reduce_list_of_eliminated_letters(current_list)
    response = tools.display_menu()

  else:
    running = True
    response = tools.display_menu()


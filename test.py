wordle_list = ["ABIDE", "ABLED", "ABODE", "ABORT", "ABOUT", "ABOVE", "ABUSE", "ABYSS", "ACORN", "ACRID", "ACTOR", "ACUTE", "ADAGE", "ADAPT", "ADEPT", "ADMIN"]

# prepare the system
current_list = []
for word in wordle_list:
  current_list.append(word)

print("Original List")
for word in current_list:
  print(word)
  
def reduce_list_of_eliminated_letters(current_list):

    new_list = []

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

    for position in range(len(pattern)):
        if pattern[position] == "?":
            for word in current_list:
                if word[position] != letter:
                    new_list.append(word)
            current_list = []
            for word in new_list:
                current_list.append(word)
            new_list = []

    return(current_list)

  
current_list = reduce_list_of_eliminated_letters(current_list)

print("Edited List")
for word in current_list:
	print(word)

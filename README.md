Script to help solve Wordle puzzles.

User starts game and makes first guess. Then user enters the response as to status of letters entered in an attempt to narrow the dictionary of legal Wordle choices.

User makes second guess using the reduced list and game continues until six guesses or solution is found.''

Reducing the list
1  - For letters used and in the correct position, do a regex findall to match the patter (. means any one letter)

2 - For letters that are not used, further reduce the word list by deleting any word that needs these forbidden letters
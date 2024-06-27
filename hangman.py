
import random
from words import words

chosen_word = random.choice(words)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from logo import logo,stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    
    if guess in display:
        print(f"You've Already Guessed the letter {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'You Guessed {guess},which is not in the word.You Lost a life!')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
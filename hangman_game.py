import random

#list of potential secret words
word_list = ["python", "hangman", "programming", "challenge"]
#Randomly select a secret word from the list
secret_word = random.choice(list)
#Initialize variables to keep track of guesses and attempts
correct_guesses = set()
incorrect_guesses = set()
attempts_left = 6

#Function to display the current game state
def display_game_state():
    #Display the secret word with guessed letters revealed


import random
import sys


# lets set some variables
wordList = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]

guess_word = []
secretWord = random.choice(wordList) # lets randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def change():

    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)
    guessing()


def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = raw_input("Pick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Invalid Input !! Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already guessed that letter!")
        else: 
            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): #This Part I just don't get it
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won! The word was %s"%secretWord)
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was",         secretWord)





def exec_hangman():
    change()
    print("Game Over!")
    

#Word Jumble
#The computer picks a random word and then "jumbles" it
#The player has to guess the original word

import random

def exec_word_jumble():
    #create a sequence of words to choose from
    WORDS= ("python",
            "easy",
            "great")
    
    #The Hints
    HINTS=("a snake",
           "that was so...",
           "better than good")
    
    #pick one word randomly from the sequence
    word=random.choice(WORDS)
    
    #Order the hints to the words
    if word==WORDS[0]:
        i=0
    elif word==WORDS[1]: 
        i=1
    else:
        i=2
        
    #create a variable to use later to see if the guess is correct
    correct=word
    
    #create a jumbled version of the word
    jumble=""
    while word:
        position=random.randrange(len(word))
        #return randomly selected elements from word
        jumble+=word[position] # adding value of the index `position` to jumble
        word=word[:position]+word[(position+1):]
    # items from the beginning through position-1 # items position+1 through the rest of the array
    #start the game
    print(
        """
             Welcome to WORD JUMBLE!
    
        Unscramble the letters to make a word. GOOD LUCK!
        (Press enter at the prompt to quit.)
    """
    )
    
    print("The jumble is: ", jumble)
    a=b=0
    
    #Guessing mechanism
    guess=raw_input("\nYour guess: ")
    b+=1
    
    while guess!=correct and guess!="" and guess!="hint" and b<=10:
        print("That's not it! Enter 'hint' to get a hint")
        guess=raw_input("Your guess: ")
        b+=1
    if guess=="hint":
        print ("THE HINT: ",HINTS[i])
        a+=1
        
    while guess!=correct and guess!="" and b<=10:
        guess=raw_input("Your guess: ")
        b+=1
    
     
    #Correct answser     
    if guess==correct:
        
        print("That's it! You guessed it.\n")
    if a:
        print ("But you needed a tip!")
    else:
        print("Great! You didn't even need a tip!")
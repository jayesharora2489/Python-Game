import Project2
import Project3
import hangman2

while(True):
    print(
        """
1. Hangman
2. Word Jumble
3. Quiz
4. Exit
        """
        )
    
    choice=input("Enter your choice:")
    
    if(choice==1):
        hangman2.exec_hangman()
    elif(choice==2):
        Project2.exec_word_jumble()
    elif(choice==3):
        Project3.exec_quiz()
    elif(choice==4):
        break
    else:
        print('Invalid Option')
import random

# Dictionary of questions and answers

questions = {
            'Who is president of USA?':
            ('\na. Charles Darwin\nb. Donald Duck\nc. Donald Trump\nd. Barack Obama\n', 'c'),
            'What is the capital of USA?':
            ('\na. Zimbabwe\nb. New York\nc. Washington\nd. Do not exist', 'c'),
            'How many books are there in Harry Potter series?':
            ('\na. 1\nb. 3\nc. 5\nd. 7', 'd'),
            'The polar bear is a native of which of these regions?':
            ('\na. Antarctica\nb. Arctic\nc.Central America \nd.Alaska', 'b'),
            'Which Pokemon evolves into Raichu?':
            ('\na. Pikachu\nb. Squirtle \nc. Bulbasaur \nd. Charizard', 'a')
            }

def ask_question(questions):
    '''Asks random question from 'questions 'dictionary and returns
       players's attempt and correct answer.'''

    item = random.choice(list(questions.items()))
    #items() is a method returns a list of tuple pairs
    #random.choice(seq) : Return a random element from the non-empty sequence seq
    question = item[0]
    (variants, answer) = item[1]
    print(question, variants)
    attempt = raw_input('\nEnter \'a\', \'b\', \'c\' or \'d\' for your answer\n')
    return (attempt, answer)


def exec_quiz():
    # Questions loop
    tries = 0
    for questions_number in range(5):
        while True: # Asking 1 question
            attempt, answer = ask_question(questions)
            if attempt not in {'a', 'b', 'c', 'd'}:
                print("INVALID INPUT!!!")
            elif attempt == answer:
                print('Correct')
                stop_asking = False
                break
            elif tries == 1: # Specify the number of tries to fail the answer        
                print('Incorrect!!! You ran out of your attempts')
                stop_asking = True
                break
            else:
                tries = tries + 1
                print('Incorrect!!! Try again.')
        if stop_asking:
            break
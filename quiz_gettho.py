import random

print('welcome to random quiz')
#name = input ('please enter your name:')
#level = input('difficulty level E/M/H/G:')

def gettho_nine_plus_ten():
    print('Gettho question whats 9+10')
    answer = input('>').strip().title()
    print('you answered: ' + answer)

    if answer == '21':
        print('Right!')
        return 1
    elif answer == '19':
        print('19 may be right in your brain but your not thinking gettho enough')
    else:
        print('Wrong!')
        return 0
def nine_plus_ten():
    print('Whats 9+10?')
    answer = input('>').strip().lower()
    print('you answered: ' + answer)

    if answer == '19':
        print('Right!')
        return 1
    elif answer == '21':
        print('Sorry this is not the gettho question')
        return 0
    else:
        print('Wrong!')
        return 0


        
questions = [gettho_nine_plus_ten,
             nine_plus_ten
]

score=0
while questions:
    question = random.choice(questions)
    points = question()
    if points:
        score+=1
        questions.remove(question)
        print("SCORE:",score)

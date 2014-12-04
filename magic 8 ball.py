import random

answers = ['yes.',
           'no.',
           'maybe.'
           'more than you know.'
]
print("welcome to magic 8 ball")
 print(' ask questions for your fate:')
 
while True:
    question = input('>')
    answer = random.choice(answers)
    print(answer)


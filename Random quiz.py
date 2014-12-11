import random
import quiz_gettho as quiz
print('welcome to random quiz')
#name = input ('please enter your name:')

        


score=0
while quiz.questions:
    question = random.choice(quiz.questions)
    points = question()
    if points:
        score+=1
        quiz.questions.remove(question)
        print("SCORE:",score)

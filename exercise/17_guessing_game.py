from random import randint 
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try: 
        print(f'Answer: {answer}')
        guess = int(input(f'Guess a numer between {sys.argv[1]} and {sys.argv[2]} : '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are correct!')
                break
    except ValueError:
        print('Please enter a number')
        continue
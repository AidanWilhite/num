
from hashlib import sha256
import os
from posixpath import split
from flask import Blueprint, render_template, session

Guess = Blueprint('Guess', __name__)


@Guess.route('/')
def index():

    return render_template('html/index.html', Number_Guessed='Please Make A Guess Then Press The Button')


@Guess.route('/<num>')
def UserGuess(num):
    # TODO take this number over to the text file and check if it is th right number!
    if num == 'first':
        return render_template('html/index.html', Number_Guessed='Please Make A Guess Then Press The Button')
    else:

        # read from a file and then find if the number in the file matches the number guessed

        Pnum = num.split('%')[0]

        # print(num)

        path = os.path.abspath('backend\\game\\num.txt')

        with open(path) as f:
            lines = f.read()

        ShaNum = str(sha256(str(Pnum).encode('utf-8')).hexdigest())

        # add one to guesses
        # check if the user can make a new guess

        # CHECK IF THE USER HAS THE SAME ID AS THE DATA BASE

        #print(f'{Pnum} : {num.split("%")} : {len(num.split("%"))} : {num}')

        if len(num.split('%')) == 2:
            if str.split(num, '%')[1] == lines.split('%')[1]:

                print('This user can submit a guess!')

                if lines.split('%')[0] == ShaNum:
                    return render_template('html/SubmitNum.html', Number_Guessed=f'Number {Pnum} is correct!')
                else:
                    return render_template('html/index.html', Number_Guessed=f'You Guessed : {Pnum}', Response=f'{Pnum} is incorrect')

            else:
                # player cant make a new guess
                return render_template('html/index.html', Number_Guessed=f'You did not wait for everybody to make a guess.', Response='As punishment, you loose a turn.')
        else:
            return render_template('html/SubmitNum.html', Number_Guessed=f'There is either an error, or somebody tried to format there own request D:')

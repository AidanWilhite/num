
from hashlib import sha256
import os
from flask import Blueprint, render_template

Set = Blueprint('Set', __name__)


@Set.route('/SetNumber/<num>')
def SetNum(num):
    # Check that it is a number
    try:

        nnum = int(num)

        f = open(os.path.abspath('backend\\game\\num.txt'), 'w')

        sha = str(sha256(str(nnum).encode('utf-8')).hexdigest())
        #sha0 = str(sha256(str(0).encode('utf-8')).hexdigest())

        f.write(f'{sha}%0')

        # return render_template('html/index.html', Number_Guessed='Please Make A Guess Then Press The Button')
        return render_template('html/NewWave.html', Number_Guessed=f'Number {nnum} Has Been Set')

    except:
        return render_template('html/SubmitNum.html', Number_Guessed=f'{num} has not been set because it has whitespace, or it is not a number')


@ Set.route('/SetNumber/')
def SetNumIndex():
    return render_template('html/SetNum.html', SetNum=f'Plese Set A Number In The Box Below')


@ Set.route('/SetNumber/NewWave/')
def NewWave():
    with open(os.path.abspath('backend\\game\\num.txt')) as r:
        lines = r.read()

    w = open(os.path.abspath('backend\\game\\num.txt'), 'w')

    line = lines.split('%')[0] + '%' + str(int(lines.split('%')[1]) + 1)

    w.write(line)

    return render_template('html/NewWave.html', Number_Guessed=f'Everyone can make a another guess now!')

from flask import Flask
import random

app = Flask(__name__)
# constants
HIGH_IMG = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW_IMG = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT_IMG = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
rand_int = random.randint(0, 9)
print(rand_int)


def decorator(function):
    def wrapper(*args, **kwargs):
        if kwargs['number'] < rand_int:
            return function(LOW_IMG)
        elif kwargs['number'] > rand_int:
            return function(HIGH_IMG)
        else:
            return function(CORRECT_IMG)
    return wrapper


@app.route('/')
def title():
    return '<h1>Guess a number between 0 and 9</h1><img ' \
           'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"> '


@app.route('/<int:number>')
@decorator
def num(number):
    return f'<img src="{number}">'


if __name__ == '__main__':
    # Run application in debug mode to autoload our server
    app.run(debug=True)

# class Planet:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in == True:
#             function(args[0])
#
#     return wrapper
#
#
# @decorator
# def named(user):
#     print(f'This user\'s name is {user.name}')
#
#
# planet = Planet('benjamin')
# planet.is_logged_in = False
# named(planet)

#  Do this to run a flask application

# 1. changed shell path to -- C:\WINDOWS\system32\cmd.exe from poweshell.exe
#
# 2. exit from pycharm
#
# 3. open pycharm again from terminal activated environment variable  using - venv\Scripts\activate.bat
#
# 4. installed Flask again. Although pycharm didn't show any red lines .
#
# 5. ran this from terminal set FLASK_APP=main.py
#
# 6. flask run

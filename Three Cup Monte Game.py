#how to shuffle a list

example = [1,2,3,4,5]
from random import shuffle
shuffle(example)
# print(example)

#Three Cup Monte Game

my_list = [' ', 'O',' ']
def shuffle_list(my_list):
    # Take in list, and returned the list
    shuffle(my_list)

    return my_list
# print(my_list)
# print(shuffle_list(my_list))

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        # Recall input() returns a string
        guess = input("Pick a number : 0,1, or 2 " )
    return int(guess)
# print(player_guess())

def check_guess(my_list,guess):
    if my_list[guess] == 'O':
        print('Correct guess!')
    else:
        print('Wrong, Better try next time')
        print(my_list)

# Initial List
mylist = [' ','O',' ']

# Shuffle It
mixed_up_list = shuffle_list(mylist)

# Get User's Guess
guess = player_guess()

# Check User's Guess
#------------------------
# Notice how this function takes in the input
# based on the output of other functions!
check_guess(mixed_up_list,guess)

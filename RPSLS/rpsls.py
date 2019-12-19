import random
def name_to_number(name):
    ''' converting input string to numbers in sequence of 
        rock,spock,paper,lizard,scissors '''
    if name.lower() == 'rock':
        return 0
    elif name.lower() == 'spock':
        return 1
    elif name.lower() == 'paper':
        return 2
    elif name.lower() == 'lizard':
        return 3
    elif name.lower() == 'scissors':
        return 4
    else :
        return 5 
def number_to_name(number):
    ''' converting number back to rock,spock,paper,lizard,scissors'''
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4 :
        return 'scissors'
def rpsls():
    players_choice = input('Player chooses ')
    players_value = name_to_number(players_choice)
    print('Player chooses',player_choice)

    if players_value == 5:
        print('Please select valid name in rpsls')
        return 0

    computer_value=random.randrange(0,5)
    print('Computer chooses',number_to_name(computer_value))
    
    mod_value = (players_value-computer_value)%5
    if mod_value == 0:
        print('Player and Compute tied!')

    elif mod_value == 1 or mod_value == 2:
        print('Player wins!')

    elif mod_value == 4 or mod_value == 3:
        print('Computer wins!')
    print()

for i in range(5):     # playing games for 5 times 
    rpsls()

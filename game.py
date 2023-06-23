import random

reference = {
     'rock':"rock", 
     "r": "rock", 
     'paper': 'paper', 
     'p': 'paper', 
     'sc': 'scissors',
     'scissors': 'scissors', 
     'l': 'lizard',
     'lizard': 'lizard', 
     'sp': 'spock',
     'spock': 'spock',
     'q': 'quit',
     'quit': 'quit',
     'h': 'help',
     'help': 'help'
     }

score = [0,1,2]

quit = False

def check_winner(player1,player2):
    rules = {'rock':{
                    'rock': ['tie'],
                    'paper': ['lose'],
                    'scissors': ['win'],
                    'lizard': ['win'],
                    'spock': ['lose']},
             'paper':{
                    'rock': ['win'],
                    'paper': ['tie'],
                    'scissors': ['lose'],
                    'lizard': ['lose'],
                    'spock': ['win']},
             'scissors':{
                    'rock': ['lose'],
                    'paper': ['win'],
                    'scissors': ['tie'],
                    'lizard': ['lose'],
                    'spock': ['lose']},
             'lizard':{
                    'rock': ['lose'],
                    'paper': ['win'],
                    'scissors': ['lose'],
                    'lizard': ['tie'],
                    'spock': ['win']},
             'spock': {
                    'rock': ['win'],
                    'paper': ['lose'],
                    'scissors': ['win'],
                    'lizard': ['lose'],
                    'spock': ['tie']}
             }
    return rules[player1][player2]


def get_player_input():
    while True:
       user_input = input('Enter your choice: [R]ock, [P]aper, [Sc]issors, [L]izard, [Sp]ock, [Q]uit, or [H]elp ').lower()
       if user_input in reference:
            return reference[user_input]
       print('Please enter a valid choice')


def get_computer_choice():
     return random.choice(('rock', 'paper', 'scissors', 'lizard', 'spock'))

def update_score(score1):
    match score1:
        case 'win':
            score[0] = score[0]+ 1
        case 'lose':
            score[1] = score[1] + 1
        case 'tie':
            score[2] = score[2]+ 1

def game_play():
    player_input = get_player_input()
    if player_input == 'quit':
       quit = True
       pass
       return 'quit'
    computer_choice = get_computer_choice()
    game_check = check_winner(player_input, computer_choice)
    update_score(game_check[0])
    print('End of Game')
    

def driver():
    while quit == False:
       game_play()
    print('game end')


driver()

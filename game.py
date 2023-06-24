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

score = [0,0,0]

quit = False

def check_winner(player1,player2):
    rules = {'rock':{
                    'rock': ['tie', "Rock ties with rock."],
                    'paper': ['lose', "Paper covers rock."],
                    'scissors': ['win', "Rock crushes scissors"],
                    'lizard': ['win', "Rock crushes lizard."],
                    'spock': ['lose', "Spock disintegrates rock."]},
             'paper':{
                    'rock': ['win', "Paper covers rock."],
                    'paper': ['tie', "Paper ties with paper."],
                    'scissors': ['lose', "Scissors cut paper."],
                    'lizard': ['lose', "Lizard eats paper."],
                    'spock': ['win', "Paper disproves Spock."]},
             'scissors':{
                    'rock': ['lose', "Rock crushes scissors."],
                    'paper': ['win', "Scissors cut paper."],
                    'scissors': ['tie', "Scissors tie with paper."],
                    'lizard': ['lose', "Scissors decapitate lizard."],
                    'spock': ['lose', "Spock crushes scissors."]},
             'lizard':{
                    'rock': ['lose', "Rock crushes lizard."],
                    'paper': ['win', "Lizard eats paper."],
                    'scissors': ['lose', "Scissors decapitate lizard."],
                    'lizard': ['tie', "Lizard ties with lizard."],
                    'spock': ['win', "Lizard poisons Spock. "]},
             'spock': {
                    'rock': ['win', "Spock disintegrates rock."],
                    'paper': ['lose', "Paper disproves Spock."],
                    'scissors': ['win', "Spock crushes scissors."],
                    'lizard': ['lose', "Lizard poisons Spock. "],
                    'spock': ['tie', "Spock ties with Spock."]}
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

def get_score():
    return "Wins: {}, Losses: {}, Ties: {}".format(str(score[0]), str(score[1]), str(score[2]))
def game_play():
    player_input = get_player_input()
    if player_input == 'quit':
       quit = True
       return 'quit'
    computer_choice = get_computer_choice()
    game_check = check_winner(player_input, computer_choice)
    update_score(game_check[0])
    print(get_score())
    print(game_check[1])
    print("Would you like to continue?")
    

def driver():
    while not quit: 
      if  game_play() == "quit":
          break;
    print('game end')


driver()

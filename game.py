#Rock, Paper, Scissors Game

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


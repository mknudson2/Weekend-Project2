import random
from random import choice
from random import randint
from tkinter import messagebox
import tkinter as tk

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
          break
    print('game end')

# def on_button_click(row, col):
#     get_player_input = buttons[row][col]['text']
#     get_computer_choice = random.choice(['rock', 'paper', 'scissors','lizard','spock'])
#     messagebox.showinfo("Result", f"Player: {get_player_input}\nComputer: {get_computer_choice}")


#TKINTER
window =tk.Tk()
computer_frame =tk.Frame(window, width=300, height= 200)
center_frame = tk.Frame(window, width=300, height=200)
player_frame = tk.Frame(window, width=300, height= 200)
input = ' '
window.geometry("800x500")
window.title("Rock, Paper, Scissors")

greeting = tk.Label(window, text = "Welcome, combatant!", font=('sans-serif, 20'))
comp_label = tk.Label(computer_frame, text="Computer", padx= 100, pady=100)
resolve = tk.Button(center_frame, text="Resolve")

rock = tk.Radiobutton(player_frame, text="Rock", variable= input, value='rock')
paper = tk.Radiobutton(player_frame, text="Paper", variable= input, value='paper')
scissors = tk.Radiobutton(player_frame, text="Scissors", variable= input, value='scissors')
lizard = tk.Radiobutton(player_frame, text="Lizard", variable= input, value='lizard')
spock = tk.Radiobutton(player_frame, text="Spock", variable= input, value='spock')
match input:
    case "rock": 
        if random.randint(1,10) == 10:
                image_name = "therock.png"
        else:
                image_name = "rock.png"
    case "scissors":
        image_name = "scissors.png" 
    case "paper":
        image_name = "paper.png"
    case "lizard":
        image_name = "lizard.png"
    case "spock":
        image_name = "spock.png"

# buttons={}
# for row in range(5):
#     for col in range(1):
#         button_text = ['rock', 'paper', 'scissors','lizard','spock'][row]
#         buttons[row] = buttons.get(row, {})
#         buttons[row][col] = tk.Button(window, text=button_text, padx=2, pady=1,
#                                      command=lambda r=row, c=col: on_button_click(r, c))
#         buttons[row][col].grid(row=row, column=col)
        

computer_frame.grid(column=0, row=0)
comp_label.grid(column= 0, row=2)

center_frame.grid(column = 1, row = 0)
resolve.grid(column=1, row=2, padx=40, sticky="nsew")

player_frame.grid(column=2, row = 0)
rock.grid(column=1, row=2, padx=20)
paper.grid(column=2, row=2)
scissors.grid(column=3, row=2)
lizard.grid(column=4, row=2)
spock.grid(column=5, row=2)



# greeting.pack()

window.mainloop()

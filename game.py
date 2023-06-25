import random
from random import choice
from random import randint
import tkinter as tk
from PIL import ImageTk, Image

class Help_object:
    def __init__(self, input1):
       self.input1 = input1
    
help_me = Help_object("")

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


#TKINTER
window =tk.Tk()
computer_frame =tk.Frame(window, width=300, height= 200)
center_frame = tk.Frame(window, width=300, height=200)
player_frame = tk.Frame(window, width=300, height= 200)
input1 = ' '
window.geometry("800x500")
window.title("Rock, Paper, Scissors")
image_name= "rock.png"
greeting = tk.Label(window, text = "Welcome, combatant!", font=('sans-serif, 20'))
comp_label = tk.Label(computer_frame, text="Computer:", padx= 200, pady=100, background='red')
player_label = tk.Label(player_frame, text="You:", font=('sans-serif, 16'))
play = tk.Button(center_frame, text="Play", padx= 15, pady=15, activeforeground='red', anchor='center',font=('sans-serif, 14'),bd=0)


#FUNCTIONS PLEASE WORK 
def select_graphic():
    print(help_me.input1)
    match help_me.input1:
        case "rock.png":
            if random.randint(9) == 9:
                img2 = ImageTk.PhotoImage(Image.open("rock.png"))
            else: 
                 img2 = ImageTk.PhotoImage(Image.open("therock.png"))
        case "paper.png":
            img2 = ImageTk.PhotoImage(Image.open("paper.png"))
        case "scissor.jpg":
            img2 = ImageTk.PhotoImage(Image.open("scissor.jpg"))
        case "lizard.png":
            img2 = ImageTk.PhotoImage(Image.open("lizard.png"))
        case "space.png":
            img2 = ImageTk.PhotoImage(Image.open("space.png"))
        case __:
            img2 = ImageTk.PhotoImage(Image.open("lizard.png"))
    player1_image.configure(image=img2)
    player1_image.image = img2
    

def set_input_scissors(event):
    help_me.input1 = "scissor.jpg"
    print(help_me.input1)
    select_graphic()
def set_input_lizard(event):
    help_me.input1 = "lizard.png" 
    print(help_me.input1)
    select_graphic()
def set_input_spock(event):
    help_me.input1 = "space.png" 
    print(help_me.input1)
    select_graphic()
def set_input_rock(event):
    help_me.input1 = "rock.png" 
    print(help_me.input1)
    select_graphic()
def set_input_paper(event):
    help_me.input1 = "paper.png"
    print(help_me.input1)
    select_graphic()
rock = tk.Radiobutton(player_frame, text="Rock", variable= input1, value='rock')
paper = tk.Radiobutton(player_frame, text="Paper", variable= input1, value='paper')
scissors = tk.Radiobutton(player_frame, text="Scissors", variable= input1, value='scissors')
lizard = tk.Radiobutton(player_frame, text="Lizard", variable= input1, value='lizard')
spock = tk.Radiobutton(player_frame, text="Spock", variable= input1, value='spock')


#Image declaration
img = ImageTk.PhotoImage(Image.open(image_name))
player1_image = tk.Label(window, image = img)
# buttons={}

# for row in range(5):
#     for col in range(5):
#         button_text = ['rock', 'paper', 'scissors', 'lizard', 'spock'][row]
#         buttons[row] = buttons.get(row, {})
#         buttons[row][col] = tk.Button(window, text=button_text, padx=20, pady=10,
#                                      command=lambda r=row, c=col: on_button_click(r, c))
#         buttons[row][col].grid(row=row, column=col)
        


computer_frame.grid(column=2, row=0)
comp_label.grid(column= 0, row=2)

center_frame.grid(column =1, row = 0)
play.grid(column=1, row=1, padx=(80,0))

player_frame.grid(column=0, row=11)
rock.grid(column=0, row=12)
paper.grid(column=0, row=13)
scissors.grid(column=0, row=14)
lizard.grid(column=0, row=15)
spock.grid(column=0, row=16)
player_label.grid(column=0, row=0)
player1_image.grid(column=0,row=0, pady=10, padx=10)



rock.bind('<Button-1>', set_input_rock)
paper.bind('<Button-1>',set_input_paper)
scissors.bind('<Button-1>', set_input_scissors)
lizard.bind('<Button-1>', set_input_lizard )
spock.bind('<Button-1>', set_input_spock)
# greeting.pack()

window.mainloop()

import random
from random import choice
from random import randint
import tkinter as tk
from PIL import ImageTk, Image

class Help_object:
    def __init__(self, input1):
       self.input1 = input1
       self.comp_img = ""
       self.oscillate = 0
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



def get_computer_choice():
     help_me.comp_img = random.choice(('rock', 'paper', 'scissors', 'lizard', 'spock'))
     return help_me.comp_img

def update_score(score1):
    match score1:
        case 'win':
            score[0] = score[0]+ 1
        case 'lose':
            score[1] = score[1] + 1
        case 'tie':
            score[2] = score[2]+ 1

def get_score():
    return "Your Score: Wins: {}, Losses: {}, Ties: {}".format(str(score[0]), str(score[1]), str(score[2]))

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
window.geometry("900x500")
window.title("Rock, Paper, Scissors")
image_name= "rock.png"
greeting = tk.Label(window, text = "Welcome, combatant!", font=('sans-serif, 20'))
comp_image_name = "Blank-image.png"
comp_image = ImageTk.PhotoImage(Image.open(comp_image_name))
computer_image_widget = tk.Label(computer_frame, image=comp_image)
computer_label = tk.Label(computer_frame, text="Computer:", font=('sans-serif', 16, "bold" ))
you_label = tk.Label(player_frame, text="You:", font=('sans-serif', 16, "bold" ))
score_label = tk.Label(window, text="Your Score:", font=('sans-serif', 16, "bold"),fg='blue')
game_check_label = tk.Label(window, text="  ", font=('sans-serif', 16, "bold" ),fg='red')
play = tk.Button(center_frame, text="Play", padx= 15, pady=15,  anchor='center',font=('sans-serif', 14, "bold" ),bd=0, activeforeground='red')
again = tk.Button(center_frame, text="Again?", padx= 15, pady=15,  anchor='center',font=('sans-serif', 14, "bold" ),bd=0, activeforeground='red')


def game_play(event):
    if help_me.oscillate == 0:
        help_me.oscillate = 1
        print(help_me.oscillate)
        get_computer_choice()
        match help_me.comp_img:
            case "rock":
                comp_img = ImageTk.PhotoImage(Image.open("rock.png"))
            case "paper":
                comp_img = ImageTk.PhotoImage(Image.open("paper.png"))
            case "scissors":
                comp_img = ImageTk.PhotoImage(Image.open("scissors.jpg"))
            case "spock":
                comp_img = ImageTk.PhotoImage(Image.open("spock.png"))
            case "lizard":
                comp_img = ImageTk.PhotoImage(Image.open("lizard.png"))
            case __:
                comp_img = ImageTk.PhotoImage(Image.open("lizard.png"))
        computer_image_widget.configure(image=comp_img)
        computer_image_widget.image = comp_img
        game_check = check_winner(help_me.input1[:-4], help_me.comp_img)
        update_score(game_check[0])
        score_label.configure(text=get_score())
        score_label.text=get_score()
        game_check_label.configure(text=game_check[1])
        game_check_label.text=game_check[1]
        
        play.configure(text="Again?")
        play.text = "Again?"
        
    else:
        
        help_me.oscillate = 0
        comp_img = ImageTk.PhotoImage(Image.open("Blank-image.png"))
        computer_image_widget.configure(image=comp_img)
        computer_image_widget.image = comp_img
        game_check_label.configure(text="")
        game_check_label.text= ""
        play.configure(text="Play")
        play.text= "Play"
        

#FUNCTIONS PLEASE WORK 
def select_graphic():
    print(help_me.input1)
    match help_me.input1:
        case "rock.png":
            if random.randint(0,10) == 9:
                img2 = ImageTk.PhotoImage(Image.open("therock.png"))
            else: 
                 img2 = ImageTk.PhotoImage(Image.open("rock.png"))
        case "paper.png":
            img2 = ImageTk.PhotoImage(Image.open("paper.png"))
        case "scissors.jpg":
            img2 = ImageTk.PhotoImage(Image.open("scissors.jpg"))
        case "lizard.png":
            img2 = ImageTk.PhotoImage(Image.open("lizard.png"))
        case "spock.png":
            img2 = ImageTk.PhotoImage(Image.open("spock.png"))
        case __:
            img2 = ImageTk.PhotoImage(Image.open("lizard.png"))
    player1_image.configure(image=img2)
    player1_image.image = img2
    

def set_input_scissors(event):
    help_me.input1 = "scissors.jpg"
    print(help_me.input1)
    select_graphic()
def set_input_lizard(event):
    help_me.input1 = "lizard.png" 
    print(help_me.input1)
    select_graphic()
def set_input_spock(event):
    help_me.input1 = "spock.png" 
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



rock = tk.Radiobutton(player_frame, text="Rock", variable= input1, value='rock',font=('sans-serif, 12') )
paper = tk.Radiobutton(player_frame, text="Paper", variable= input1, value='paper',font=('sans-serif, 12'))
scissors = tk.Radiobutton(player_frame, text="Scissors", variable= input1, value='scissors',font=('sans-serif, 12'))
lizard = tk.Radiobutton(player_frame, text="Lizard", variable= input1, value='lizard',font=('sans-serif, 12'))
spock = tk.Radiobutton(player_frame, text="Spock", variable= input1, value='spock',font=('sans-serif, 12'))


#Image declaration
img = ImageTk.PhotoImage(Image.open(image_name))
player1_image = tk.Label(window, image = img)

#player side frame
player_frame.grid(column=0, row=1)
you_label.grid(column=0, row=1)
rock.grid(column=0, row=2)
paper.grid(column=0, row=3)
scissors.grid(column=0, row=4)
lizard.grid(column=0, row=5)
spock.grid(column=0, row=6)


score_label.grid(column=2, row=2, sticky='N')
game_check_label.grid(column=2, row=1)
player1_image.grid(column=0,row=0, sticky='N', padx=20)


#center frame
center_frame.grid(column =1, row = 0)
play.grid(column=1, row=1, padx=(80,0))

#computer side frame
computer_frame.grid(column=2, row=0)
computer_image_widget.grid(column=0, row=2, padx=80)
computer_label.grid(column=0, row=3)


rock.bind('<Button-1>', set_input_rock)
paper.bind('<Button-1>',set_input_paper)
scissors.bind('<Button-1>', set_input_scissors)
lizard.bind('<Button-1>', set_input_lizard )
spock.bind('<Button-1>', set_input_spock)

play.bind('<Button-1>', game_play)

window.mainloop()
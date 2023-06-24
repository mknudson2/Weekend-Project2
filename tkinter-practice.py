from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
def run_window():
    root= Tk()
    root.title("Hello")
    root.geometry("800x500")


    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    img2 = ImageTk.PhotoImage(Image.open('scissor.jpg'))
    Greetings = Label(root,image = img2)
    Greetings.grid(column=2, row=1, sticky=(W, E))


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
    
    root.mainloop()
run_window()
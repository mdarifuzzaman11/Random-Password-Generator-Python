import random
from tkinter import * # create a GUI window
import string


def generate_password(): #generate password
    password = [] # empty list
    for i in range(5): # loop 5 times
        alpha = random.choice(string.ascii_letters) #each character is a random choice from the string.ascii_letters
        symbol = random.choice(string.punctuation) #each character is a random choice from the string.punctuation
        numbers = random.choice(string.digits)#each character is a random choice from the string.digits
        password.append(alpha)#each character is a random choice from the string.ascii_letters
        password.append(symbol) #each character is a random choice from the string.punctuation
        password.append(numbers) #each character is a random choice from the string.digits

    y = "".join(str(x) for x in password) #each character is a random choice from the string.digits
    lbl.config(text=y)  #each character is a random choice from the string.digits 


root = Tk() #creates a window for the program to run in 
root.title("PASSWORD GENERATOR") #title of the window
root.geometry("550x500")    #size of the window
btn = Button(root, text="Generate Password", command=generate_password) #creates a button that generates a password
btn.grid(row=2, column=2) #creates a button that generates a password
lbl = Label(root, font=("times", 15, "bold")) #creates a label that displays the password
lbl.grid(row=4, column=2) #creates a label that displays the password
root.mainloop() #runs the program
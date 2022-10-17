#This is importing the tkinter package and our random number generator.
from tkinter import *
import random

#This will be the window for the dice to be displayed in.
root = Tk()
root.title('DiceBot')
root.geometry("400x450")

#These are our numbers for a standard die roll result (1-6) in unicode (reference in write up).
def get_number(n):
	if n == '\u2680':
		return(1)
	elif n == '\u2681':
		return(2)
	elif n == '\u2682':
		return(3)
	elif n == '\u2683':
		return(4)
	elif n == '\u2684':
		return(5)
	elif n == '\u2685':
		return(6)

#Here will be my definitions for each of my separate die roll displays, their numerical value,
#and the combined total of that numerical value.

def roll_dice():
	die1 = random.choice(die)
	die2 = random.choice(die)

	tdie1 = get_number(die1)
	tdie2 = get_number(die2)

	dice_label1.config(text=die1)
	dice_label2.config(text=die2)

	sub_dice_label1.config(text=tdie1)
	sub_dice_label2.config(text=tdie2)

	total = tdie1 + tdie2
	total_label.config(text=f"Combined Roll = {total}")

#These are the unicode for each die face in my list.
die = ['\u2680', '\u2681','\u2682','\u2683','\u2684','\u2685']

#This is the frame for my display.
my_frame = Frame(root)
my_frame.pack(pady=35)

#These are the titles and colors of each item in my display (dice, button to roll the dice, total)
#First, the details of the dice.
dice_label1 = Label(my_frame, font=("Calibri", 100), fg="Dark Red")
dice_label1.grid(row=0, column=0, padx=5)
sub_dice_label1 = Label(my_frame)
sub_dice_label1.grid(row=1, column=0)

dice_label2 = Label(my_frame, font=("Calibri", 100), fg="Dark Red")
dice_label2.grid(row=0, column=1, padx=5)
sub_dice_label2 = Label(my_frame)
sub_dice_label2.grid(row=1, column=1)

#Then the details of the button.
my_button = Button(root, text="Roll the Dice!", command=roll_dice, font=("Calibri", 20), fg = "black")
my_button.pack(pady=20)

#Lastly, the colour of the total rolls
total_label = Label(root, text="", font=("Calibri", 18), fg="Dark Red")
total_label.pack(pady=10)

#It's ready to be initialized!
roll_dice()
root.mainloop()



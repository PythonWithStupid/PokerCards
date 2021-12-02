#Import the required Libraries
from tkinter import *
import tkinter 
from deck import Deck
from HandChecker import HandChecker
# Local imports

DISPLAY = tkinter.Tk()
CANVAS = Canvas(DISPLAY, width=800, height=600)
CANVAS.pack()

# Initialize the deck
deck = Deck(CANVAS)

# Initialize HandChecker object
hand_checker = HandChecker(deck.all_cards, deck.exposed_cards)
# Configure canvas
CANVAS.configure(background='darkgreen')

deck.draw_hands()
deck.draw_flop()
deck.draw_one(400, 200)
deck.draw_one(520, 200)

hand_checker.is_pair()




DISPLAY.mainloop()


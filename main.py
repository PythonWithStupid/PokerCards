#Import the required Libraries
import random
from tkinter import *
from PIL import Image,ImageTk
from deck import Deck
# Local imports

DISPLAY = Tk()
CANVAS = Canvas(DISPLAY, width=800, height=600)
CANVAS.pack()

def resize_image(images):
    # A list to store resized images.
    resized_images = []
    for image in images:
        resizedImg = image.resize((100, 150), Image.ANTIALIAS)
        newImg = ImageTk.PhotoImage(resizedImg)
        resized_images.append(newImg)
    return resized_images
imageList = [# All the Clubs (2 to King) (13-Cards)
             Image.open('Playing Cards/PNG-cards-1.3/2_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/3_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/4_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/5_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/6_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/7_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/8_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/9_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/10_of_clubs.png'),
             Image.open('Playing Cards/PNG-cards-1.3/jack_of_clubs2.png'),
             Image.open('Playing Cards/PNG-cards-1.3/queen_of_clubs2.png'),
             Image.open('Playing Cards/PNG-cards-1.3/king_of_clubs2.png'),
             Image.open('Playing Cards/PNG-cards-1.3/ace_of_clubs.png'),

            # All the Spades (2 to King) (12-Cards)
            Image.open('Playing Cards/PNG-cards-1.3/2_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/3_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/4_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/5_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/6_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/7_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/8_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/9_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/10_of_spades.png'),
            Image.open('Playing Cards/PNG-cards-1.3/jack_of_spades2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/queen_of_spades2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/king_of_spades2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/ace_of_spades.png'),


            # All the Hearts (2 to King) (13-Cards)
            Image.open('Playing Cards/PNG-cards-1.3/2_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/3_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/4_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/5_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/6_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/7_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/8_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/9_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/10_of_hearts.png'),
            Image.open('Playing Cards/PNG-cards-1.3/jack_of_hearts2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/queen_of_hearts2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/king_of_hearts2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/ace_of_hearts.png'),

            # All the Diamonds (2 to King)
            Image.open('Playing Cards/PNG-cards-1.3/2_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/3_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/4_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/5_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/6_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/7_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/8_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/9_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/10_of_diamonds.png'),
            Image.open('Playing Cards/PNG-cards-1.3/jack_of_diamonds2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/queen_of_diamonds2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/king_of_diamonds2.png'),
            Image.open('Playing Cards/PNG-cards-1.3/ace_of_diamonds.png'),
             ]
def flop():
    resizedCards = resize_image(imageList)

def draw_hands(num_players):
    handPositions = [[(350, 400), (400, 400)]]
    pos = handPositions
    CANVAS.create_image(pos[0][0], anchor=NW, image=resizedCards[secret_number])
    CANVAS.create_image(pos[0][1], anchor=NW, image=resizedCards[secret_number2])
    print(handPositions[0][0])

flop_displayed = False
def key_press(e):
    DISPLAY.bind('<KeyPress>', key_press)
def key_released(e):
    DISPLAY.bind('<KeyRelease>', key_released)


    return None
resizedCards = resize_image(imageList)
deck = Deck(CANVAS)

CANVAS.configure(background='darkgreen')

deck.draw_hands()
deck.draw_flop()
deck.draw_one(300, 200)
deck.draw_one(350, 200)
#Create an instance of tkinter frame



DISPLAY.mainloop()


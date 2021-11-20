import random
from tkinter import *
from PIL import Image, ImageTk

class Deck(object):
    def __init__(self, surface):
        self.surface = surface
        self.background = Image.open('table_felt.jpg')
        # All 52-Playing Cards
        self.images = [  # All the Clubs (2 to King) (13-Cards)
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

        # A list to store resized images.
        self.resized_cards = []
        for image in self.images:
            resizedImg = image.resize((100, 150), Image.ANTIALIAS)
            newImg = ImageTk.PhotoImage(resizedImg)
            self.resized_cards.append(newImg)


        self.calledCards = []

    def draw_hands(self):
        card_one = random.choice(self.resized_cards)
        card_two = random.choice(self.resized_cards)

        handPositions = [[(350, 400), (400, 400)]]
        pos = handPositions
        self.surface.create_image(pos[0][0], anchor=NW, image=card_one)
        self.surface.create_image(pos[0][1], anchor=NW, image=card_two)
        self.calledCards.append(card_one)
        self.calledCards.append(card_two)
        self.resized_cards.remove(card_one)
        self.resized_cards.remove(card_two)
        print(len(self.resized_cards))
    def draw_flop(self):


        card_one = random.choice(self.resized_cards)
        card_two = random.choice(self.resized_cards)
        card_three = random.choice(self.resized_cards)

        self.surface.create_image(150, 200, anchor=NW, image=card_one)
        self.surface.create_image(200, 200, anchor=NW, image=card_two)
        self.surface.create_image(250, 200, anchor=NW, image=card_three)
        self.calledCards.append(card_one)
        self.resized_cards.remove(card_one)
        self.calledCards.append(card_two)
        self.resized_cards.remove(card_two)
        self.calledCards.append(card_three)



        self.resized_cards.remove(card_three)


    def draw_one(self, x, y):
        card_one = random.choice(self.resized_cards)

        self.surface.create_image(x, y, anchor=NW, image=card_one)

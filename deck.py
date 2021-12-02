import random
from tkinter import *
from PIL import Image, ImageTk

class Deck(object):
    
    def __init__(self, surface):
        self.surface = surface
        # All 52-Playing Cards
        self.all_cards = [ 
            # List of Clubs
            ['Graphics/2_of_clubs.png',
            'Graphics/3_of_clubs.png',
            'Graphics/4_of_clubs.png',
            'Graphics/5_of_clubs.png',
            'Graphics/6_of_clubs.png',
            'Graphics/7_of_clubs.png',
            'Graphics/8_of_clubs.png',
            'Graphics/9_of_clubs.png',
            'Graphics/10_of_clubs.png',
            'Graphics/jack_of_clubs2.png',
            'Graphics/queen_of_clubs2.png',
            'Graphics/king_of_clubs2.png',
            'Graphics/ace_of_clubs.png'],

            # List of Diamonds 
            ['Graphics/2_of_diamonds.png',
            'Graphics/3_of_diamonds.png',
            'Graphics/4_of_diamonds.png',
            'Graphics/5_of_diamonds.png',
            'Graphics/6_of_diamonds.png',
            'Graphics/7_of_diamonds.png',
            'Graphics/8_of_diamonds.png',
            'Graphics/9_of_diamonds.png',
            'Graphics/10_of_diamonds.png',
            'Graphics/jack_of_diamonds2.png',
            'Graphics/queen_of_diamonds2.png',
            'Graphics/king_of_diamonds2.png',
            'Graphics/ace_of_diamonds.png'],

            # List of Hearts 
            ['Graphics/2_of_hearts.png',
            'Graphics/3_of_hearts.png',
            'Graphics/4_of_hearts.png',
            'Graphics/5_of_hearts.png',
            'Graphics/6_of_hearts.png',
            'Graphics/7_of_hearts.png',
            'Graphics/8_of_hearts.png',
            'Graphics/9_of_hearts.png',
            'Graphics/10_of_hearts.png',
            'Graphics/jack_of_hearts2.png',
            'Graphics/queen_of_hearts2.png',
            'Graphics/king_of_hearts2.png',
            'Graphics/ace_of_hearts.png'],

            # List of Spades 
            ['Graphics/2_of_spades.png',
            'Graphics/3_of_spades.png',
            'Graphics/4_of_spades.png',
            'Graphics/5_of_spades.png',
            'Graphics/6_of_spades.png',
            'Graphics/7_of_spades.png',
            'Graphics/8_of_spades.png',
            'Graphics/9_of_spades.png',
            'Graphics/10_of_spades.png',
            'Graphics/jack_of_spades2.png',
            'Graphics/queen_of_spades2.png',
            'Graphics/king_of_spades2.png',
            'Graphics/ace_of_spades.png']

        ]
        
        # A list to store resized images. This stores the cards that 
        # are already pulled from the deck and stores them in memory so
        # they can be drawn.
        self.card_images = []
        # A copy of the images list that will be used to remove cards
        # already pulled from the deck.
        self.images_list_cpy = self.all_cards
        # A list to keep track of the exposed cards
        self.exposed_cards = []


    def resize_image(self, image, temp_card_list):
        resizedImg = image.resize((100, 150), Image.ANTIALIAS)
        newImg = ImageTk.PhotoImage(resizedImg)
        temp_card_list.append(newImg)
    
        return newImg


    def select_card(self):
        # Get random suit, then random card from that suit
        suit_selected = random.choice(self.images_list_cpy)
        card_selected = random.choice(suit_selected)

        # Remove card from deck
        self.images_list_cpy = [[card for card in suit if card != card_selected] for suit in self.images_list_cpy]
        # Add card to exposed_cards list
        self.exposed_cards.append(card_selected)
        # Open and resize image
        card_image = Image.open(card_selected)
        resized_card_image = self.resize_image(card_image, self.card_images)

        return resized_card_image


    def draw_hands(self):

        # Selet cards from deck
        card1 = self.select_card()
        card2 = self.select_card()

        # Postional coordinates for player cards on screen (card1), (card2)
        pos = [(350, 400), (400, 400)]
        
        # Draw player cards on screen
        self.surface.create_image(pos[0], anchor=NW, image=card1)
        self.surface.create_image(pos[1], anchor=NW, image=card2)


    def draw_flop(self):
       
        # Selet cards from deck
        card1 = self.select_card()
        card2 = self.select_card()
        card3 = self.select_card()

         # Positional coordinates for flop cards on screen (card1), (card2), (card3)
        pos = [(150, 200), (270, 200), (390, 200)]
       
        # Draw the cards
        self.surface.create_image(pos[0], anchor=NW, image=card1)
        self.surface.create_image(pos[1], anchor=NW, image=card2)
        self.surface.create_image(pos[2], anchor=NW, image=card3)
        

    def draw_one(self, x, y):

        # Selet card from deck
        card = self.select_card()

        # Draw the card
        self.surface.create_image((x + 120), y, anchor=NW, image=card)

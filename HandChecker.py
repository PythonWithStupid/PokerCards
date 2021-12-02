

class HandChecker(object):
    def __init__(self, all_cards, exposed_cards):
        self.high_card = False
        self.pair = False
        self.two_pair = False
        self.three_of_a_kind = False
        self.straight = False
        self.flush = False
        self.full_house = False
        self.four_of_a_kind = False
        self.straight_flush = False
        
        self.all_cards = all_cards
        self.exposed_cards = exposed_cards

        self.exposed_card_coordinates = []

    def find_card_index(self, theList, item):
        for i in range(len(theList)):
            suit = theList[i]
            for j in range(len(suit)):
                if suit[j] == item: 
                    return (i, j)
        
    
    def is_pair(self):
        pair_count = 0
        for card in self.exposed_cards:
            card_coordinate = self.find_card_index(self.all_cards, card)
            self.exposed_card_coordinates.append(card_coordinate)
        
        for i in range(len(self.exposed_card_coordinates)):
            print("i = ", self.exposed_card_coordinates[i][1], "\n")
            for j in range(i+1, len(self.exposed_card_coordinates)):
                print("j = ", self.exposed_card_coordinates[j][1])
                
                # Series of if statements to detect the different pair type hands
                if (self.exposed_card_coordinates[i][1] == self.exposed_card_coordinates[j][1]):
                    pair_count += 1

        if pair_count == 0:
            print("High Card")
        elif pair_count == 1:
            print("One Pair")
        else:
            print("Two Pair")
        
        
        
        
        
        
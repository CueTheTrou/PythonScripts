import random

#Create Deck function
def create_deck():
    suits = ["♥", "♦", "♣", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8",
    "9", "10", "J", "Q", "K", "A"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))

    random.shuffle(deck)
    return deck

#Draw Card function
def draw_card(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        if deck:
            hand.append(deck.pop())
        else:
            break
    return hand, deck

def show_card(card):
    space = " "
    if len(card[1]) == 2:
        space = ""
        print (f"""
        +-------+
        |{card[1]}     {space}|
        |       |
        |   {card[0]}   |
        |       |
        |{space}     {card[1]}|
        +-------+
        """)

deck = create_deck()
while len(deck) > 0:
    num_cards = int(input("How many cards would you like to draw? "))
    if num_cards > len(deck):
        print(f"Only {len(deck)} cards left, drawing all remaining cards.")
        num_cards = len(deck)
    
    hand, deck = draw_card(deck, num_cards)
    for card in hand:
        show_card(card)

print("We are out of cards")

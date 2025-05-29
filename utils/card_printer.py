from utils import baraja_es
from utils import baraja_fr

symbols = {
    "bastos" : "¶",
    "oros" : "O",
    "espadas" : "†",
    "copas" : "Y",
    "picas" : "♠",
    "diamantes" : "♦",
    "tréboles" : "♣",
    "corazones" : "♥"
}

values_fr = {
    1 : "A",
    11 : "J",
    12 : "Q",
    13 : "K"
}

def print_card(card):

    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"

    if card in baraja_fr.deck:
        if card.number == 10:
            number_right = str(card.number)
            number_left = str(card.number)
        else:
            number_right = str(values_fr.get(card.number, str(card.number))) + " "
            number_left = " " + str(values_fr.get(card.number, str(card.number)))

        suit_line = f"│    {symbols.get(card.suit)}    │"
        number_line_left = f"│{number_left}       │"
        number_line_right = f"│       {number_right}│"

        print(top)
        print(number_line_left)
        print(side)
        print(suit_line)
        print(side)
        print(number_line_right)
        print(bottom)
    
    elif card in baraja_es.deck:
        if card.number in [10, 11, 12]:
            number_right = str(card.number)
            number_left = str(card.number)
        else:
            number_right = str(card.number) + " "
            number_left = " " + str(card.number)

        suit_line = f"│    {symbols.get(card.suit)}    │"
        number_line_left = f"│{number_left}       │"
        number_line_right = f"│       {number_right}│"

        print(top)
        print(number_line_left)
        print(side)
        print(suit_line)
        print(side)
        print(number_line_right)
        print(bottom)

if __name__ == "__main__":

    print_card(baraja_es.deck[0])
    print("As de oros")
    print_card(baraja_es.deck[12])
    print("As de copas")
    print_card(baraja_es.deck[24])
    print("As de espadas")
    print_card(baraja_es.deck[36])
    print("As de bastos")

    print_card(baraja_fr.deck[0])
    print("As de corazones")
    print_card(baraja_fr.deck[13])
    print("As de tréboles")
    print_card(baraja_fr.deck[26])
    print("As de picas")
    print_card(baraja_fr.deck[39])
    print("As de diamantes")

    input("")
import random
from typing import Dict

rankReference: Dict[int, str] = {
    0: "3",
    1: "4",
    2: "5",
    3: "6",
    4: "7",
    5: "8",
    6: "9",
    7: "10",
    8: "Jack",
    9: "Queen",
    10: "King",
    11: "Ace",
    12: "2",
}

suitReference: Dict[int, str] = {
    0: "Diamonds",
    1: "Clubs",
    2: "Hearts",
    3: "Spades"
}


class Card:
    def __init__(self, _rank: int, _suit: str):
        self.rank: int = _rank
        self.suit: str = _suit

        self.name: str = rankReference[self.rank] + " of " + suitReference[self.suit]

    
    def getCompleteRanking(self) -> int:
        return (self.rank * 100) + self.suit

        



    
class Hand:
    def __init__(self):
        # list of cards is assorted with 3 of diamonds lowest and 2 of spades highest
        # lowest card is self.cards[0]
        self.cards: list[Card] = []

    def sort(self) -> None:
        self.cards = sorted(self.cards, key=lambda card: card.getCompleteRanking())


    def addCard(self, card: Card) -> None:
        self.cards.insert(0, card)
        self.sort()

    def getLowestCard(self) -> Card:
        return self.cards[0]

    def getHighestCard(self) -> Card:
        return self.cards[-1]
    
    def displayHand(self) -> None:
        for num, card in enumerate(self.cards):
            print(f"{num + 1}. {card.name}")

    def containsThreeOfDiamonds(self) -> bool:
        for card in self.cards:
            if card.name == "3 of Diamonds":
                return True
            
        return False
    

class Dealer:
    def __init__(self):
        self.cardsDealt: list[str] = []

    def dealHand(self) -> Hand:
        cardsBeingDealt: Hand = Hand()


        while len(cardsBeingDealt.cards) < 13:
            cardGenerated: Card = Card(random.randint(0, 12), random.randint(0, 3))

            if cardGenerated.name in self.cardsDealt:
                cardGenerated: Card = Card(random.randint(0, 12), random.randint(0, 3))
            else:
                cardsBeingDealt.addCard(cardGenerated)
                self.cardsDealt.append(cardGenerated.name)

        return cardsBeingDealt


class Play:
    def __init__(self):
        self.cards: list[Card] = []

class SingleCard(Play):
    def __init__(self):
        super().__init__()

class Pair(Play):
    def __init__(self):
        super().__init__()

class ThreeOfAKind(Play):
    def __init__(self):
        super().__init__()


class FiveCard(Play):
    def __init__(self):
        super().__init__()

class Straight(FiveCard):
    def __init__(self):
        super().__init__()

class Flush(FiveCard):
    def __init__(self):
        super().__init__()

class FullHouse(FiveCard):
    def __init__(self):
        super().__init__()

class FourOfAKind(FiveCard):
    def __init__(self):
        super().__init__()

class StraightFlush(FiveCard):
    def __init__(self):
        super().__init__()



class Pile:
    def __init__(self):
        self.plays: list[Play] = []

    def getMostRecentPlay(self) -> Play:
        return self.plays[0]
    
    def addNewPlay(self, play: Play) -> None:
        self.plays.insert(0, play)


def printCurrentPlayerName() -> None:
    if currentPlayer is playerOneHand:
        print("Player 1")
    elif currentPlayer is playerTwoHand:
        print("Player 2")
    elif currentPlayer is playerThreeHand:
        print("Player 3")
    elif currentPlayer is playerFourHand:
        print("Player 4")





dealer: Dealer = Dealer()

playerOneHand: Hand = dealer.dealHand()
playerTwoHand: Hand = dealer.dealHand()
playerThreeHand: Hand = dealer.dealHand()
playerFourHand: Hand = dealer.dealHand()

players: list[Hand] = [playerOneHand, playerTwoHand, playerThreeHand, playerFourHand]



# figures out who is going first
currentPlayer: Hand = playerOneHand

if playerTwoHand.containsThreeOfDiamonds():
    currentPlayer = playerTwoHand
elif playerThreeHand.containsThreeOfDiamonds():
    currentPlayer = playerThreeHand
elif playerFourHand.containsThreeOfDiamonds():
    currentPlayer = playerFourHand

print("\n")

# says who is going first
printCurrentPlayerName()
print("You must play the three of diamonds")

print("\n")

currentPlayer.displayHand()

print("\n")

print("What would you like to play?")



while len(playerOneHand.cards) != 0 and len(playerTwoHand.cards) != 0 and len(playerThreeHand.cards) != 0 and len(playerFourHand.cards) != 0:
    break




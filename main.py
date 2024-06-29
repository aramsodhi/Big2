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

playTypeReference: Dict[int, str] = {
    0: "Single",
    1: "Pair",
    2: "Three of a kind",
    4: "Five card"
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
        for card in self.cards:
            print(card.name)
    

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




class Pile:
    def __init__(self):
        self.cardsPlayed = list[Card]

        self.playType = "Single"

    def getTopCard(self):
        if self.playType is "Single":
            return self.cardsPlayed[0]
        
        elif self.playType is "Pair":
            return self.cardsPlayed[:1]
        
        elif self.playType is "Three of a kind":
            return self.cardsPlayed[:2]
        
        elif self.playType is "Five card":
            return self.cardsPlayed[:4]


    def playSingle(self, card: Card) -> None:
        if self.playType is "Single" and card.getCompleteRanking() > self.getTopCard().getCompleteRanking():
            self.cardsPlayed.insert(0, card)

    def playPair(self, pair: list[Card]) -> None:
        if self.playType is "Pair":
            # check if number of two cards is the same
            if pair[0].rank is pair[1].rank:
                # check if number is higher than current number
                if pair[0].rank > self.getTopCard()[0].rank:
                    # PLAY PAIR
                    pass
                elif pair[0].rank is self.getTopCard()[0].rank:
                    pass
                    # if the same, check if highest card of played pair is higher than highest of current pair


dealer: Dealer = Dealer()

playerOneHand: Hand = dealer.dealHand()
playerTwoHand: Hand = dealer.dealHand()
playerThreeHand: Hand = dealer.dealHand()
playerFourHand: Hand = dealer.dealHand()

players: list[Hand] = [playerOneHand, playerTwoHand, playerThreeHand, playerFourHand]

playerOneHand.displayHand()



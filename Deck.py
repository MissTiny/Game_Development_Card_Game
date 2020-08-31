import Card
Card = Card.Card

class Deck:
    
    def __init__(self):
        self.cardList = []
        self.colorList = ['red','blue','green']
        self.fillList = ['solid', 'shaded', 'clear']
        self.shapeList = ['circle', 'triangle','square']
        self.numList = ['1','2','3']

        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        self.cardList.append(Card(color, fill, shape, number))

    def getNumberOfCards(self):
        return len(self.cardList)

    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, CardNumber):
        return self.cardList[CardNumber]

    #shuffle method with three shuffles
    def shuffle(self):
        import random
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        return self.cardList

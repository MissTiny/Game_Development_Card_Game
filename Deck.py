import numpy as np
import Card
import os
import sys
Card = Card.Card

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Deck:
    
    def __init__(self,init_num):
        self.cardList = [] #element type: cards
        self.colorList = ['red','blue','green']
        self.fillList = ['solid', 'shaded', 'clear']
        self.shapeList = ['circle', 'triangle','square']
        self.numList = ['1','2','3']
        self.hint_num = 3
        self.record = [] #passed formed set | element type: List of Card
        self.waitingList = [] #sets waiting for checking | element type: tuple value
        self.init_num = init_num
        self.score =0
         #cards that are displayed
        for color in self.colorList:
            for fill in self.fillList:
                for shape in self.shapeList:
                    for number in self.numList:
                        #path yellow shaded triangle2 example
                        image_path =resource_path(color+" "+fill+" "+shape+number+".gif")
                        #image_path = "CardImages/"+color+" "+fill+" "+shape+number+".gif"
                        self.cardList.append(Card(color, fill, shape, number,image_path))
        self.display = [(count,elem) for count,elem in enumerate(self.cardList[0:init_num])] #tuple value
        self.hasSetInDisplay = False
        self.hasSetInCardList = False
        self.hint = []
    def displayCheck(self):
        self.hasSetInDisplay = False
        for (count1,card_1) in self.display[:-2]:
            for (count2,card_2) in self.display[count1+1:-1]:
                for (count3,card_3) in self.display[count2+1::]:
                    card1 = card_1.getAll()
                    card2 = card_2.getAll()
                    card3 = card_3.getAll()
                    checklist = [1,1,1,1] #init with 'na' == 1
                    #same for all same = 2, diff for all different == 0, na for not valid
                    if (card1  == ("","","","")):
                        continue
                    if(card2  == ("","","","")):
                        continue
                    if(card3  == ("","","","")):
                        continue
                    for i in range(4):
                        #totally for attribute
                        
                        attribute_list = [card1[i],card2[i],card3[i]]
                        num = len(np.unique(attribute_list))
                        if num == 3:
                            #all different == 0
                            checklist[i] = 0
                        elif num == 1:
                            #all same == 2
                            checklist[i] = 2
                    
                    if 1 not in checklist:#if 'na' not in checklist
                        #only same == 2 and diff == 0
                        self.hasSetInDisplay = True
                    if (self.hasSetInDisplay ==True):
                        self.hint=[count1,count2,count3]
                        print(card1,card2,card3)
                        print(self.hint)
                        return self.hasSetInDisplay
    
    def cardListCheck(self):
        self.hasSetInCardList = False
        cardlist = [(count,elem) for count,elem in enumerate(self.cardList)]

        for (count1,card_1) in cardlist[:-2]:
            for (count2,card_2) in cardlist[count1+1:-1]:
                for (count3,card_3) in cardlist[count2+1::]:
                    card1 = card_1.getAll()
                    card2 = card_2.getAll()
                    card3 = card_3.getAll()
                    checklist = [1,1,1,1] #init with 'na' == 1
                    #same for all same = 2, diff for all different == 0, na for not valid
                    if (card1  == ("","","","")):
                        continue
                    if(card2  == ("","","","")):
                        continue
                    if(card3  == ("","","","")):
                        continue
                    for i in range(4):
                        #totally for attribute
                        
                        attribute_list = [card1[i],card2[i],card3[i]]
                        num = len(np.unique(attribute_list))
                        if num == 3:
                            #all different == 0
                            checklist[i] = 0
                        elif num == 1:
                            #all same == 2
                            checklist[i] = 2
                    
                    if 1 not in checklist:#if 'na' not in checklist
                        #only same == 2 and diff == 0
                        self.hasSetInCardList = True
                    if (self.hasSetInCardList ==True):
                        return self.hasSetInCardList
                    
                    
    def getNumberOfCards(self):
        return len(self.cardList)
    def getDisplayList(self):
        return self.display
    #takes in an integer (1-81) and returns the index at that card
    def getCard(self, CardNumber):
        return self.cardList[CardNumber]

    #shuffle method with three shuffles
    def shuffle(self):
        import random
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        random.shuffle(self.cardList)
        self.display = [(count,elem) for count,elem in enumerate(self.cardList[0:self.init_num])] #tuple value
        return self.cardList
    def getRecord(self):
        return self.record
    def moveToRecord(self):
        clean_waitingList =[elem for (count,elem) in self.waitingList]
        self.record.append(clean_waitingList) #add success set to past records
        self.cardList = [elem for elem in self.cardList if elem not in clean_waitingList] #remove the set from the cardlist
        
        #renew the display
        set_count = 0

        for (count,elem) in self.waitingList:
            if(self.getNumberOfCards()>9):
                self.display[count]=(count,self.cardList[self.init_num-3+set_count])
            else:
                self.display[count]=(count,Card("","","","","CardImages/blank.gif"))
            set_count+=1
        self.waitingList = [] 
    def select(self,Card_dict):
        self.waitingList.append(Card_dict) #add the selected card into waitingList
    
    def unselect(self,Card_dict):
        self.waitingList.remove(Card_dict) #add the selected card into waitingList
        
    def emptyWaitingList(self):
        self.waitingList = []
    def getWaitingList(self):
        return self.waitingList
    def setCheck(self):
        #all different set
        card1 = self.waitingList[0][1].getAll()
        card2 = self.waitingList[1][1].getAll()
        card3 = self.waitingList[2][1].getAll()
        checklist = [1,1,1,1] #init with 'na' == 1
        #same for all same = 2, diff for all different == 0, na for not valid
        for i in range(4):
            #totally for attribute
            
            attribute_list = [card1[i],card2[i],card3[i]]
            num = len(np.unique(attribute_list))
            if num == 3:
                #all different == 0
                checklist[i] = 0
            elif num == 1:
                #all same == 2
                checklist[i] = 2
        
        #final check
        result = False
        if 1 not in checklist:#if 'na' not in checklist
            #only same == 2 and diff == 0
            result = True
        #clean up
        if result ==True:
            self.score+=20
            self.moveToRecord()
        else:
            self.score -=5
            self.emptyWaitingList()

        #todo: error message hint
        return (result)

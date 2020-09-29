import tkinter as tk
from tkinter import *
class Card:

    def __init__(self, Color, Shape, Fill, Number,Image_Path):
        self.color = Color
        self.fill = Fill
        self.shape = Shape
        self.number = Number
        self.image = PhotoImage(file=Image_Path)
       # self.is_selected = False

    #create the methods for getting the properties of the card
    def getColor(self):
        return self.color
    def getFill(self):
        return self.fill
    def getShape(self):
        return self.shape
    def getNumber(self):
        return self.number
    def getImage(self):
        return self.image
    '''
    def isSelected(self):
        return self.is_selected
    '''
    def getAll(self):
        return (self.color, self.fill,self.shape,self.number)
    
    '''
    #change the status of selected
    def changeIsSelected(self):
        self.is_selected = not self.is_selected
    '''
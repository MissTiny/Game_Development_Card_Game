# -*- coding: utf-8 --
"""
Created on Wed Sep  2 01:30:31 2020

@author: MissTiny
"""
##################
##################
#library
import tkinter as tk
from tkinter import *
#To read files in directory
import glob
import random 
import Deck
Deck = Deck.Deck
import numpy as np
import time
#####################
def newGame(init_num):
    deck = Deck(init_num)
    deck.shuffle()
    return deck
button_list=[]   
selected_button = []

def cardSelect(btn,card,deck,top_frame,side_frame,bottom_frame,main_frame):
    #waitingList and display are tuple value
    global selected_button
    
    if card not in deck.getWaitingList():
        #if the card is selected, change button outlook
        deck.select(card)
        selected_button.append(btn)
        btn['relief'] = SUNKEN
        btn['bg'] = "#DDE6E7"
    else:
        #if the card is canceled, change button outlook back
        deck.unselect(card)
        selected_button.remove(btn)
        btn['relief'] = RAISED
        btn['bg']="white"
    if (len(deck.getWaitingList()) == 3):
        #if three cards are choosen, auto check start
        response = deck.setCheck()
        for button in selected_button:
            button['relief'] = RAISED
            button['bg']="white"
        
        
        #announcement

        message = Label(top_frame,font=("Courier", 20))
        if response:
            top_frame['bg'] = "#90EE90" #light green
            message['text']="Congratulations! Successfully find a set"
            message['bg']=top_frame['bg']
            global button_list
            for btn in selected_button:
                btn.destroy()
            recordDisplay(deck,side_frame)

            selected_button=[]
            
        else:
            message['text']="Sorry! This is not a set. Please try again"
            top_frame['bg'] = "#F08080" #light red
            message['bg']=top_frame['bg']
        selected_button = []
        #label.place(relx=0.5,rely=0.1)
        message.place(relx=0.5,rely=0.5,anchor = CENTER)
        top_frame.after(800, lambda arg1= message,arg2=top_frame:flashMessage(arg1,arg2)) 

        
        #update_sidebar
        score_content = Label(side_frame,text=str(len(deck.getRecord())),bg = side_frame['bg'],font=("Courier", 20))
        score_content.place(relx = 0.5, rely = 0.15, anchor=CENTER)
        
        deck_content = "Remain in the deck:" + str(deck.getNumberOfCards())
        deck_info = Label(bottom_frame,text=deck_content, bg = bottom_frame['bg'],font=("Courier", 10))
        deck_info.place(relx=0.5, rely=0.1,anchor = CENTER)
        
        selffresh(deck,bottom_frame,main_frame,side_frame,top_frame)
        if (deck.getNumberOfCards() == 0):
            btns=[main_frame,top_frame,side_frame,bottom_frame]
            init("end",len(deck.getRecord()),btns)
            
def flashMessage(message, frame):
    message.destroy()
    frame['bg'] = "white"
def display(cards_display_list,deck,main_frame,top_frame,side_frame,bottom_frame,is_hint):
    '''
    for i in range(len(cards_display_index)):  
        card = deck.getCard(cards_display_index[i])
        photo = card.getImage()
        #btn = Button(main_frame,image = photo,bg="white",command =card.changeIsSelected,activebackground="grey" )    
        btn =Button(main_frame,image = photo,bg="white",relief = RAISED)   
        btn.config(command =lambda arg1=btn,arg2=card,arg3=deck,arg4=top_frame,arg5=side_frame,arg6=bottom_frame:cardSelect(arg1,arg2,arg3,arg4,arg5,arg6))
        col = i %4
        row = i//4
        btn.grid(row= row, column = col)
        btn.image = photo
    '''
    hint_button =Button(side_frame,text="Hint",relief = RAISED,font=("Courier", 10))
    hint_button.config(command =lambda arg1=deck.getDisplayList(),arg2=deck,arg3=main_frame,arg4=top_frame,arg5=side_frame,arg6=bottom_frame,arg7=True:display(arg1,arg2,arg3,arg4,arg5,arg6,arg7))
    hint_button.place(relx=0.5, rely=0.05,anchor = CENTER)
    if(is_hint):
        global selected_button
        for button in selected_button:
            button['relief'] = RAISED
            button['bg']="white"
        deck.waitingList = []
        selected_button = []
    for widget in main_frame.winfo_children():
        widget.destroy()
    for (i,card) in cards_display_list:
        photo = card.getImage()
        if (card.getColor() == ""): 
            btn =Button(main_frame,image=photo,bg="white",relief = RAISED,state=tk.DISABLED)   
        else:
            #btn = Button(main_frame,image = photo,bg="white",command =card.changeIsSelected,activebackground="grey" )
            if ((i in deck.hint) & (is_hint)):
                btn =Button(main_frame,image = photo,bg="#fed8b1",relief = RAISED)
                selected_button.append(btn)
            else:
                btn =Button(main_frame,image = photo,bg="white",relief = RAISED)   
            btn.config(command =lambda arg1=btn,arg2=(i,card),arg3=deck,arg4=top_frame,arg5=side_frame,arg6=bottom_frame,arg7=main_frame:cardSelect(arg1,arg2,arg3,arg4,arg5,arg6,arg7))
        col = i %4
        row = i//4
        btn.grid(row= row, column = col)
        btn.image = photo
        global button_list
        button_list.append(btn)

def recordDisplay(deck,side_frame):
    #gallery = Text(side_frame,wrap="none")
    #scroll = Scrollbar(orient="vertical", command = gallery.yview)
    #gallery.configure(yscrollcommand=scroll.set)
    #scroll.place(relx = 1,rely = 0,relheight=1,anchor='ne')
    rely = 0.25
    for (i,set) in enumerate(deck.getRecord()):
        if (i % 2) == 1 :
            relx = 0.6
        else:
            relx=0.1
        for card in set:
            image = image=card.getImage().subsample(3)
            card_image=Label(side_frame,image=image,bg="white")
            card_image.image = image
            #gallery.window_create("end",window=image)
            #gallery.insert("end","\n")
            card_image.place(relx = relx,rely=rely,anchor=CENTER)
            relx+=0.15
        if (i%2) == 1:
            rely+=0.05
def selffresh(deck,bottom_frame,main_frame,side_frame,top_frame):
    deck.cardListCheck()
    deck.displayCheck()
    display(deck.getDisplayList(),deck,main_frame,top_frame,side_frame,bottom_frame,False)
    print("still have")
    print(deck.hasSetInDisplay)
    print(deck.hasSetInCardList == True)

    while ((not deck.hasSetInDisplay )& (deck.hasSetInCardList )):
        #display = false --no set, cardlist = true -- has set
        print("enter false statement")
        top_frame['bg'] = "yellow" #coral
        message = Label(top_frame,font=("Courier", 20))
        message['text']="Current display doesn't have a set. AutoFreshed"
        message['bg']=top_frame['bg']
        message.place(relx=0.5,rely=0.5,anchor = CENTER)
        deck.shuffle()
        deck.displayCheck()
        top_frame.after(800, lambda arg1= message,arg2=top_frame:flashMessage(arg1,arg2))
        print("new display")
        display(deck.getDisplayList(),deck,main_frame,top_frame,side_frame,bottom_frame,False)
    if (deck.hasSetInCardList == False):
        btns = [bottom_frame,main_frame,side_frame,top_frame]
        init("noSet",len(deck.getRecord()),btns) 
    return deck
        
def game():
    number_init = 12
    ##side_bar design
    side_frame = Frame(window,height= 880,width = 400,bg="#F9E8A7")
    side_frame.pack(side = RIGHT)   
    
    #top warning
    top_frame = Frame(window, width=980,height=50,bg="white")
    top_frame.pack(side = TOP)
    
    ##main display
    main_frame = Frame(window, bg="white",pady = 50)
    main_frame.pack(side = TOP)
    #bottom button
    bottom_frame = Frame(window, width = 980,height = 100,bg="white")
    bottom_frame.pack()
    

    deck = newGame(number_init)
    
    #cards_display_index = range(number_init)
    card_button_list = [] #list of all buttons east access
    deck = selffresh(deck,bottom_frame,main_frame,side_frame,top_frame)
    #side bar design
    hint_button =Button(side_frame,text="Hint",relief = RAISED,font=("Courier", 10))
    hint_button.config(command =lambda arg1=deck.getDisplayList(),arg2=deck,arg3=main_frame,arg4=top_frame,arg5=side_frame,arg6=bottom_frame,arg7=True:display(arg1,arg2,arg3,arg4,arg5,arg6,arg7))
    hint_button.place(relx=0.5, rely=0.05,anchor = CENTER)
    score_title = Label(side_frame,text="Your Score", bg = side_frame['bg'],font=("Courier", 20))
    score_title.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    score_content = Label(side_frame,text=str(len(deck.getRecord())),bg = side_frame['bg'],font=("Courier", 20))
    score_content.place(relx = 0.5, rely = 0.15, anchor=CENTER)
    record_title= Label(side_frame,text="Set Recorded", bg = side_frame['bg'],font=("Courier", 20))
    record_title.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    recordDisplay(deck,side_frame)
    '''
    gallery=Text(side_frame,wrap="none")
    scroll = Scrollbar(orient="vertical",command=gallery.yview)
    scroll.place(relx=0.9,rely=0.25,anchor= CENTER)
    scroll.config(command=gallery.yview)
    
    num=0
    for set in deck.getRecord():
        print(num)
        num+=1
        for card in set:
            card_image=Label(side_frame,image=card.getImage())
            card_image=card_image.subsample(2)
            card_image.image = card.getImage()
            gallery.window_create("end",window=card_image)
            gallery.insert("end","\n")
    gallery.configure(state="disabled")
    gallery.place(relx=0,rely = 0.5)
    '''


    deck_content = "Remain in the deck:" + str(deck.getNumberOfCards())
    deck_info = Label(bottom_frame,text=deck_content, bg = bottom_frame['bg'],font=("Courier", 10))
    deck_info.place(relx=0.5, rely=0.1,anchor = CENTER)
    restart_button = Button(bottom_frame,text="Click to Restart the Game!",relief = RAISED,font=("Courier", 10))
    btns=[side_frame,main_frame,top_frame,bottom_frame]
    restart_button.config(command =lambda arg1=btns:gameStart(arg1))
    restart_button.place(relx=0.5, rely=0.5,anchor = CENTER)
    home_button =Button(bottom_frame,text="Home",relief = RAISED,font=("Courier", 10))
    home_button.config(command =lambda arg1=btns:init("start",'',arg1))
    home_button.place(relx=0.25, rely=0.5,anchor = CENTER)
    quit_button =Button(bottom_frame,text="Quit",relief = RAISED,font=("Courier", 10))
    #button feature
    quit_button.config(command =lambda arg1=btns:init("end",len(deck.getRecord()),arg1))
    quit_button.place(relx=0.75, rely=0.5,anchor = CENTER)

def gameStart(btns):
    for i in btns:
        i.destroy()
    game()
def init(is_init,score,btns):
    for i in btns:
        i.destroy()
    info_list = []
    if (is_init == "start"):
        #MainFrame - displaying cards
        start_game = Button(window,text="Start The Game !",relief = RAISED, bg = "lightblue",font=("CourierHelvetica",20))
        info_list.append(start_game)
        start_game.config(command = lambda arg = info_list: gameStart(arg) )
        start_game.place(relx = 0.5,rely = 0.5,anchor=CENTER)
    else:
        if (is_init == "noSet"):
            announce_content = "Cards in Deck can no longer form a set! Game end!"
            announce_info = Label(window,text=announce_content, bg = '#90EE90',font=("Courier", 20))
            announce_info.place(relx=0.5,rely = 0.30,anchor=CENTER)
            info_list.append(announce_info)
            score_content = "Congrats! Your Final Score is " + str(score)
            score_info = Label(window,text=score_content, bg = '#90EE90',font=("Courier", 40))
            score_info.place(relx=0.5,rely = 0.4,anchor=CENTER)
            info_list.append(score_info)
        else:
            score_content = "Congrats! Your Final Score is " + str(score)
            score_info = Label(window,text=score_content, bg = '#90EE90',font=("Courier", 40))
            score_info.place(relx=0.5,rely = 0.4,anchor=CENTER)
            info_list.append(score_info)
            
        start_game = Button(window,text="Play Again !",relief = RAISED, bg = "lightblue",font=("CourierHelvetica",20))
        info_list.append(start_game)
        start_game.config(command = lambda arg = info_list: gameStart(arg) )
        start_game.place(relx = 0.5,rely = 0.5,anchor=CENTER)

#####################
#initial window
window = tk.Tk()
#window setting
window.title("The Set Game")
window.geometry("1280x960")
window.configure(bg="white")
#start game
header_frame = Frame(window, width=1280,height=100,bg = "LightBlue")
header_frame.pack( side = TOP)
message = Label(header_frame,text="Welcome! The Set Game!",bg=header_frame['bg'],font=("CourierHelvetica", 44))
message.place(relx=0.5,rely=0.5,anchor = CENTER)
#random pick 12 cards
#todo: add a variable to make player select cards

#number_init = 12
#cards_display_index = range(number_init)

init("start",20,[])

#window display

#FooterFrame

#check_button =Button(top_frame,text=str(len(deck.getWaitingList())),bg="white",relief = RAISED)   
#check_button.pack()

window.mainloop()
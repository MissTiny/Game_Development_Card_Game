#####IMPORTANT!####
This program can only run on Windows system because the program is coded under window circumstance.
Tkinter in mac os has a lot of error issues when using this codes. 
    For example, the button color can not be changed unless using the tkmacosx package. Then a new issue associated with display formatting appears.


#For window user
How to execute the game:
    double click on SetGame.exe [shortcut]
    --if it doesn't work, please navigate into folder SetGame, scroll down and find the real SetGame.exe file.

Now the game window is opened:
    #ignore the terminal
    To start the game: 
        Click the button [Start The Game !]

    How to play the game:
        The object of the game is to identify a 'Set' of three cards from 12 cards laid out on the table. Each card has a variation of the following four features:
                (A) COLOR:
                Each card is red, green, or purple.
                (B) SYMBOL:
                Each card contains ovals, squiggles, or diamonds.
                (C) NUMBER:
                Each card has one, two, or three symbols.
                (D) SHADING:
                Each card is solid, open, or striped.
                A 'Set' consists of three cards in which each feature is EITHER the same on each card OR is different on each card. That is to say, any feature in the 'Set' of three cards is either common to all three cards or is different on each card.
                Citing from: http://magliery.com/Set/SetRules.html#:~:text=A%20player%20must%20call%20'Set,are%20returned%20to%20the%20table.
        
        Note:
            Select a Card : Click on the card -- the card will be grey if selected
            UnSelect a Card : Click on the card that is selected -- the card will turn white from grey if unselected
            Check the set: an autocheck will execute when three cards are selected.
                Success : A green top message will show up
                Failure : A red top message will show up
            When a set is found, the three cards will be removed from the deck. And three other cards from the remaining cards in the deck will replace the displayed position of the original three cards.
            System will automatically check whether the cards displayed can found a set. If not, a auto-shuffle of the deck will appear with an announce on the top in yellow. If cards in deck can no longer create a set, then game is forced to end.

            When deck has fewer than 12 cards, blank card will be used to replace the cards that founded the set. The blank card will not be able to be clicked.

            Game natural ends:
                1. When deck is empty [all 27 set are found]
                2. When cards in deck can no longer create a set.

            #side bars
            Score: Score is counted based on the amount of set found
            Set Record: Sets that you have found will be displayed here
            [button] Hint: Click to see indicated set -- cards that can form a set will be shadowed orange.

            #bottom buttons
            Remain in the deck: Number of cards remained in the deck
            [button] Home : Click to return the home page without showing your score
            [button] Click to Restart the Game!: Click to restart the game [Score will refreshed to 0, Set Record will be emptyed, And the cards in deck will be refilled]
            [button] Quit : Click to return the home page with a score showed.
            
    How to end the program:
        Click the [X] button on the up right corner. Terminal will close with the window.

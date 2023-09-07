"""Implements the logic of the game of boggle."""

from graphics import GraphWin
from boggleboard import BoggleBoard
from boggleletter import BoggleLetter
from brandom import randomize

class BoggleGame:

    __slots__ = [ "_validWords", "_board", "_foundWords", "_selectedLetters" , "_score" ]

    def __init__(self, win):
        """
        Create a new Boggle Game and load in our lexicon.
        """
        # set up the set of valid words we can match
        self._validWords = self.__readLexicon()

        # init other attributes here.
        self._board = BoggleBoard(win)
        self._foundWords = []
        self._selectedLetters = []
        self._score = 0 


    def __readLexicon(self, lexiconName='bogwords.txt'):
        """
        A helper method to read the lexicon and return it as a set.
        """
        validWords = set()
        with open(lexiconName) as f:
          for line in f:
            validWords.add(line.strip().upper())

        return validWords
        # given

    def doOneClick(self, point):
        """
        Implements the logic for processing one click.
        Returns True if play should continue, and False if the game is over.
        """
        # These steps are one way to think about the design, although
        # you are free to do things differently if you prefer.

        # step 1: check for exit button and return False if clicked
        if self._board.inExit(point):
            return False

        # step 2: check for reset button and reset
        elif self._board.inReset(point):
            self._board.resetColors()
            self._board.reset()
            self._foundWords = []
            self._selectedLetters = []
            return True

        # step 3: check if click is on a cell in the grid
        elif self._board.inGrid(point):
            
          # get BoggleLetter at point 
            ourLetter = self._board.getBoggleLetterAtPoint(point)

          # if this is the first letter in a word being constructed,
          # add letter and display it on lower text of board
            ourLetter.setFillColor("light green")
            ourLetter.setTextColor("forest green") 
  

          # check if its the first letter added and hasn't been clicked on before,
          # and update state 
            if self._selectedLetters == []:
                self._selectedLetters.append(ourLetter)
                letters = self._board.getStringFromLowerText() 
                self._board.setStringToLowerText(letters + ourLetter.getLetter().lower())

            #else check if the letter clicked on is adjacent to the last letter
            #and check if it hasn't been clicked on 
            #change colors and lower text
            elif ourLetter.isAdjacent(self._selectedLetters[-1]) and ourLetter not in self._selectedLetters:
                self._selectedLetters.append(ourLetter)
                letters = self._board.getStringFromLowerText() 
                self._board.setStringToLowerText(letters + ourLetter.getLetter().lower())
                self._selectedLetters[-1].setFillColor("light green")
                self._selectedLetters[-1].setTextColor("forest green")
                self._selectedLetters[-2].setFillColor("powder blue")
                self._selectedLetters[-2].setTextColor("blue")
                

          # else if clicked on same letter as last time, end word and check for validity
          #convert the the list of objects(selectedLetters) to a list of strings
          #check if the word is a valid word
          #and check if it hasn't been found already 
          #add score
          #then reset the state
            elif ourLetter == self._selectedLetters[-1]:
                gameletters = [ourLetter.getLetter() for ourLetter in self._selectedLetters]
                if ''.join(gameletters).upper() in self._validWords:
                    if ''.join(gameletters).upper() not in self._foundWords:
                        self._foundWords.append(''.join(gameletters))
                        self._board.setStringToTextArea('\n'.join(self._foundWords))
                        self._board.setStringToUpperText("Score: " + str(self.Score(''.join(gameletters))))
                self._board.setStringToLowerText("")
                self._board.resetColors()
                self._selectedLetters = []

            #if clicked anywhere else, reset the state
            else:
                self._board.setStringToLowerText("")
                self._board.resetColors()
                self._selectedLetters = []

        # return True to indicate we want to keep playing
        return True 

    #pass the current found word and update the score 
    def Score(self, words):
        if len(words) == 3:
            self._score += 1
        elif len(words) == 4:
            self._score+= 1
        elif len(words) == 5:
            self._score += 2 
        elif len(words) == 6:
            self._score += 3
        elif len(words) == 7:
            self._score += 5
        elif len(words) >= 8:
            self._score += 11
        return self._score

if __name__ == '__main__':

    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!
    randomize()
    win = GraphWin("Boggle", 400, 400)
    game = BoggleGame(win)
    keepGoing = True
    while keepGoing:
        point = win.getMouse()
        keepGoing = game.doOneClick(point)

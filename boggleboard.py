"""
Extends the Board class with specific features required for Boggle
"""

from graphics import *
from brandom import *
from boggleletter import BoggleLetter
from board import Board

class BoggleBoard(Board):
    """Boggle Board class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a grid
    of BoggleLetters, shaken appropriately to randomize play."""

    __slots__ = ['_grid', "_cubes"]

    def __init__(self, win):
        super().__init__(win, rows=4, cols=4)

        self._cubes =  [[ "A", "A", "C", "I", "O", "T" ],
                        [ "T", "Y", "A", "B", "I", "L" ],
                        [ "J", "M", "O", "Qu", "A", "B"],
                        [ "A", "C", "D", "E", "M", "P" ],
                        [ "A", "C", "E", "L", "S", "R" ],
                        [ "A", "D", "E", "N", "V", "Z" ],
                        [ "A", "H", "M", "O", "R", "S" ],
                        [ "B", "F", "I", "O", "R", "X" ],
                        [ "D", "E", "N", "O", "S", "W" ],
                        [ "D", "K", "N", "O", "T", "U" ],
                        [ "E", "E", "F", "H", "I", "Y" ],
                        [ "E", "G", "I", "N", "T", "V" ],
                        [ "E", "G", "K", "L", "U", "Y" ],
                        [ "E", "H", "I", "N", "P", "S" ],
                        [ "E", "L", "P", "S", "T", "U" ],
                        [ "G", "I", "L", "R", "U", "W" ]]

        # set up an empty list
        self._grid = []
        # iterate through each square in the grid
        for col in range(self._cols):
            grid_col =[]
            for row in range(self._rows):
                letter = BoggleLetter(self.getBoard(), col, row)
                grid_col.append(letter)
            self._grid.append(grid_col)    
        self.shakeCubes()



    def getBoggleLetterAtPoint(self, point):
        """
        Return the BoggleLetter that contains the given point in the window,
        or None if the click is outside all letters.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = BoggleBoard(win)
        >>> pointIn_0_0 = Point(board.getXInset() + board.getSize() / 2, \
                                board.getYInset() + board.getSize() / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_0_0) == board._grid[0][0]
        True
        >>> pointIn_1_2 = Point(board.getXInset() + board.getSize() * 3 / 2, \
                                board.getYInset() + board.getSize() * 5 / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_1_2) == board._grid[1][2]
        True
        >>> win.close()
        """

        # return BoggleLetter object at given location on the screen
        # and check if given point is in grid
        if self.inGrid(point):
            # if our point is in the grid we can then....
            (col,row) = self.getPosition(point)
            # find the position of the point
            return self._grid[col][row]
        # return None if not in grid
        else:
            return None    

    def resetColors(self):
        """
        "Unclicks" all boggle letters on the board without changing any
        other attributes.  (Change letter colors back to default values.)
        """
        for col in range(self._cols): #looking in the columns
            for row in range(self._rows): #looking in the rows
                self._grid[col][row].setFillColor("white")
                self._grid[col][row].setTextColor("black")
                # reset squares by filling the rectangle with white

    def reset(self):
        """
        Clears the boggle board by clearing letters and colors,
        clears all text areas (right, lower, upper) on board
        and resets the letters on board by calling shakeCubes.
        """
        # reset letter and color
        for col in range(self._cols):
            for row in range(self._rows):
                self._grid[col][row].setLetter("")
                self._grid[col][row].setFillColor("white")
        # clear all text areas 
        self.setStringToLowerText("")
        self.setStringToTextArea("")
        self.setStringToUpperText("")
        # reset letters on board
        self.shakeCubes()

    def shakeCubes(self):
        """
        Shakes the boggle board and sets letters as described by the handout.
        """
        # shuffle cubes
        shuffledCubes = shuffled(self._cubes)

        # iterate over squares to shuffle the side of the cube facing up
        for rowGrid in range(self._rows):
            for colGrid in range(self._cols):
                # use randomInt to randomly choose the face-up side of the cube
                self._grid[colGrid][rowGrid].setLetter(shuffledCubes[0][randomInt(0,5)])
                # slice list of lists shuffled cubes to systematically assign a list to 
                # each square in the grid
                shuffledCubes = shuffledCubes[1:]
                


    def __str__(self):
        """
        Returns a string representation of this BoggleBoard
        """
        board = ''
        for r in range(self._rows):
            for c in range(self._cols):
                boggleLetter = self._grid[c][r]
                color = boggleLetter.getTextColor()
                letter = boggleLetter.getLetter()
                board += '[{}:{}] '.format(letter,color)
            board += '\n'
        return board


if __name__ == "__main__":
    from doctest import testmod
    # testmod()

    # # Uncomment this code when you are ready to test it!
    
    # # When you are ready to run on different boards,
    # # insert a call to randomize() here.  BUT you will
    # # find it much easier to test your code without
    # # randomizing things!
    
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard(win)
    print(board)
    
    randomize()

    keepGoing = True
    while keepGoing:
        pt = win.getMouse()
        if board.inExit(pt):
            keepGoing = False
        elif board.inGrid(pt):
            (col, row) = board.getPosition(pt)
            print("{} at {}".format(board._grid[col][row], (pt.getX(), pt.getY())))
        elif board.inReset(pt):
            board.reset()


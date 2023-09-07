"""
Implements the functionality of a single letter squanre on the Boggle board.
"""

from graphics import *
from board import Board

class BoggleLetter:
    """A Boggle letter has several attributes that define it:
       *  _row, _col coordinates indicate its position in the grid (ints)
       *  _textObj denotes the Text object from the graphics module,
          which has attributes such as size, style, color, etc
          and supports methods such as getText(), setText() etc.
    """

    # add more attributes if needed!
    __slots__ = ['_col', '_row', '_textObj', '_rect' ]

    def __init__(self, board, col=-1, row=-1, letter="", color="black"):
        """
        Construct a new Boggle Letter at the given position on the board,
        and with the optional letter and color.
        """

        # needed for standalone testing (can safely ignore)
        xInset = board.getXInset()
        yInset = board.getYInset()
        size = board.getSize()
        win = board.getWin()

        # set row and column attributes
        self._col = col
        self._row = row

        # make rectangle and add to graphical window
        p1 = Point(xInset + size * col, yInset + size * row)
        p2 = Point(xInset + size * (col + 1), yInset + size * (row + 1))        
        self._rect = board._makeRect(p1, p2, "white")

        # initialize textObj attribute
        self._textObj = Text(self._rect.getCenter(), letter)
        self._textObj.setFill(color) # text color
        self._textObj.draw(win)

    def getRow(self):
        """Returns _col coordinate (int) attribute."""
        return self._row
        #getters for the row attribute

    def getCol(self):
        """Returns _col coordinate (int) attribute."""
        return self._col
        #getters for the collumn attribute

    def setLetter(self, char):
        """
        Sets the text on the BoggleLetter to char (str) by setting the text
        of the Text object (textObj).
        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = Board(win, rows=4, cols=4)
        >>> let1 = BoggleLetter(board, 1, 1, "A")
        >>> let1.setLetter("B")
        >>> print(let1.getLetter())
        B
        >>> win.close()
        """
        self._textObj.setText(char)
        #setter for character BoggleLetter is showing

    def getLetter(self):
        """
        Returns letter (text of type str) associated with textObj attribute.
        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = Board(win, rows=4, cols=4)
        >>> let1 = BoggleLetter(board, 1, 1, "A")
        >>> print(let1.getLetter())
        A
        >>> win.close()
        """
        return self._textObj.getText()
        #getter for character BoggleLetter is showing

    def setTextColor(self, color):
        """
        Sets the color of the letters' Text object.
        """
        self._textObj.setTextColor(color)
        #setter for the color of a BoggleLetter

    def getTextColor(self):
        """
        Gets the color of the letter's Text object.
        """
        return self._textObj.getTextColor()
        #getter for the color of a BoggleLetter

    def setFillColor(self, color):
        """
        Sets the color of the letters' Rectangle object.
        """
        self._rect.setFillColor(color)
        #setter for color of BoggleLetter

    def getFillColor(self):
        """
        Gets the color of the letter's Rectangle object.
        """
        return self._rect.getFillColor()
        #getter for letter Rectangle color

    # test for adjacency
    def isAdjacent(self, other):
        """
        Given a BoggleLetter other, check if other is adjacent to self.
        Returns True if they are adjacent, and otherwise returns False.
        Two letters are considered adjacent if they are not the same, and
        if their row and col coordinates differ by at most 1.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = Board(win, rows=4, cols=4)
        >>> let1 = BoggleLetter(board, 1, 1, "A")
        >>> let2 = BoggleLetter(board, 1, 2, "B")
        >>> let3 = BoggleLetter(board, 3, 1, "C")
        >>> let1.isAdjacent(let2)
        True
        >>> let2.isAdjacent(let1)
        True
        >>> let3.isAdjacent(let3)
        False
        >>> let3.isAdjacent(let1)
        False
        >>> let2.isAdjacent(let3)
        False
        >>> win.close()
        """
        if self.getRow() - other.getRow() == 0 and self.getCol() - other.getCol() ==0:
            #checks if other has the same coordinates as self
            return False
        return abs(self.getRow() - other.getRow()) <= 1 and abs(self.getCol() - other.getCol()) <=1
            #checks if the absolute values of the difference between rows and colums are respectively less than or equal to 1
        
            

    def __str__(self):
        """
        Converts a BoggleLetter to a human-readable string.
        Please do not change this method.
        """
        return "BoggleLetter({}, {}, '{}', '{}')".format(self._col, self._row, \
                                                self.getLetter(), self.getTextColor())

    def __repr__(self):
        """
        A handy special method that enables Python to print lists
        of BoggleLetter objects nicely.
        Please do not change this method.
        """
        return str(self)


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # # The following code is a larger test.  Uncomment the code
    # # and run it, visually inspecting the results once you
    # # are confident that the class is close to complete.
    #
    # from board import Board
    # win = GraphWin("Boggle", 400, 400)
    # board = Board(win, rows=4, cols=4)
    #
    # let1 = BoggleLetter(board, 1, 1, "A")
    # let2 = BoggleLetter(board, 1, 2)
    # let2.setLetter('B')
    # let2.setTextColor("blue")
    # let2.setFillColor("powder blue")
    # let3 = BoggleLetter(board, 3, 1, "C", color="red")
    # let3.setTextColor("dark green")
    # let3.setFillColor("DarkSeaGreen1")
    #
    # # pause for mouse click before exiting
    # point = win.getMouse()
    # win.close()

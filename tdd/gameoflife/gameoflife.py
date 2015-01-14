#!/usr/bin/python
from collections import defaultdict
import time


class Board:
    def __init__(self):
        self.board = defaultdict(lambda: 0)

    def addCells(self, cells):
        # TODO check not override another cell in location
        # and doesn't go out of bounds
        # or find another way to initialize board
        for cell in cells:
            self.board[cell] = 1
            self.getNeighborCount(cell) # realize neighbor cells

    def getNeighborCount(self, cell):
        a, b = cell
        neighbors = [self.board[(x, y)] for x in range(a-1, a+2)
                                        for y in range(b-1, b+2)
                                        if (x, y) != (a, b)]
        return sum(neighbors)

    def lifeMechanic(self, neighborCount, cellState):
        if neighborCount == 2 and cellState == 1:
            return 1
        if neighborCount == 3:
            return 1
        return 0

    def advancegame(self):
        nextBoard = Board()
        for cell in self.board.keys():
            if self.lifeMechanic(self.getNeighborCount(cell), self.board[cell]) == 1:
             nextBoard.addCells([cell])
        self.board = nextBoard.board

    def printBoard(self, x, y):
        while True:
            printable = ""
            for a in range(-x, x):
                for b in range(-y, y):
                    if self.board[(a, b)] == 1:
                        printable += "#"
                    else:
                        printable += " "
                    printable += " "
                printable += "\n"
            print printable
            self.advancegame()
            time.sleep(1)
            print

def main():
    board = Board()
    board.addCells([(1, 1), (1, 2), (1, 3),
                    (2, 1), (2, 2), (2, 3),
                    (3, 1), (3, 2), (3, 3)])
    # Ocillator
    #board.addCells([(1, 1), (1, 2), (1, 3)])
    # Glider
    #board.addCells([(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
    #board.addCells([(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)])
    board.printBoard(9, 9)

if __name__ == "__main__":
    main()

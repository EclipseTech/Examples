#!/usr/bin/python
from collections import defaultdict
import sys
import string


class InputError(Exception):
    def __init__(self, *args, **kwargs):
        super(InputError, self).__init__(*args, **kwargs)

class tictactoe:
    def __init__(self, boardSize = 3, numPlayers = 2):
        self.currentPlayer = 1
        self.board = defaultdict(lambda: 0)
        self.boardSize = boardSize
        self.numPlayers = numPlayers

    def move(self, x, y):
        if self.board[(x, y)] != 0:
            raise InputError("Move already made.")
        if x not in range(self.boardSize) or y not in range(self.boardSize):
            raise InputError("Move is off the board.")
        self.board[(x, y)] = self.currentPlayer

    def advancegame(self):
        self.currentPlayer = self.currentPlayer % self.numPlayers + 1

    def play(self, x, y):
        try:
            self.move(x, y)
            if self.winCondition():
                print "Winner is player %s!" % self.currentPlayer
                sys.exit(0)
            if self.tieCondition():
                print "Game is a tie!"
                sys.exit(0)
            self.advancegame()
        except InputError:
            pass

    def winCondition(self, playerNum = None):
        if not playerNum:
            playerNum = self.currentPlayer
        #row wins
        wins =[[(0, 0), (0, 1), (0, 2)],
               [(1, 0), (1, 1), (1, 2)],
               [(2, 0), (2, 1), (2, 2)],
        #column wins
               [(0, 0), (1, 0), (2, 0)],
               [(0, 1), (1, 1), (2, 1)],
               [(0, 2), (1, 2), (2, 2)],
        #diag wins
               [(0, 0), (1, 1), (2, 2)],
               [(0, 2), (1, 1), (2, 0)]]
        for win in wins:
            owned = map(lambda coord: self.board[coord] == playerNum, win)
            if all(owned):
                return True
        return False

    def tieCondition(self):
        full = [(0, 0), (0, 1), (0, 2),
                (1, 0), (1, 1), (1, 2),
                (2, 0), (2, 1), (2, 2)]
        owned = map(lambda coord: self.board[coord] != 0, full)
        if all(owned):
            return True
        return False

    def __str__(self):
        ret =  " %s | %s | %s \n" % (self.board[(0,0)], self.board[(0,1)], self.board[(0,2)])
        ret += "---+---+---\n"
        ret += " %s | %s | %s \n" % (self.board[(1,0)], self.board[(1,1)], self.board[(1,2)])
        ret += "---+---+---\n"
        ret += " %s | %s | %s \n" % (self.board[(2,0)], self.board[(2,1)], self.board[(2,2)])
        ret = ret.translate(string.maketrans("012", " XO"))
        return ret

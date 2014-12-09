#!/usr/bin/python
# https://sites.google.com/site/tddproblems/all-problems-1/game-of-life
# Develop an algorithm that takes "one step" in the game of life.
# The behaviour examples may simply be the rules of the game:
#    Any live cell with fewer than two live neighbours dies,
#        as if caused by underpopulation.
#    Any live cell with more than three live neighbours dies, as if by
#        overcrowding.
#    Any live cell with two or three live neighbours lives on to the next
#        generation.
#    Any dead cell with exactly three live neighbours becomes a live cell.
#    You also have to think of things such as how to represent the board in a
#        test-friendly way, and what "value" cells outside the board has.
#        Or maybe the board does not have borders?
import unittest2
from negativizer import Negativizer


class Board:
    def __init__(self):
        self.cells = {}

    def getKey(self, cell):
        return "%s %s" % cell

    def getCellAt(self, x, y):
        return self.cells[self.getKey((x, y))]

    def addCells(self, cells):
        # TODO check not override another cell in location
        for cell in cells:
            self.cells[self.getKey(cell)] = cell

    def animated(self, cell):
        if self.getKey(cell) in self.cells:
            return True

    def advancegame(self, cell):
        self.cells = {}


class TestGameOfLife(unittest2.TestCase):
    def setUp(self):
        self.board = Board()
        self.Not = Negativizer(self)

    def tearDown(self):
        self.board = None

    def assertAlive(self, cell):
        if not self.board.animated(cell):
            self.fail("Expected life")

    def assertDies(self, cell):
        self.assertAlive(cell)
        self.board.advancegame(cell)
        self.Not.assertAlive(cell)

    def testAlivebyDefault(self):
        cell = (0, 0)
        self.board.addCells([cell])
        self.assertAlive(cell)

    def test2Cells(self):
        cell1 = (0, 0)
        cell2 = (100000, 1)
        self.Not.assertAlive(cell1)
        self.Not.assertAlive(cell2)
        self.board.addCells([cell1, cell2])
        self.assertAlive(cell1)
        self.assertAlive(cell2)

    def testLifeExpiresSingleCell(self):
        #Any live cell with fewer than two live neighbours dies,
        #    as if caused by underpopulation.
        cell = (0, 0)
        self.board.addCells([cell])
        self.assertDies(cell)

    def testNeighborCount(self):
        self.fail()

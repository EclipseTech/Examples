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
from gameoflife import Board


class TestGameOfLife(unittest2.TestCase):
    def setUp(self):
        self.board = Board()

    def tearDown(self):
        self.board = None

    def assertState(self, state, cell):
        self.assertEquals(self.board.getState(cell), state)

    def assertStateChange(self, startState, endState, cell):
        self.assertState(startState, cell)
        self.board.advancegame()
        self.assertState(endState, cell)

    def assertNeighbors(self, cell, expectedNeighborCount):
        neighborCount = self.board.getNeighborCount(cell)
        if neighborCount != expectedNeighborCount:
            self.fail("Expected %s neighbors, got %s"
                      %(expectedNeighborCount, neighborCount))

    def testAliveifAdded(self):
        cell = (0, 0)
        self.board.addCells([cell])
        self.assertState(1, cell)

    def testDeadCellisDead(self):
        self.assertState(0, (-1,-1))

    def test2Cells(self):
        cell1 = (0, 0)
        cell2 = (100000, 1)
        self.assertState(0, cell1)
        self.assertState(0, cell2)
        self.board.addCells([cell1, cell2])
        self.assertState(1, cell1)
        self.assertState(1, cell2)

    def testLifeExpiresSingleCell(self):
        # Any live cell with fewer than two live neighbours dies,
        #    as if caused by underpopulation.
        cell = (0, 0)
        self.board.addCells([cell])
        self.assertStateChange(1, 0, cell)

    def testCellWithMoreThanThreeNeighborsDies(self):
        # Any live cell with more than three live neighbours dies,
        #     as if by overcrowding.
        self.board.addCells([(0, 0), (0, 1), (0, 2),
                             (1, 0), (1, 1)])
        self.assertStateChange(1, 0, (1, 1))

    def testCellTwoNeighborsLives(self):
        # Any live cell with two or three live neighbours lives
        #     on to the next generation.
        self.board.addCells([(0, 0), (0, 1), (0, 2)])
        self.assertStateChange(1, 1, (0, 1))

    def testDead2NeighborsStaysDead(self):
        self.board.addCells([(0, 0), (0, 1)])
        self.assertStateChange(0, 0, (1, 0))

    def testDeadExactly3NeighborsAnimates(self):
        # Any dead cell with exactly three live neighbours becomes a live cell.
        self.board.addCells([(0, 0), (0, 1), (0, 2)])
        self.assertStateChange(0, 1, (1, 1))

    def testCellThreeNeighborsLives(self):
        self.board.addCells([(0, 0), (0, 1), (0, 2),
                             (1, 0), (1, 1)])
        self.assertStateChange(1, 1, (1, 0))

    def testNeighborCountOne(self):
        cell1 = (0, 0)
        cell2 = (0, 1)
        self.board.addCells([cell1, cell2])
        self.assertNeighbors(cell1, 1)

    def testNeighborCountTwo(self):
        cell1 = (0, 0)
        cell2 = (0, 1)
        cell3 = (1, 0)
        self.board.addCells([cell1, cell2, cell3])
        self.assertNeighbors(cell1, 2)

    def testNeighborCountAll(self):
        self.board.addCells([(1, 1), (1, 2), (1, 3),
                             (2, 1), (2, 2), (2, 3),
                             (3, 1), (3, 2), (3, 3)])
        self.assertNeighbors((2, 2), 8)

    def testAFewStates(self):
        self.board.addCells([(0, 0), (0, 1), (0, 2)])
        self.board.advancegame()
        self.assertState( 1, (-1, 1))
        self.board.advancegame()
        self.assertState(1, (0, 0))

    def testAfewMore(self):
        self.board.addCells([(0, 0), (0, 1), (0, 2)])
        self.assertStateChange(0, 1, (-1, 1))
        self.assertStateChange(0, 1, (0, 0))

#!/usr/bin/python
import unittest2
from collections import defaultdict
import tictactoe


class TestTicTacToe(unittest2.TestCase):
    def setUp(self):
        self.game = tictactoe.tictactoe()

    def assertCurrentPlayer(self, num):
        self.assertEqual(num, self.game.currentPlayer)

    def assertCurrentPlayerOwns(self, x, y):
        self.assertEqual(self.game.board[(x, y)] , self.game.currentPlayer)

    def assertWinner(self, playerNum):
        self.assertTrue(self.game.winCondition(playerNum))

    def assertTie(self):
        self.assertTrue(self.game.tieCondition())

    def testAlternatingTurns(self):
        self.assertCurrentPlayer(1)
        self.game.advancegame()
        self.assertCurrentPlayer(2)
        self.game.advancegame()
        self.assertCurrentPlayer(1)

    def testAssertCurrentPlayerFailure(self):
        self.assertCurrentPlayer(1)
        with self.assertRaises(AssertionError):
            self.assertCurrentPlayer(2)

    def testMakeMove(self):
        self.game.move(0, 0)
        self.assertCurrentPlayerOwns(0, 0)

    def testAssertCurrentPlayerOwnsFailure(self):
        with self.assertRaises(AssertionError):
            self.assertCurrentPlayerOwns(0, 0)

    def testMakeSameMoveFails(self):
        self.game.move(0, 0)
        self.assertRaises(Exception, self.game.move, 0, 0)

    def testMakeOffBoardMoveFails(self):
        self.assertRaises(Exception, self.game.move, -1, 0)
        self.assertRaises(Exception, self.game.move, 0, -1)
        self.assertRaises(Exception, self.game.move, -1, -1)
        self.assertRaises(Exception, self.game.move, 3, 0)

    def testPlayAlternatesTurns(self):
        self.assertCurrentPlayer(1)
        self.game.play(0, 0)
        self.assertCurrentPlayer(2)
        self.game.play(0, 1)
        self.assertCurrentPlayer(1)

    def testPlayStaysOnCurrentPlayerOnBadMove(self):
        self.assertCurrentPlayer(1)
        self.game.play(-1, 0) # Bad move
        self.assertCurrentPlayer(1)
        self.game.play(0, 0) # Good move
        self.assertCurrentPlayer(2)
        self.game.play(0, 0) # Bad move
        self.assertCurrentPlayer(2)

    def testFirstRowPlayer1Wins(self):
        self.game.board[(0,0)] = 1
        self.game.board[(0,1)] = 1
        self.game.board[(0,2)] = 1
        self.assertWinner(1)

    def testFirstRowPlayer1Wins(self):
        self.game.board[(0,0)] = 1
        self.game.board[(0,1)] = 2
        self.game.board[(0,2)] = 2
        with self.assertRaises(AssertionError):
            self.assertWinner(1)

    def testFirstRowPlayer2Wins(self):
        self.game.board[(0,0)] = 2
        self.game.board[(0,1)] = 2
        self.game.board[(0,2)] = 2
        self.assertWinner(2)

    def testSecondRowPlayer2Wins(self):
        self.game.board[(1,0)] = 2
        self.game.board[(1,1)] = 2
        self.game.board[(1,2)] = 2
        self.assertWinner(2)

    def testAssertWinnerFailure(self):
        with self.assertRaises(AssertionError):
            self.assertWinner(1)
        with self.assertRaises(AssertionError):
            self.assertWinner(2)

    def testFullGame(self):
        self.game.play(0,0)
        self.game.play(1,0)
        self.game.play(0,1)
        self.game.play(1,2)
        with self.assertRaises(SystemExit) as e:
            self.game.play(0,2)
        self.assertEqual(e.exception.code, 0)

    def testTieCondition(self):
        self.game.board[(0,0)] = 2
        self.game.board[(0,1)] = 1
        self.game.board[(0,2)] = 1
        self.game.board[(1,0)] = 1
        self.game.board[(1,1)] = 2
        self.game.board[(1,2)] = 2
        self.game.board[(2,0)] = 1
        self.game.board[(2,1)] = 2
        self.game.board[(2,2)] = 1
        self.assertTie()

    def testTieConditionFailure(self):
        with self.assertRaises(AssertionError):
            self.assertTie()

    def testTieGame(self):
        self.game.play(0,1)
        self.game.play(0,0)
        self.game.play(0,2)
        self.game.play(1,1)
        self.game.play(1,0)
        self.game.play(1,2)
        self.game.play(2,0)
        self.game.play(2,1)
        with self.assertRaises(SystemExit) as e:
            self.game.play(2,2)
        self.assertEqual(e.exception.code, 0)
        self.assertTrue(self.game.tieCondition())

    exampleGameBoard =  " X |   |   \n"
    exampleGameBoard += "---+---+---\n"
    exampleGameBoard += "   |   |   \n"
    exampleGameBoard += "---+---+---\n"
    exampleGameBoard += "   |   |   \n"
    def test__str__(self):
        self.game.play(0,0)
        self.assertEqual(self.exampleGameBoard, str(self.game))

    def test__str__failure(self):
        self.assertNotEqual(self.exampleGameBoard, str(self.game))

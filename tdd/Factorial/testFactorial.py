#!/usr/local/bin/python
import unittest2

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return 1

class TestFactorial (unittest2.TestCase):
    #note: error cases such as negative numbers are not tested for
    def testSomething(self):
        self.assertEquals(1, factorial(0))
        self.assertEquals(1, factorial(1))
        self.assertEquals(2, factorial(2))
        self.assertEquals(6, factorial(3))
        self.assertEquals(24, factorial(4))
        self.assertEquals(120, factorial(5))
        self.assertEquals(720, factorial(6))

#!/usr/bin/python
import unittest2
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest2.TestCase):
    def testFizzBuzz(self):
        self.assertEquals(1, fizzbuzz(1))
        self.assertEquals(2, fizzbuzz(2))
        self.assertEquals("fizz", fizzbuzz(3))
        self.assertEquals(4, fizzbuzz(4))
        self.assertEquals("buzz", fizzbuzz(5))
        self.assertEquals("fizz", fizzbuzz(6))
        self.assertEquals("fizz", fizzbuzz(9))
        self.assertEquals("buzz", fizzbuzz(10))
        self.assertEquals(11, fizzbuzz(11))
        self.assertEquals("fizzbuzz", fizzbuzz(15))

#!/usr/bin/python
import unittest2
#Based on Dave's https://bitbucket.org/dbesen/random/src/HEAD/tdd/easy-not.py


class Negativizer(object):
    def __init__(self, parent):
        self.parent = parent

    def __getattr__(self, name):
        def replacement_method(*args, **kwargs):
            try:
                self.parent.__getattribute__(name)(*args, **kwargs)
            except AssertionError:
                pass
            else:
                raise AssertionError("Expected AssertionError, not found")
        return replacement_method


class TestEasyNot(unittest2.TestCase):
    def setUp(self):
        self.Not = Negativizer(self)

    def test_passes(self):
        self.assertEquals(1, 1)
        self.Not.assertEquals(1, 2)

    def test_equals_fails(self):
        with self.assertRaises(AssertionError):
            self.assertEquals(1, 2)

    def test_not_equals_fails(self):
        with self.assertRaises(AssertionError):
            self.Not.assertEquals(1, 1)

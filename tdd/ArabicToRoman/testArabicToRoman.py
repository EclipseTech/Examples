#!/usr/local/bin/python
import unittest2
from collections import OrderedDict

# 1 = I
# 2 = II
# 3 = III
# 4 = IV

numerals = OrderedDict(
    [(1000, "M"),
     (900, "CM"),
     (500, "D"),
     (400, "CD"),
     (100, "C"),
     (90, "XC"),
     (50, "L"),
     (40, "XL"),
     (10, "X"),
     (9, "IX"),
     (5, "V"),
     (4, "IV"),
     (1, "I")])


def arabicToRoman(arabic):
    roman=""
    for arabicNumeral, romanNumeral in numerals.items():
        roman+=romanNumeral*(arabic/arabicNumeral)
        arabic%=arabicNumeral
    return roman


class TestarabicToRoman(unittest2.TestCase):
    def testConversions(self):
        self.assertEquals("I", arabicToRoman(1))
        self.assertEquals("II", arabicToRoman(2))
        self.assertEquals("III", arabicToRoman(3))
        self.assertEquals("IV", arabicToRoman(4))
        self.assertEquals("V", arabicToRoman(5))
        self.assertEquals("X", arabicToRoman(10))
        self.assertEquals("XI", arabicToRoman(11))
        self.assertEquals("XX", arabicToRoman(20))
        self.assertEquals("XXX", arabicToRoman(30))
        self.assertEquals("L", arabicToRoman(50))
        self.assertEquals("LX", arabicToRoman(60))
        self.assertEquals("MDCCC", arabicToRoman(1800))
        self.assertEquals(arabicToRoman(2499), "MMCDXCIX")
        self.assertEquals(arabicToRoman(3949), "MMMCMXLIX")

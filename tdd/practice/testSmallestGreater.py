import unittest2


'''
Smallest greater elements in whole array
An array is given of n length, and we need to calculate the next greater element for each element in given array. If next greater element is not available in given array then we need to fill '_' at that index place.
'''
def smallestGreater(array):
    indexLargest = None
    newArray = array[:]

    for i in range(len(array)):
        index = None
        nextLargestNum = None
        for j in range(len(array)):
            if array[j] > array[i] and i != j:
                if nextLargestNum is None or array[j] < nextLargestNum:
                    nextLargestNum = array[j]
                    index = j
        if nextLargestNum is None:
            indexLargest = i
        else:
            newArray[i] = array[index]

    newArray[indexLargest] = '_'
    return newArray


class TestsmallestGreater(unittest2.TestCase):
    def test1(self):
        arrayInput = [1]
        expectedOutput = ['_']
        self.assertEqual(smallestGreater(arrayInput), expectedOutput)

        arrayInput = [1, 2]
        expectedOutput = [2, '_']
        self.assertEqual(smallestGreater(arrayInput), expectedOutput)

        arrayInput = [2, 1]
        expectedOutput = ['_', 2]
        self.assertEqual(smallestGreater(arrayInput), expectedOutput)

        arrayInput = [4, 3, 2, 1]
        expectedOutput = ['_', 4, 3, 2]
        self.assertEqual(smallestGreater(arrayInput), expectedOutput)

        arrayInput = [6, 3, 9, 8, 10, 2, 1, 15, 7]
        expectedOutput = [7, 6, 10, 9, 15, 3, 2, '_', 8]
        self.assertEqual(smallestGreater(arrayInput), expectedOutput)

        arrayInput = [13, 6, 7, 12]
        expectedOutput = ['_', 7, 12, 13]
        self.assertEqual(smallestGreater(arrayInput), expectedOutput)

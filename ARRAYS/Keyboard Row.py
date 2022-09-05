# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
from ast import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # made the set of three rows of keyboard characters
        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        res = []
        for word in words:
            # made the set of each word in the list words
            wrd = set(word.lower())
            # if intersection of the set of each word with any row is equal to word itself then that word is the answer
            if (wrd & set1 == wrd) or (wrd & set2 == wrd) or (wrd & set3 == wrd):
                res.append(word)

        return res

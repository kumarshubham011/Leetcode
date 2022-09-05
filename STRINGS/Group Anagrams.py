# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from ast import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            # as sorted return comma seperated list
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dict:
                dict[sorted_word] = [word]
            else:
                dict[sorted_word].append(word)

        result = []
        for value in dict.values():
            result.append(value)
        return result

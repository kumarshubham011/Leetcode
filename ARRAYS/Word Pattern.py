# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# METHOD 1: USING ONE DICTIONARY
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        dic = {}
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        # for eg pattern = "aa" and words = ['dog', 'cat'] -> return False

        for i in range(len(words)):
            if words[i] not in dic:
                # simply map pattern with the word
                dic[words[i]] = pattern[i]

            elif dic[words[i]] != pattern[i]:
                # this pattern has already been mapped -> check if the current word mathces previous mapping
                return False
        return True


# TWO DICTIONARY SOLUTION
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        wordtochar, chartoword = {}, {}
        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c in chartoword and chartoword[c] != w:
                return False
            elif w in wordtochar and wordtochar[w] != c:
                return False
            # map c and w to their respective hashmaps
            wordtochar[w] = c
            chartoword[c] = w
        return True

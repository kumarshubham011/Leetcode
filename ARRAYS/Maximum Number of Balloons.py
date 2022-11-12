from collections import Counter
import math


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        countBall = Counter('balloon')
        res = math.inf
        for c in countBall:
            res = min(res, countText[c] // countBall[c])
        return res

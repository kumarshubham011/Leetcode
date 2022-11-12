# O(N) space
from ast import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # add two zeros one at start and other at end
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

# O(1) SPACE:


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0

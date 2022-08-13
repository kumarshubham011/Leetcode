class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        print(res << 2)
        for i in range(32):
            # left shift the result
            res = res << 1
            print(res)
            if n & 1 == 1:
                res += 1
            # print(res)
            n = n // 2
        return res

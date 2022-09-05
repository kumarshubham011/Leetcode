# METHOD 1- ITERATIVE

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        r = [0, 1]
        a = 0
        b = 1
        for i in range(2, n):
            res = a + b
            a = b
            b = res
            r.append(res)

        return r[n-1] + r[n-2]

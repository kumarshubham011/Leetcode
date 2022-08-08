# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2  # if n%2 is 0 then adding it to count will have no effect that's why we haven't added if statements
            n = n//2  # right shifting to dump lsb and check the next bit
        return count

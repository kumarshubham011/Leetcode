# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.

def stairs(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return stairs(n-1) + stairs(n-2) + stairs(n-3)


print(stairs(5))
print(stairs(4))

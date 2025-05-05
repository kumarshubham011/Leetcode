# Problem statement
# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N-dimensional forest.

# Example:
# Input: ‘N’ = 3

# Output: 
# * * *
# * * *
# * * *

def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(n):
            print('* ', end="")
        print()

print(nForest(3))


# Example:
# Input:  ‘N’ = 3

# Output: 
# * 
# * *
# * * *

def nForest(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()

print(nForest(3))


# Example:
# Input: ‘N’ = 3

# Output: 
# 1
# 1 2 
# 1 2 3

def nTriangle(n:int) ->None:
    # Write your solution here.
    for i in range(n):
        for j in range(i+1):
            print(f"{j+1} ", end="")
        print()
print(nTriangle(3))



# Input: ‘N’ = 3

# Output: 
# 1
# 2 2 
# 3 3 3

def triangle( n:int) ->None:
    # Write your solution here.
        for i in range(n):
            res = i+1
            for j in range(i+1):
                print(f"{res} ", end="")
            print()

print(triangle(3))


# Input: ‘N’ = 3

# Output: 
# * * *
# * *

def seeding(n: int) -> None:
    # Write your solution here.
        for i in range(n):
            for j in range(n-i):
                print("* ", end="")
            print()

print(seeding(3))


# Input: ‘N’ = 3

# Output: 

# 1 2 3
# 1 2
# 1
def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n):
        for j in range(n - i):
            print(f"{j+1} ", end="")
        print()
print(nNumberTriangle(3))


# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****

def nStarTriangle(n: int) -> None:
    # Write your code here.
        for i in range(n):
            # space
            for j in range(n-i-1):
                print(" ", end="")
            # star
            for j in range(2*i + 1):
                print("*", end="")
            # space
            for j in range(n-i-1):
                print(f" ", end="")
            print()
print(nStarTriangle(3))


# Input: ‘N’ = 3

# Output: 

# *****
#  ***
#   *

def nStarTriangle(n: int) -> None:
    for i in range(n):
        #space
        for j in range(i):
            print(" ", end="")

        #stars
        for j in range(2*n - 1 - 2*i):
            print("*", end="")
        
        #space
        for j in range(i):
            print(" ", end="")
        print()



# Example:
# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****
# *****
#  ***
#   *

def nStarDiamond(n: int) -> None:
    # for first pyramid patter
    for i in range(n):
        # space
        for j in range(n-i-1):
            print(" ", end="")
        # star
        for j in range(2*i + 1):
            print("*", end="")
        # space
        for j in range(n-i-1):
            print(" ", end="")
        print()
    
    # for secodn pyramid pattern
    for i in range(n):
        # space
        for j in range(i):
            print(" ", end="")
        # star
        for j in range(2*n - 1 - 2*i):
            print("*", end="")
        # space
        for j in range(i):
            print(" ", end="")
        print()


#  Rotated Triangle
# Example:
# Input: ‘N’ = 3

# Output: 

# *
# **
# ***
# **
# *

def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(1, 2*n ):
        stars = i
        if i > n:
            stars = 2*n - i # ex: 6-4
        for j in range(stars):
            print("*", end="")

        print()
print(nStarTriangle(3))


# Example:
# Input: ‘N’ = 3

# Output: 

# 1
# 0 1
# 1 0 1

def nBinaryTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(1,n+1):
        if i%2 == 0:
            start = 0
        else:
            start = 1

        for j in range(i):
            print(start, end=" ")
            start = 1-start # 0 becomes 1, 1 becomes 0
        print()


# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
def numberCrown(n: int) -> None:
    for i in range(1, n+1):
        # numbers
        for j in range(1, i+1):
            print(j, end="")
        # space
        for j in range (0, 2 * (n-i)):
            print(" ", end="")
        # numbers
        for j in range(i, 0, -1):
            print(j, end="")

        print()

print(numberCrown(5))



# Sample Input 2 :
# 4
# Sample Output 2 :
# 1
# 2 3
# 4 5 6 
# 7 8 9 10

def nNumberTriangle(n: int) -> None:
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end=" ")
            num += 1
        print()


# Example:
# Input: ‘N’ = 3

# Output: 

# A
# A B
# A B C

def nLetterTriangle(n: int) -> None:
    for i in range(1, n+1):
        for j in range(65, 65 + i):
            print(chr(j), end=" ")
        print()




# Input: ‘N’ = 3

# Output: 

# A B C
# A B
# A

def nLetterTriangle(n: int):
    for i in range(1, n+1):
        for j in range(65, 65 + n + 1 -i):
            print(chr(j), end= " ")
        print()

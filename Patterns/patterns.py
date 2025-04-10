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
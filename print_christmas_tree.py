import sys
# Happy Holidays!
# with height = 5:
#     *
#    ***
#   *****
#  *******
# *********
#     |
# Dependency: Python 3.3

def printTree(height):        
    stars = 1
    for i in range(height):
        print((' ' * (height - i)) + ('*' * stars))
        stars += 2
    print((' ' * height) + '|')
    

printTree(5)

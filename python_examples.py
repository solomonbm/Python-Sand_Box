#https://www.codementor.io/python/tutorial/essential-python-interview-questions
#http://cs231n.github.io/python-numpy-tutorial/#python
import math
import os

def string_operations():
    hello = 'hello'   # String literals can use single quotes
    world = "world"   # or double quotes; it does not matter.
    print (hello)       # Prints "hello"
    print (len(hello))  # String length; prints "5"
    hw = hello + ' ' + world  # String concatenation
    print (hw)  # prints "hello world"
    hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
    print (hw12)  # prints "hello world 12"
    s = "hello"
    print (s.capitalize())  # Capitalize a string; prints "Hello"
    print (s.upper())       # Convert a string to uppercase; prints "HELLO"
    print (s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
    print (s.center(7))     # Center a string, padding with spaces; prints " hello "
    print (s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                                     # prints "he(ell)(ell)o"
    print ('  world '.strip())  # Strip leading and trailing whitespace; prints "world"

def lists_operations():
    xs = [3, 1, 2]   # Create a list
    print (xs, xs[2])  # Prints "[3, 1, 2] 2"
    print (xs[-1])     # Negative indices count from the end of the list; prints "2"
    xs[2] = 'foo'    # Lists can contain elements of different types
    print (xs)         # Prints "[3, 1, 'foo']"
    xs.append('bar') # Add a new element to the end of the list
    print (xs)         # Prints "[3, 1, 'foo', 'bar']"
    x = xs.pop()     # Remove and return the LAST(!) element of the list
    print (x, xs)      # Prints "bar [3, 1, 'foo']"
    nums = range(5)    # range is a built-in function that creates a list of integers
    print (nums)         # Prints "[0, 1, 2, 3, 4]"
    print (nums[2:4])    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
    print (nums[2:])     # Get a slice from index 2 to the end; prints "[2, 3, 4]"
    print (nums[:2])     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
    print (nums[:])      # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
    print (nums[:-1])    # Slice indices can be negative; prints ["0, 1, 2, 3]"
    nums[2:4] = [8, 9] # Assign a new sublist to a slice
    print (nums)         # Prints "[0, 1, 8, 9, 4]"
    animals = ['cat', 'dog', 'monkey']
    for idx, animal in enumerate(animals):
        print ('#%d: %s' % (idx + 1, animal)) # Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line
    # List comprehensions:
    nums = [0, 1, 2, 3, 4]
    squares = [x ** 2 for x in nums]
    print (squares)   # Prints [0, 1, 4, 9, 16]
    even_squares = [x ** 2 for x in nums if x % 2 == 0]
    print (even_squares)  # Prints "[0, 4, 16]"

def dictionaries_operations():
    d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
    print (d['cat'])       # Get an entry from a dictionary; prints "cute"
    print ('cat' in d)     # Check if a dictionary has a given key; prints "True"
    d['fish'] = 'wet'    # Set an entry in a dictionary
    print (d['fish'])      # Prints "wet"
    # print d['monkey']  # KeyError: 'monkey' not a key of d
    print (d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
    print (d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
    del d['fish']        # Remove an element from a dictionary
    print (d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"
    d = {'person': 2, 'cat': 4, 'spider': 8}
    for animal in d:
        legs = d[animal]
        print ('A %s has %d legs' % (animal, legs)) # Prints "A person has 2 legs", "A spider has 8 legs", "A cat has 4 legs"
    # Dictionary comprehensions:
    nums = [0, 1, 2, 3, 4]
    even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
    print (even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"

def tuples():
    # A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important
    # differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a
    # trivial example:
    d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
    t = (5, 6)       # Create a tuple
    print (type(t))    # Prints "<type 'tuple'>"
    print (d[t])       # Prints "5"
    print (d[(1, 2)])  # Prints "1"
        
def FirstReverse(str):
    
    newStr = ''.join((str[i] for i in range(len(str)-1,-1,-1)))
    # range([start], stop[, step])
    # start: Starting number of the sequence. which is len(str)-1 becuse string starts at index = 0 and ends at index = len(str)-1
    # stop: Generate numbers up to, but not including this number. since we are stepping backwards, and so we want to generate the numbers up to 0 it will be -1
    # step: Difference between each number in the sequence. Iterating backwards one char by one so -1
    # str.join(sequence) - The method join() returns a string in which the string elements of sequence have been joined by str separator.
    return newStr
    
def FirstFactorial(num): 

    if num == 1:
        return 1
        
    return num*FirstFactorial(num-1)

def LetterChanges(str): 

    aToZ = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    aToZLength = len(aToZ)
    newStr = ''
    for i in str:
        if i in aToZ:
            pos = aToZ.index(i)        
            if pos < aToZLength-1:
                char = aToZ[pos+1]
                if char in vowels:
                    char = char.upper()
                newStr += char
            else:
                newStr += 'A'
        else:
            newStr += i
        
    return newStr

def SimpleAdding(num):
    if num == 1:
        return num
    return num + SimpleAdding(num-1)

def LetterCapitalize(str): 

     # split the string into a list
     words = str.split(" ")

     # we split the word into two parts and then combine the parts 
     # the first part is the first letter which we capitalize and the 
     # second part is the rest of the string
     for i in range(0, len(words)):
         words[i] = words[i][0].upper() + words[i][1:]

     # return the list of words joined into a string
     return " ".join(words)

def SimpleSymbols(str):

    # pad the strings so that if a character exists at the beginning
    # of the string for example, we don't get on out-of-bounds error by
    # trying to get the character before it
    str = '=' + str + '='

    # loop through the entire string
    for i in range(0, len(str)):
    
        # check to see if current character is an alphabetic character  
        if str[i].isalpha():

          # check to see if a + symbol is to the left and right
          # if not, then we know this string is not valid
          if str[i-1] != '+' or str[i+1] != '+':
            return 'false'

    return 'true'

def TimeConvert(num):

    hoursNeedZero = ''
    minuetsNeedZero = ''
    # to get the hours, we divide num by 60 and round it down
    # e.g. 61 / 60 = 1 hour
    # e.g. 43 / 60 = 0 hours
    hours = int(math.floor(num / 60))
    if hours < 10:
        hoursNeedZero = '0'

    # to get the minutes, now we use the remainder that we discarded above
    # the modulo operation is represented by the % symbol
    # e.g. 61 % 60 = 1 minute
    # e.g. 43 % 60 = 43 minutes
    minutes = num % 60
    if minutes < 10:
        minutesNeedZero = '0'
        
    # combine the hours and minutes
    return hoursNeedZero + str(hours) + ':' + minutesNeedZero + str(minutes);
        
def AlphabetSoup(str): 
    
    return ''.join(sorted(str))

def print_directory_contents(sPath):                                           
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr) / 2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def default_val_in_memory_ex(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

# *args,**kwargs examples:
def f(*args,**kwargs): print(args, kwargs)
def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)



def main():
    print (FirstReverse("Coderbyte"))
    print (FirstFactorial(4))
    print (LetterChanges("hello*3"))
    print (SimpleAdding(4))
    print (LetterCapitalize("hello world from coderbyte"))
    print (SimpleSymbols("+d+=3=+s+"))
    print (TimeConvert(124))
    print (AlphabetSoup("hooplah"))
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i:i*i for i in A1}
    A6 = [[i,i*i] for i in A1]
    Aarr = [A0, A1, A2, A3, A4, A5, A6]
    for i in range(7):
        print('A'+str(i)+' = '+str(Aarr[i]))
    print_directory_contents('C:\MyProjects')
    print (quicksort([3,6,8,10,1,2,1]))
    default_val_in_memory_ex(2)
    default_val_in_memory_ex(3,[3,2,1])
    default_val_in_memory_ex(3)
    # *args,**kwargs examples:
    l = [1,2,3]
    t = (4,5,6)
    d = {'a':7,'b':8,'c':9}

    f()
    f(1,2,3)                    # (1, 2, 3) {}
    f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
    f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
    f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
    f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

    f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
    f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
    f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
    f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f2(1,2,3)                       # 1 2 (3,) {}
    f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
    f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
    f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
    f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

    f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
    f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
    f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
    f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    
if __name__ == "__main__":
    main()


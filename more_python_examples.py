#For layout
def print_new_section(section_no, section_name):
    print("--------------------")
    print("#{} {}".format(section_no, section_name))
    print("--------------------")
#1
def print_list_enum(list1):
    '''Prints two elemnt tuples of the list1 list elements
        in the order which they appear
        with their order number'''
    for i, elem in enumerate(list1):
        print(i, elem)

#2
def check_if_prime(n):
    '''Checks if a given number is a prime number
        according to Wilson's therom, which claims that
        if p is a prime then ((p-1)! + 1) is divisable by p'''
    import math
    print("is {} a prime? {}".format(n,(math.factorial(n-1) + 1)%n == 0))

#3
def print_age_with_default(ages, name):
    '''Prints the name's age if appears in the ages dict'''
    age = ages.get(name, 57)
    print("{} is {} years old".format(name, age))

#4
def find_the_needle(haystack, needle):
    '''Given a list of letters - "haystack",
        find the letter "needle" within the "haystack" list.
        if found - print "Found!
        if not found print "Not Found!'''
    for letter in haystack:
        if letter == needle:
            print('Found!')
            break
    else: # if no break occurred
        print('Not Found!')

#5
def print_directory_contents(sPath):
    import os
    dirs = os.listdir(sPath)
    for sChild in dirs:
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)        
    
def main():
    list1 = ['Marseille', 'Amsterdam', 'New York', 'London']
    print_new_section(1, 'print_list_enum')    
    print_list_enum(list1)
    print_new_section(2, 'check_if_prime')
    check_if_prime(19)
    check_if_prime(100)
    check_if_prime(5003)
    print_new_section(3, 'print_age_with_default')    
    ages = {'Mary' : 31,'Jonathan' : 28}
    print_age_with_default(ages, 'Mary')
    print_age_with_default(ages, 'Dick')
    print_new_section(4, 'find_the_needle')    
    needle = 'd'
    haystack = ['a', 'b', 'c']
    find_the_needle(haystack, needle)
    print_new_section(5, 'print_directory_contents')
    sPath = 'C:\\MyProjects\\PyDev\\PythonTest'
    print_directory_contents(sPath)
    
if __name__ == "__main__":
    main()
    

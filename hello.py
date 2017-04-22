def main():
    print('Hello World!')
    print('What is your name?')
    my_name = input()
    print('It is good to meet you, '+my_name)
    print('The length of your name is: '+str(len(my_name)))
    print('What is your age?')
    my_age = int(input())
    print('You will be '+str(my_age+1)+' in a year.')
    

if __name__ == "__main__":
    main()

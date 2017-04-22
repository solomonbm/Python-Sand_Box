def reverseString(str):
    #newStr = ''.join((str[i] for i in range(len(str)-1,-1,-1)))
    newStr = str[::-1]
    return newStr


def main():
    print(reverseString("ijneB si eman yM"))

if __name__ == "__main__":
    main()
    

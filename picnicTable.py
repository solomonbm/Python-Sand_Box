def printPicnic(itemsDict, leftWidth, rightWidth):
    strHeader = 'PICNIC ITEMS'
    print(strHeader.center(len(strHeader)*2, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

def main():
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    printPicnic(picnicItems, 12, 5)
    printPicnic(picnicItems, 20, 6)

if __name__ == "__main__":
    main()
    

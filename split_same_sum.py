def split_index(myList):
    if len(myList) < 2:
        return -1
    sumLeft, sumRight = 0, sum(myList)
    return search_split_index(myList, 0, sumLeft, sumRight)

def search_split_index(myList, idx, sumLeft, sumRight):
    if sumLeft == sumRight:
        return idx
    if sumLeft > sumRight:
        return -1
    return search_split_index(myList, idx+1, sumLeft+myList[idx], sumRight-myList[idx])

    
def main():
    l1 = [1,2,3,1,2,3]
    l2 = [1,5,2,4,6]
    l3 = [1]
    l4 = [1,5,2,4,0]
    l5 = [1,2,2,5]
    l6 = []
    print("index of l1 = "+str(split_index(l1)))
    print("index of l1 = "+str(split_index(l2)))
    print("index of l1 = "+str(split_index(l3)))
    print("index of l1 = "+str(split_index(l4)))
    print("index of l1 = "+str(split_index(l5)))
    print("index of l1 = "+str(split_index(l6)))

if __name__ == "__main__":
    main()

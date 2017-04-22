class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, data):
        self.data = data
        return self.data

    def setNext(self, next):
        self.next = next

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next != None


class singleLinkList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(newNode)

    def listLength(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        return count

    def print_llist(self):
        current = self.head        
        while current != None:
            print(str(current.getData())+' ->'),
            current = current.getNext()
        print('Null')    

def main():
    ll = singleLinkList()
    ll.insertAtBeginning(55)
    ll.insertAtEnd(2)
    ll.insertAtEnd(56)
    ll.insertAtEnd(1)
    ll.insertAtEnd(20)
    ll.insertAtEnd(16)
    ll.insertAtEnd(9)
    ll.insertAtEnd(7)
    ll.insertAtEnd(3)
    ll.print_llist()
    print(ll.listLength())

if __name__ == "__main__":
    main()

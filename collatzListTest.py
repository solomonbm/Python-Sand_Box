typeOfsons = ["(N)","(B)","(A)"]

def collatzList(n):
    "This function returns the upward list of odd numbers in the oddTree from a start point n"
    if n == 1:
        print "1"
        return
    if n%2 == 0:
        return collatzList(n/2)
    
    print typeOfsons[n%3] + str(n) + "-->",
    return collatzList(3*n + 1)

def getParent(n):
    n = n*3 + 1
    while n%2 == 0:
        n = n/2

    return n

def getDistance(n,d):    
    if n == 1:
        return d
    elif n%2 == 0:
        return getDistance(n/2,d)
    else:            
        return getDistance(3*n + 1,d+1)    
    
def getData(n):
    data = {'Number': n, 'Parent': getParent(n), 'Distance': getDistance(n,0), 'TypeOfSons': typeOfsons[n%3]}
    print(data)

def collatzListTest():
	n = 2
	while n%2 == 0:
		n = input("Enter an odd number: ")
	t = input("What do you want to see? [1:n's Data, 2:All Lists up To n] ")
	if t == 1:
		getData(n)
	elif t == 2:
		for i in xrange(3,n+1,2):
			collatzList(i)

def main():
    collatzListTest()        
        
    
main()

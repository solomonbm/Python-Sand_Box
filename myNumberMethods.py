from random import *

class myNumberMethods(object):

    def __init__(self):
        # myNumberMethods has a number of optional return variables:
        # retList (example [0,1,1])
        # retInt (example 57)
        # retStr (example "0,1,1,2")
        self.retList = []
        self.retInt = 0
        self.retStr = ""

    def clear(self):
        print()
        self.retList = []
        self.retInt = 0
        self.retStr = ""

    def fibNoRec1(self, n):
        ''' This function returns
            the first n Fibonacci numbers,
            using a WHILE loop '''
        self.clear()
        n1=0
        n2=1
        i=2
        
        if n==1:                        
            self.retList.append(n1)            
        else:            
            self.retList.append(n1)
            self.retList.append(n2)            
                
        while i<n: #loop starts from 2 because 0 and 1 are already printed    
            n3=n1+n2            
            self.retList.append(n3)            
            n1=n2    
            n2=n3
            i = i + 1        

    def fibNoRec2(self, n):
        self.clear()
        a,b = 0,1
        self.retList.append(a)
        for i in range(n-1):
            a,b = b, a+b            
            self.retList.append(a)

    def fibRec(self, n):
        self.clear()
        for i in range(n):
            self.retList.append(self.fibRecOfN(i+1))        

    def fibRecOfN(self, n):
        if n==1:            
            return 0
        elif n==2:            
            return 1
        return self.fibRecOfN(n-1) + self.fibRecOfN(n-2)   

    def isIntPalindrome(self, n):        
        r,temp,m = 0, 0, n
        while m>0:
            r = m%10            
            temp = (temp*10)+r
            m = m//10           

        if temp==n:
            return True
        else:
            return False

    def isStrPalindrome(self, s):        
        strLength = len(s)
        if strLength==0 or strLength==1:
            return True
        elif s[0]==s[strLength-1]:
            return self.isStrPalindrome(s[1:strLength-1])

        return False

    def isArmstrongNumber(self, n):
        ''' Armstrong number is a number that is equal to
            the sum of cubes of its digits for example 0, 1, 153, 370, 371, 407 etc.
	    153 = (1*1*1)+(5*5*5)+(3*3*3)  
	    where:  
	    (1*1*1)=1  
	    (5*5*5)=125  
	    (3*3*3)=27  
	    So:  
	    1+125+27=153 '''
        c,a,m = 0, 0, n
        while m>0:
            a = m%10            
            c = c+(a*a*a)
            m = m//10           

        if c==n:
            return True
        else:
            return False

    def randIntList(self, listLength, listRange):        
        self.clear()
        self.retList = [randint(0,listRange) for b in range(listLength)]
            
def main():
    mnm = myNumberMethods()
    common_int = 3
    mnm.fibNoRec1(common_int)    
    print(mnm.retList)
    mnm.fibNoRec2(common_int)
    print(mnm.retList)    
    mnm.fibRec(common_int)
    print(mnm.retList)
    print(mnm.isIntPalindrome(43434))
    print(mnm.isStrPalindrome("4gg34"))
    print(mnm.isArmstrongNumber(371))
    mnm.randIntList(3,2)
    print(mnm.retList)
    

if __name__ == "__main__":
    main()
    

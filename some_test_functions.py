def findSumInList(n,l):
    

def isPalindrome(s):
    return s == s[::-1]
    
def XO(s):
    count_o, count_x, length = 0, 0, len(s)
    for i in range(length):
        if s[i] == 'o':
            count_o += 1
        elif s[i] == 'x':
            count_x += 1
    return count_o == count_x

def main():
    print('XO("xoxxo"): '+str(XO('xoxxo')))
    print('XO("xoxoxo"): '+str(XO('xoxoxo')))
    print('XO("zqzqq"): '+str(XO('zqzqq')))
    print('isPalindrome("xoxox"): '+str(isPalindrome('xoxox')))
    print('isPalindrome("xoxoxo"): '+str(isPalindrome('xoxoxo')))
    print('isPalindrome("zqzqq"): '+str(isPalindrome('zqzqq')))

if __name__ == "__main__":
    main()

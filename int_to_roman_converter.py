from collections import OrderedDict

def int_to_roman(input):
   """
   Convert an integer to Roman numerals.

   Examples:
   >>> int_to_roman(0)
   Traceback (most recent call last):
   ValueError: Argument must be between 1 and 3999

   >>> int_to_roman(-1)
   Traceback (most recent call last):
   ValueError: Argument must be between 1 and 3999

   >>> int_to_roman(1.5)
   Traceback (most recent call last):
   TypeError: expected integer, got <type 'float'>

   >>> for i in range(1, 21): print int_to_roman(i)
   ...
   I
   II
   III
   IV
   V
   VI
   VII
   VIII
   IX
   X
   XI
   XII
   XIII
   XIV
   XV
   XVI
   XVII
   XVIII
   XIX
   XX
   >>> print int_to_roman(2000)
   MM
   >>> print int_to_roman(1999)
   MCMXCIX
   """
   
   if type(input) != type(1):
      raise TypeError, "expected integer, got %s" % type(input)
   if not 0 < input < 4000:
      raise ValueError, "Argument must be between 1 and 3999"   
   '''ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')'''
   roman = OrderedDict()
   roman[1000] = "M"
   roman[900] = "CM"
   roman[500] = "D"
   roman[400] = "CD"
   roman[100] = "C"
   roman[90] = "XC"
   roman[50] = "L"
   roman[40] = "XL"
   roman[10] = "X"
   roman[9] = "IX"
   roman[5] = "V"
   roman[4] = "IV"
   roman[1] = "I"
   result = ""
   for q in roman.keys():      
    # input = m*q + r
      m = int(input / q)
      result += roman[q] * m
      input -= (q * m)
   return result

def main():
    print('int_to_roman(6): '+int_to_roman(6))
    print('int_to_roman(65): '+int_to_roman(65))
    print('int_to_roman(56): '+int_to_roman(56))
    print('int_to_roman(12): '+int_to_roman(12))
    print('int_to_roman(45): '+int_to_roman(45))
    print('int_to_roman(-8): '+int_to_roman(-8))
    

if __name__ == "__main__":
    main()

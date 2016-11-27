'''Enumerate'''
cities = ['Marseille', 'Amsterdam', 'New York', 'London']
# The bad way
i = 0
for city in cities:
    print(i, city)
    i += 1
# The good way
for i, city in enumerate(cities):
    print(i, city)

'''Zip'''
x_list = [1,2,3]
y_list = [4,5,6]
# The bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)
# The good way
for x, y in zip(x_list, y_list):
    print(x, y)

'''Tuple'''
x = 10
y = -10
print('Before: x = %d, y = %d' % (x, y))
# The bad way
tmp = y
y = x
x = tmp
print('After: x = %d, y = %d' % (x, y))
# The good way
x, y = y, x
print('After: x = %d, y = %d' % (x, y))

'''Dict default'''
ages = {
    'Mary' : 31,
    'Jonathan' : 28
    }
# The bad way
if 'Dick' in ages:
    age = ages['Dick']
else:
    age = 'Unknown'
print('Dick is %s years old' % age)
# The good way
age = ages.get('Dick', 'Unknown')
print('Dick is %s years old' % age)

'''For with else'''
needle = 'd'
haystack = ['a', 'b', 'c']
# The bad way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not Found!')
# The good way
for letter in haystack:
    if needle == letter:
        print('Found!')        
        break
else: # if no break occurred
    print('Not Found!')

'''With open'''
# The bad way
f = open('lay-low.txt')
text = f.read()
for line in text.split('\n'):
    print(line)
f.close()
# The good way
with open('lay-low.txt') as f:
    for line in f:
        print(line)

'''Try'''
print('Converting!')
print(int('1'))
print('Done!')
# The good way
print('Converting!')
try:
print(int('x'))
except:
    print('Conversion failed!')
else: # if no-except
    print('Conversion successful!')
finally: #Always    
    print('Done!')

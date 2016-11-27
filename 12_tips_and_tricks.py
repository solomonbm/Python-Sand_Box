# List Comprehension
print("#List Comprehension: [x ** 2 for x in range(10) if x != 4]")
print([x ** 2 for x in range(10) if x != 4])
# Dict Comprehension
print(">>>")
print("#Dict Comprehension: {x: x ** 2 for x in range(5) if x != 4}")
print({x: x ** 2 for x in range(5) if x != 4})
# Argument Unpacking
print(">>>")
def func(regular_arg, *args, **kwargs):
    print (regular_arg, args, kwargs)
    
print("#Argument Unpacking: def func(regular_arg, *args, **kwargs):")
print("                         print (regular_arg, args, kwargs)")
print("func(1, 2, 3, a=1, b=2)")
func(1, 2, 3, a=1, b=2)
# Triniary IF
print(">>>")
print("#Triniary IF: x = 'yes' if something else 'no'")
# Dictionary get() function
print(">>>")
print("#Dictionary get() function: x = my_dict.get(key, 'default')")
my_dict = {1:"Benji", 2:"Ira", 3:"Tal", 4:"Natan"}
key = 6
x = my_dict.get(key, "default")
print(x)
import this
# Generators
print(">>>")
print("Generators: generator = (x ** 2 for x in range(4))")
generator = (x ** 2 for x in range(4))
next(generator)
print("next(generator)")
next(generator)
print("next(generator)")
for x in generator: print(x)
# List Comprehension
print(">>>")
print("List Comprehension: [(i,j) for i in range(3) for j in range(i)]")
l = [(i,j) for i in range(3) for j in range(i)]
print(l)
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(noprimes)
print(primes)
def foo(x=[]):
    x.append("wa")
    print(x)

foo()
foo()
foo()

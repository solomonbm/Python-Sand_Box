class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is {}".format(self.name))

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("... and I am {}".format(self.hero_name))
        
class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass


def main():
    corey = Person('Corey')
    corey.reveal_identity()

    wade = SuperHero('Wade Wilson', 'Deadpool')
    wade.reveal_identity()

    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    # specify output from here onwards
    print('a.go()')
    a.go()
    print('b.go()')
    b.go()
    print('c.go()')
    c.go()
    print('d.go()')
    d.go()
    print('e.go()')
    e.go()

    print('a.stop()')
    a.stop()
    print('b.stop()')
    b.stop()
    print('c.stop()')
    c.stop()
    print('d.stop()')
    d.stop()
    print('e.stop()')
    e.stop()

    print('a.pause()')
    a.pause()
    print('b.pause()')
    b.pause()
    print('c.pause()')
    c.pause()
    print('d.pause()')
    d.pause()
    print('e.pause()')
    e.pause()

if __name__ == '__main__':
    main()

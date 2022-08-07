# inheritance is a method for resuing code
# dry - don't repeat yourself. den't define something twice

class Mammal:
    def walk(self):
        print("It's walking")

class Dog(Mammal): # to inherit mammal class (parent class)
    def play(self):
        print("The dog is playing")

class Cat(Mammal):
    def purr(self):
        print("Cat is purring")

dog1 = Dog()
dog1.walk()
dog1.play()

cat1 = Cat()
cat1.purr()
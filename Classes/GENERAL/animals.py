class Dog:
    scientific_name = 'Canis Lupus familiaris'

    #Variables which need to be for all new elements should be here
    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print('Bowow')

    def eat(self, food):
        if food == 'biscuit':
            print('yummy')
        else:
            print('That\'s not food')

    #(as we added the init we don't need
    #this method anymore )
    #def learn_name(self, name):
        #self.name = name
    def hear (self, word):
        if self.name in word:
            self.speak()

    def count (self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()

#How to declare an inheritance or sub-class, (Dog) is how we delare from the
#new sub-class inherits
class husk(Dog):
    origem = 'Siberia'

    def speak(self):
        print('Awoooo')


class Cat:
    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("Purr")
        elif self.mood == "angry":
            print("Hiss")
        else:
            print("Meow!")

class Person:
    mood=None
    def __init__(self,id):
        self.id=id
        self.mood = "happy"
        print(self)
    def setMood(self, mood):
        self.mood=mood
    def showMood(self):
        print(self.mood)
    def canVibe(self, majnu):
        #this will take another person object as parameter and return true if both their mood are same else false
        if self.mood == majnu.mood:
            return True
        else:
            return False
        




p1 = Person(1)
p2= Person(2)
p1.setMood("fear")
p1.showMood()
p2.setMood("fun")
p2.showMood()



print(p1.canVibe(p2))
p1.setMood("fun")
print(p1.canVibe(p2))

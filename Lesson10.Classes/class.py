# define a class
class Animal:
    def __init__(self, name, legs_number):
        self.name = name
        self.legs_number = legs_number
    
    def __init__(self, voice):
        self.voice = voice

# when a class is created, the instance variable 'voice' is created and set to the input value
cat = Animal("Meow")
print(cat.voice)

dog = Animal("Woof")
print(dog.voice)
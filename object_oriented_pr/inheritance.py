class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("Say something")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)     #pentru a importa name si age din Pet
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")

c = Cat("Miti", 10, "grey")
c.show()
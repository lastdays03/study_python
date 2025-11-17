class Animal:
    def __init__(self, name):
        self.name = name
        print(f"[Animal] Created with name: {self.name}")

    def speak(self):
        return f"{self.name} makes a sound."

class Flyer:
    def __init__(self, can_fly=True):
        self.can_fly = can_fly
        print(f"[Flyer] Can fly: {self.can_fly}")

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying!"
        else:
            return f"{self.name} can't fly."

class Swimmer:
    def __init__(self, can_swim=True):
        self.can_swim = can_swim
        self.__hidden2 = "hidden2"
        print(f"[Swimmer] Can swim: {self.can_swim}")

    def swim(self):
        if self.can_swim:
            return f"{self.name} is swimming!"
        else:
            return f"{self.name} can't swim."
    
    def get_hidden2(self):
        return self.__hidden2

class Bird(Animal, Flyer):
    def __init__(self, name, can_fly=True):
        Animal.__init__(self, name)
        Flyer.__init__(self, can_fly)
        print(f"[Bird] Initialized: {self.name}, Can fly: {self.can_fly}")

    def speak(self):
        return f"{self.name} chirps."

class Duck(Animal, Flyer, Swimmer):
    def __init__(self, name, can_fly=True, can_swim=True):
        Animal.__init__(self, name)
        Flyer.__init__(self, can_fly)
        Swimmer.__init__(self, can_swim)
        self.__hidden1 = "hidden1"
        print(f"[Duck] Initialized: {self.name}, Can fly: {self.can_fly}, Can swim: {self.can_swim}")

    def speak(self):
        return f"{self.name} quacks."

    def get_hidden1(self):
        return self.__hidden1
    def get_hidden2(self):
        return super().get_hidden2()

if __name__ == "__main__":
    # bird = Bird("Sparrow", can_fly=True)
    # print(bird.speak())
    # print(bird.fly())
    duck = Duck("Donald", can_fly=True, can_swim=True)
    # print(duck.speak())
    # print(duck.fly())
    # print(duck.swim())
    # print(duck.get_hidden1())
    # print(duck.get_hidden2())
    # print(duck.__hidden1)
    # print(duck.__hidden2)
    print(dir(duck))
    print(duck.get_hidden1())
    print(duck._Duck__hidden1)
    duck._Duck__hidden1 = "hidden1_changed"
    print(duck.get_hidden1())
    print(duck._Duck__hidden1)

    print(duck.get_hidden2())
    print(duck._Swimmer__hidden2)
    duck._Swimmer__hidden2 = "hidden2_changed"
    print(duck.get_hidden2())
    print(duck._Swimmer__hidden2)
    print(type(duck))
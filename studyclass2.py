# 다중 상속 예제 (생성자 포함)

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
        print(f"[Swimmer] Can swim: {self.can_swim}")

    def swim(self):
        if self.can_swim:
            return f"{self.name} is swimming!"
        else:
            return f"{self.name} can't swim."

# 다중 상속: Bird는 Animal, Flyer를 상속 (생성자 오버라이딩)
class Bird(Animal, Flyer):
    def __init__(self, name, can_fly=True):
        Animal.__init__(self, name)
        Flyer.__init__(self, can_fly)
        print(f"[Bird] Initialized: {self.name}, Can fly: {self.can_fly}")

    def speak(self):
        return f"{self.name} chirps."

# 다중 상속: Duck는 Animal, Flyer, Swimmer 모두 상속 (생성자 오버라이딩)
class Duck(Animal, Flyer, Swimmer):
    def __init__(self, name, can_fly=True, can_swim=True):
        Animal.__init__(self, name)
        Flyer.__init__(self, can_fly)
        Swimmer.__init__(self, can_swim)
        print(f"[Duck] Initialized: {self.name}, Can fly: {self.can_fly}, Can swim: {self.can_swim}")

    def speak(self):
        return f"{self.name} quacks."

# 사용 예시
if __name__ == "__main__":
    print("-----Bird Example-----")
    bird = Bird("Sparrow", can_fly=True)
    print(bird.speak())      # Sparrow chirps.
    print(bird.fly())        # Sparrow is flying!

    print("\n-----Duck Example-----")
    duck = Duck("Donald", can_fly=True, can_swim=True)
    print(duck.speak())      # Donald quacks.
    print(duck.fly())        # Donald is flying!
    print(duck.swim())       # Donald is swimming!

    # 생성자 파라미터 조작 예
    print("\n-----Penguin Example (Bird can't fly)-----")
    penguin = Bird("Penguin", can_fly=False)
    print(penguin.speak())   # Penguin chirps.
    print(penguin.fly())     # Penguin can't fly.

    print("\n-----Rubber Duck Example (can't fly, can't swim)-----")
    rubber_duck = Duck("Rubber Duck", can_fly=False, can_swim=False)
    print(rubber_duck.speak())    # Rubber Duck quacks.
    print(rubber_duck.fly())      # Rubber Duck can't fly.
    print(rubber_duck.swim())     # Rubber Duck can't swim.

# 다중 상속에서도 super()를 사용할 수 있습니다.
# 다만, 모든 부모 클래스가 super() 호출을 올바르게 사용하도록 설계되어 있어야 하고,
# super()는 MRO(Method Resolution Order)에 따라 부모들을 순서대로 호출합니다.
# 아래는 super()를 써서 생성자를 호출하는 방식을 예시로 보여줍니다.

class Animal:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Flyer:
    def __init__(self, can_fly=True, **kwargs):
        self.can_fly = can_fly
        super().__init__(**kwargs)

    def fly(self):
        if self.can_fly:
            return f"{self.name} is flying!"
        else:
            return f"{self.name} can't fly."

class Swimmer:
    def __init__(self, can_swim=True, **kwargs):
        self.can_swim = can_swim
        super().__init__(**kwargs)

    def swim(self):
        if self.can_swim:
            return f"{self.name} is swimming!"
        else:
            return f"{self.name} can't swim."

# 다중 상속: super()와 MRO 활용
class Duck2(Animal, Flyer, Swimmer):
    def __init__(self, name, can_fly=True, can_swim=True):
        super().__init__(name=name, can_fly=can_fly, can_swim=can_swim)
        print(f"[Duck2] Initialized: {self.name}, Can fly: {self.can_fly}, Can swim: {self.can_swim}")

    def speak(self):
        return f"{self.name} quacks (super version)."

print("\n-----Duck2 Example (super() with multiple inheritance)-----")
duck2 = Duck2("SuperDuck", can_fly=True, can_swim=True)
print(duck2.speak())
print(duck2.fly())
print(duck2.swim())

# 다중 상속 시 super() 사용에 주의: 모든 부모가 super().__init__(**kwargs) 호출 필요!

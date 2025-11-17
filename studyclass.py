class Person:
    cnt = 0
    # __name = "Johnaaa"
    name = "John333"
    def __init__(self, name, age, city="Seoul"):
        self.name = name
        # self.__name = name
        self.age = age
        self.city = city
        Person.cnt += 1
    def say_hello(self):
        print(Person.cnt)
        print(f"Hello, my name is {self.name} and I am {self.age} years old and I live in {self.city}")
    @classmethod
    def get_cnt(cls):
        return cls.cnt
    @staticmethod
    def get_species():
        return "Homo sapiens"
# person = Person("John", 30)
# person.say_hello()

# person1 = Person("Jane", 25, "Busan")
# person1.say_hello()

# print(Person.get_cnt())
# print(Person.get_species())
# print(person.get_cnt())
# print(person.get_species())
# person1.__init__("Jane2", 25, "Busan2")
# print(person1.say_hello())
# print(dir(person))

class Student(Person):
    def __init__(self, name, age, city="Seoul", student_id="1234567890"):
        super().__init__(name, age, city)
        self.student_id = student_id
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old and I live in {self.city} and my student id is {self.student_id}")
student = Student("Jane", 25, "Busan")
student.say_hello()
print(student.get_cnt())
print(student.get_species())
print(student.say_hello())

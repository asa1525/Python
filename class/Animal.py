class Animal(object):
    def __init__(self, name = '姓名'):
        self.name = name
    def speak(self):
        return self.name
        
class Cat(Animal):
    def speak(self):
        return '{}: 喵喵喵'.format(self.name)

class Dog(Animal):
    def speak(self):
        return '{}: 汪汪汪'.format(self.name)

class Person(Animal):
    def speak(self):
        return '{}:你好'.format(self.name)

leo = Cat('Leo')
print(leo.speak())
shango = Dog('Shango')
print(shango.speak())
pan = Person('Pan')
print(pan.speak())
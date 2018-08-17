class Person(object):
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age 

    def __repr__(self):
        return '{}的年龄为{}'.format(self.name, self.age)

class Male(Person):
  def __repr__(self):
    return '他叫{}, 他的年龄为{}'.format(self.name, self.age)
 
class Female(Person):
  def __repr__(self):
    return '她叫{}, 她的年龄为{}'.format(self.name, self.age)

leo = Male('Leo')
diana = Female('Diana', 7)
print(leo, diana)
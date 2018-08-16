class Vehicle:
    def __init__(self,name,engine):
        self.__name = name
        self.__engine = engine

    def getName(self):
        return self.__name

    def getEngine(self):
        return self.__engine

    def setEngine(self,engine):
        self.__engine = engine

class Car(Vehicle):
    def __inti__(self,name,engine,electric):
        super().__init__(name,engine)
        self.__electric = electric

    def getCarName(self):
        print("Name" + self.getName())
        print("Engine" + self.getEngine())
        print("electric" + self.__electric())

    def getAuto(self):
        print("auto mobile")

myCar = Car("Tesla","Engine","Power")
myCar.getCarName()
print(myCar,getAuto())

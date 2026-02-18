class Vehicle:
    #Make:String
    #Model:String
    def __init__(self,make,model):
        self.__Make=make
        self.__Model=model
    def display_info(self):
        print("The make of vehicle is", self.__Make)
        print("The model is",self.__Model)
class Car(Vehicle):
    #Mileage:INTEGER
    def __init__(self,make,model):
        super().__init__(make,model)
        self.__Mileage=0
    def SetMileage(self):
        self.__Mileage=int(input("Enter the mileage of the car: "))
    def display_info(self):
       super().display_info()
       print("The milleage of vehicle is", self.__Mileage)
       
    
vechicle=Vehicle("Nissan","Q")
vechicle.display_info
Car=Car("Nissan","Q")
Car.display_info()

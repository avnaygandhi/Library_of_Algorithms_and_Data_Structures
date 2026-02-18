class person:
    #Name:String
    #Age:INTERGER
    def __init__(self,n):
        self.__Name=n
        self.__Age=0
    def GetName(self):
        print(self.__name)
    def GetAge(self):
        print(self.__age)
    def SetName(self):
        self.Name=input("Enter the name: ")
        print(self.__name)
    def SetAge(self):
        self.age=int(input("Enter your age: "))
        print(self.__age)

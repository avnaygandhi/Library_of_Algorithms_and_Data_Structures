class UniversityMember:
    #ID:STRING
    #Name:STRING
    def __init__(self,ID,name):
        self.__ID=ID
        self.__Name=name
    def GetDetails(self):
        print("ID: ",self.__ID)
        print("name: ",self.__Name)
class Student(UniversityMember):
    def __init__(self,ID,name,m):
        super().__init__(ID,name)
        self.__Major=m
    def GetDetails(self):
        super().GetDetails()
        print("The major is: ",self.__Major)
class Professor(UniversityMember):
    def __init__(self,ID,name,d):
        super().__init__(ID,name)
        self.__Department=d
    def GetDetails(self):
        super().GetDetails()
        print("The department they work in is:",self.__Department)
Student1=Student("1","Avnay","AI")
Student1.GetDetails()

Student1=Professor("1","DR Kappor","Computer science")
Student1.GetDetails()

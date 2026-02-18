class Person:
    def __init__(self,n,a):
        self.__Name=n
        self.__Age=a
    def GetName(self):
        print("The name is",self.__Name)
    def GetAge(self):
        print("The age is ",self.__age)
    def SetAge(self):
        self.__age=int(input("Enter the new age:"))
        print("the new age",self.__age)
class Student(Person):
    def __init__(self,n,a,ID):
        super().__init__(n,a)
        self.__StudentID=ID
    def GetStudentID(self):
        print("Student ID =",self.__StudentID)
        
Student1=Student("Avnay","17",1)
Student1.GetStudentID()
Student1.GetName()
Student1.SetAge()

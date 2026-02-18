class Deparament:
    def __init__(self,DID,Name):
        self.__deptID=DID
        self.__name=Name
        self.__teachers=[]

    def GetID(self):
        print("The id:",self.__deptID)
    def GetName(self):
        print("The name is",self.__deptID)
    def SetTeacher(self,teacher):
        self.__teachers.append(teacher)
    def printTeacher(self):
        for i in range(len(self.__teachers)):
            print(self.__teachers[i].printTeacherdetail())

    def HighestPaidTeacher(self):
        HighestSalary=0
        HighestName=None
        for y in range(len(self.__teachers)):
           if self.__teachers[y].GetSalary()>HighestSalary:
               HighestSalary=self.__teachers[y].GetSalary()


        return HighestSalary
           

class teacher:
    def __init__(self,name,subject,salary):
        self.__TeacherID=0
        self.__Name=name
        self.__Subjet=subject
        self.__Salary=salary
        
    def GetTeacherID(self):
        return self.__TeacherID
    def GetName(self):
        return self.__Name
    def GetSubject(self):
        return self.__Subjet

    def GetSalary(self):
        return self.__Salary

    def SetSubject(self):
        self.__Subjet=input("Enter the new subject: ")

    def SetSalary(self):
        self.__Salary=input("Enter the new salary: ")

    def printTeacherdetail(self):
        print(self.__TeacherID)
        print(self.__Name)
        print(self.__Subjet)
    
        
D1=Deparament(1,"Math")
t1=teacher("ko","Math",2000)
t2=teacher("Cum","Math",2500)
D1.SetTeacher(t1)
D1.SetTeacher(t2)
D1.printTeacher()
D2=Deparament(2,"CS")
t3=teacher("Jam","CS",5000)
D2.SetTeacher(t3)
t4=teacher("Harper","CS",2000)
D2.SetTeacher(t4)

print("Highest salary in D1 is", D1.HighestPaidTeacher())

def highestpayperson():
    HighestPaidTeacherInSchool=D1.HighestPaidTeacher()
    if D2.HighestPaidTeacher()>HighestPaidTeacherInSchool:
        HighestPaidTeacherInSchool=D2.HighestPaidTeacher()
    print("HighestPaidTeacherInSchool is", HighestPaidTeacherInSchool)

highestpayperson()
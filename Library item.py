from datetime import *
class LibaryItem:
    def __init__(self,t,a,i):
        self.__Title=t
        self.__Author_Artist=a
        self.__ItemID=i
        self.__OnLoan=False
        self.__DueDate = datetime.today()
        
    def GetTitle(self):
        print(self.__Title)
        
    def GetAuthor_Artist(self):
        print(self.__Author_Artist)

    def GetItemID(self):
        print(self.__ItemID)
        
    def GetOnLoan(self):
        print(self.__OnLoan)

    def Borrowing(self):
        self.OnLoan=True
        self.__DueDate=+datatime.timedelta(week=3)

    def Returning(self):
        self.OnLoan=False

    def PrintDetail(self):
        print(self.__Title, self.__Author_Artist,self.__ItemID,self.__OnLoan,self.__DueDate)

class Book(LibaryItem):
    def __init__(self,t,a,i):
        super().__init__(t,a,i)
        self.__IsRequested=False
        
    def getIsRequested(self):
        print(self.__IsRequested)

    def SetIsRequested(self):
        self.__IsRequested=True
        print(self.__IsRequested)

class CD(LibaryItem):
    def __init__(self,t,a,i):
        super().__init__(self)
        self.__Genre=""

    def getGenre(self):
        print(self.__Genre)

    def setGenre(self):
        self.__Genre=input("enter the new genre:")
        print(self.__Genre)


Book1=Book("Cs textbook","Sylvia Langfield",1)

print(Book1.PrintDetail())
        

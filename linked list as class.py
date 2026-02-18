class Node():
    def __init__(self,Maxsize):
        self.__MaxSize=Maxsize
        self.__Data=[""]*Maxsize
        self.__Pointer=[-1]*Maxsize
        self.__FreeListPointer=0
        self.__StartPointer=-1
    def instance(self):
        self.__StartPointer=-1
        self.__FreeListPointer=0
        for index in range(self.__MaxSize - 1):
            self.__Pointer[index]=index + 1
        self.__Pointer[self.__MaxSize-1]=-1 
    def Insert(self,NewItem):
        if self.__FreeListPointer==-1:
            return ("No empty node")

        NewPointer=self.__FreeListPointer
        self.__FreeListPointer=self.__Pointer[self.__FreeListPointer]
        self.__Data[NewPointer]=NewItem

        if self.__StartPointer == -1 or self.__Data[self.__StartPointer] >= NewItem:
            self.__Pointer[NewPointer] = self.__StartPointer
            self.__StartPointer = NewPointer
            return
        CurrentPointer = self.__StartPointer
        while (self.__Pointer[CurrentPointer] != -1 and self.__Data[self.__Pointer[CurrentPointer]] < NewItem):
            CurrentPointer = self.__Pointer[CurrentPointer]
        self.__Pointer[NewPointer] = self.__Pointer[CurrentPointer]
        self.__Pointer[CurrentPointer] = NewPointer

    def Delete(self):
        if self.__StartPointer==-1:
            print("Underflow error")
        CurrentPointer=self.__StartPointer
        self.__StartPointer=self.__Pointer[self.__StartPointer]

        self.__Pointer[CurrentPointer]=self.__FreeListPointer
        self.__FreeListPointer=CurrentPointer
    def traverse(self):
        CurrentPointer=self.__StartPointer
        result=[]
        while CurrentPointer!=-1:
            result.append(self.__Data[CurrentPointer])
            CurrentPointer=self.__Pointer[CurrentPointer]
        return result
        
        
node1=Node(5)
node1.instance()
node1.Insert(2)
node1.Insert(50)
node1.Insert(80)
node1.Delete()
print(node1.traverse())



class node():
    def __init__(self,data,pointer):
        self.__Data=data
        self.__Next=pointer

class linkedlist():
    def __init__(self,StartPointer,Size):
        self.__StartPointer=StartPointer
        self.__size=Size

    def Add(self,Value):
        New_Node=Node(Value,self.__StartPointer)
        self.__Root=New_Node
        Self.__Size+=1

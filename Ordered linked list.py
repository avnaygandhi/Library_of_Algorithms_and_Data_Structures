class Node:
    def __init__(self,Data):
        self.__data=Data
        self.__next=None
        self.__head=None
    def Add(self,Data):
        NewNode=Node(Data)
        if  self.__head==None or Data<self.__Head.__Data:
            NewNode.__next=self.__head
            self.__head=NewNode
            return
        current=self.__head
        while current.__next!=None and current.__next.__data<Data:
            current=current.__next
        NewNode.__next=current.__next
        current.__next=NewNode
InitialList=Node(["C","J","L","P"])
print(InitialList)
print(InitialList.Add("A"))

      

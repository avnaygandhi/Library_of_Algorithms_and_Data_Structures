class StackViaLinkedList:
    def __init__(self)->None:
        self.__Top:int=-1
        self.__LinkedList:list=[]
    def push(self,x:int)->None:
        self.__LinkedList.append(x)
        self.__Top+=1
    def pop(self)->None:
        self.__Top-=1
    def __str__(self):
        return str(self.__LinkedList[:-1])
    
SVLL=StackViaLinkedList()
SVLL.push(5)
SVLL.push(10)
SVLL.push(15)
SVLL.pop()
print("Stack",SVLL)

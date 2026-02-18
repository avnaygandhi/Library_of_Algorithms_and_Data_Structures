class Queue:
    def __init__(self,Max):
        self.__MaxSize=Max
        self.__Data=[]
        self.__Head=-1
        self.__Tail=-1
    def EnQueue(self,ElementToAdd):
        if (self.__Head==0 and self.Tail==self.__MaxSize) or self.__Head==self.__Tail-1:
            print("Overflow error")
        elif self.__Tail==-1:
            Head=0
            Tail=0
        elif self.__Tail==self.__MaxSize:
            self.__Tail=0
        else:
            self.__Tail+=1
        self.__Data.append(ElementToAdd)

    def DeQueue(self):
        if self.__Head==self.__Tail:
            self.__Head=1
        elif Head==MaxSize:
            self.__Head=1
        else:
            self.__Head+=1

    def Isempty(self):
        if self.__Head==-1 and self.__Tail==-1:
            return True
        else:
            return False

Queue1=Queue(5)
Queue1.EnQueue(20)
Queue1.EnQueue(40)
Queue1.DeQueue()
print(Queue1.Isempty())

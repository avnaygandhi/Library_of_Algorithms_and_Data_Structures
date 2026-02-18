class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Next=-1

class Queue:
    def __init__(self,MaxSize):
        self.Data=[]
        self.Head=0
        self.MaxSize=MaxSize
        self.Tail=-1

    def enqueue(self,elementtoadd):
        NewNode=Node(elementtoadd)
        if (self.Head==0 and self.Tail==self.MaxSize) or (self.Head==self.Tail-1):
            print("Overflow error")

        elif self.Tail==-1:
            Head=0
            Tail=0
        elif self.Tail==self.MaxSize:
            self.Tail=0
        else:
            self.Tail+=1
        self.Data.append(NewNode)

    
    def Dequeue(self):
        if self.Head==self.Tail:
            self.Head=1
        elif self.Head==self.MaxSize:
            self.head=1
        else:
            self.Head+=1

    def Isempty(self):
        if self.Head==-1 and self.Tail==-1:
            return True
        else:
            return False


Queue1=Queue(5)
Queue1.enqueue(2)
Queue1.enqueue(4)
Queue1.enqueue(52)
Queue1.Dequeue()
print("Is the queue empty?",Queue1.Isempty())



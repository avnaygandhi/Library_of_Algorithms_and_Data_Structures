class QueueViaStack:
    def __init__(self):
        self.Stack1:list=[]
        self.Stack2:list=[]
    def Enqueue(self,x):
        self.Stack1.append(x)
    def Dequeue(self):
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        if not self.Stack2:
            return None
        return self.Stack2.pop()

    def __str__(self):
        return str(self.Stack2[:-1]+self.Stack1)
QVS=QueueViaStack()
QVS.Enqueue(1)
QVS.Enqueue(2)
QVS.Enqueue(3)
QVS.Dequeue()
QVS.Enqueue(4)
print("Queue",QVS)

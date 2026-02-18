class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Left=None
        self.Right=None
    def InOrder(self):
        if self.Left:
            self.Left.InOrder()
        print(self.Data,end=" ")
        if self.Right:
            self.Right.InOrder()
        
    def PreOrder(self):
        #Simply print Root<-Left<-Right
        print(self.Data,end=" ")
        if self.Left:
            self.Left.PreOrder()
        if self.Right:
            self.Right.PreOrder()
    def PostOrder(self):
        if self.Left:
            self.Left.PostOrder()
        if self.Right:
            self.Right.PostOrder()
        print(self.Data,end=" ")

Root=Node(20)
Root.Left=Node(10)
Root.Right=Node(30)
Root.Left.Left=Node(5)
Root.Left.Right=Node(15)
Root.Right.Left=Node(25)
Root.Right.Right=Node(35)

print("In order tranversal")
Root.InOrder()

print("\n Pre order tranversal")
Root.PreOrder()

print("\n Post Order transversal")
Root.PostOrder()

class Node:
    def __init__(self, data):
        self.Data = data
        self.Next = -1

class Stack:
    def __init__(self, MaxSize):
        self.__data = []
        self.top = 0
        self.__MaxSize = MaxSize
        
    def Push(self, elementToAdd):
        if len(self.__data) >= self.__MaxSize:
            print("Overflow error")
        else:
            self.__data.append(elementToAdd)
            self.top += 1
    
    def Pop(self):
        if len(self.__data) == 0:
            print("Underflow error")
            return None
        else:
            self.top -= 1
            return self.__data.pop()
    
    def Isempty(self):
        if self.top==-1:
            return True
        else:
            return False

# Example usage
Stack1 = Stack(2)
x = Node("Avnay")
y=Node("Computer")
z=Node("Sceince")
Stack1.Push(x)
Stack1.Push(y)
Stack1.Push(y)
Stack1.Pop()
print("Is the stack empty",Stack1.Isempty())







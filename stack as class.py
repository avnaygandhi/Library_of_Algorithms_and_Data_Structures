#
class Stack:
    def __init__(self,MaxSize):
        self.__data=[]
        self.__top=0
        self.__MaxSize=MaxSize
    def Push(self,elementToAdd):
        if len(self.__data)>self.__MaxSize:
            print("Overflow error")
        else:
            self.__data.append(elementToAdd)
            self.__top+=1
    def Pop(self):
        if len(self.__data)==0:
            print("Underflow error")
        else:
            self.__top-=1
    def Isempty(self):
        if len(self.__data)==0:
            return True
        else:
            return False
    def Peek(self):
        if len(self.__data)==0:
            print("invaild")
        print("The top value is:",self.__data[self.__top])

Stack1=Stack(2)
Stack1.Push(2)
Stack1.Pop()
print(Stack1.Isempty())
Stack1.Peek()

Data=[]
Top=0
MaxSize=int(input("Enter the size of stack:"))

    
    
def Push(elementToAdd):
    global Top
    if len(Data)>MaxSize:
        print("Overflow error")
    Data.append(elementToAdd)
    Top=Top+1
    
def Pop():
    global Top
    if len(Data)==0:
        print("Underflow error")
    else:
        Top-=1
def Isempty():
    global Top
    if len(Data)==0:
        return True
    else:
        return False
def Peek():
    global Top
    if len(Data)==0:
        print("invaild")
    print("The top value is:",Data[Top])

Push(2)
print(Data)
Pop()
print(Isempty())
Push(5)
Peek()

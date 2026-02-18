Data=[]
Head=-1
Tail=-1
MaxSize=2
def Enqueue(ElementToAdd):
    global Head,Tail,MaxSize
    if (Head==0 and Tail==MaxSize) or Head==Tail-1:
        print("Overflow error")
    elif Tail==-1:
        Head=0
        Tail=0
    elif Tail==MaxSize:
        Tail=0
    else:
        Tail=Tail+1
    Data.append(ElementToAdd)

def Dequeue():
    global Head,Tail
    if Head==Tail:
        Head=0
        Tail=0
    elif Head==MaxSize:
        Head=1
    else:
        Head+=1
            
def Isempty():
    global Head,Tail
    if Head==-1 and Tail==-1:
        return True
    else:
        return False
Enqueue(20)
Enqueue(220)
print (Data)
Dequeue()
print (Data)
Isempty()

        

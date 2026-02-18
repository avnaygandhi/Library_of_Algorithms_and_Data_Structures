NullPointer = -1
MaxSize = 5

Data = [""] * MaxSize
Pointer = [NullPointer] * MaxSize

global StartPointer, FreeListPointer
StartPointer = NullPointer
FreeListPointer = 0


Pointer=[i+1 for i in range(MaxSize)]
Pointer[MaxSize-1]=NullPointer


def Insert(NewItem):
    global StartPointer, FreeListPointer

    if FreeListPointer == NullPointer:
        return("No empty node")
        

    
    NewPointer = FreeListPointer
    FreeListPointer = Pointer[FreeListPointer]
    Data[NewPointer] = NewItem

   
    if StartPointer == NullPointer or Data[StartPointer] >= NewItem:
        Pointer[NewPointer] = StartPointer
        StartPointer = NewPointer
        return Data

    
    CurrentPointer = StartPointer
    while (Pointer[CurrentPointer] != NullPointer and Data[Pointer[CurrentPointer]] < NewItem):
        CurrentPointer = Pointer[CurrentPointer]

    Pointer[NewPointer] = Pointer[CurrentPointer]
    Pointer[CurrentPointer] = NewPointer
    return Data


def Delete():
    global StartPointer, FreeListPointer

    if StartPointer == NullPointer:
        return ("underflow error")
        

   
    CurrentPointer = StartPointer
    StartPointer = Pointer[StartPointer]

    
    Pointer[CurrentPointer] = FreeListPointer
    FreeListPointer = CurrentPointer

def traverse():
    Result=[]
    CurrentPointer=StartPointer
    while CurrentPointer!=0:
        Result.append(Data[CurrentPointer])
        CurrentPointer=Pointer[CurrentPointer]
    return Result

def RevseringLinkedList():
    global StartPointer
    CurrentPointer=StartPointer
    PreviousPointer=None
    while CurrentPointer==-1:
        next_node = current.next  
        current.next = prev       
        prev = current            
        current = next_node       
    return prev    
print(Insert(2))
print(Insert(3))
print(Delete())
print(traverse())
print(RevseringLinkedList())



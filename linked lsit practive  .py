#Data:ARRAY[1:9][1:2] Of INTEGER
Array=[[0 for i in range(2)]for y in range(9)]
StartPointer=0
FreeListPointer=1
def InsertData(NewData,NewPointer):
    if StartPointer==-1:
        print("No empty node")
    TempData=Array[StartPointer][0]
    TempPointer=Array[StartPointer][1]
    Array[StartPointer][0]=NewData
    Array[StartPointer+1][0]=TempData
    Array[StartPointer][1]=NewPointer
    Array[StartPointer+1][1]=TempPointer

def OutputLinkedList():
    for i in range(9):
        return Array[i][0]
    

def RemoveData(Value):
    global StartPointer, FreeListPointer
    Current = StartPointer
    Previous = -1
    
    while Current != -1:
        if Array[Current][0] == Value:
            if Previous == -1:
                StartPointer = Array[Current][1]
            else:
                Array[Previous][1] = Array[Current][1]
            
            # Add removed node back to free list
            Array[Current][0] = 0
            Array[Current][1] = FreeListPointer
            FreeListPointer = Current
            return
        Previous = Current
        Current = Array[Current][1]
    
    print("Value not found")

def OutputResverseLinkedList():
    for i in range(8,0,-1):
        return Array[i][0]
        
InsertData(5,2)
InsertData(10,1)
InsertData(15,-1)
print(OutputLinkedList())
print(RemoveData(5))
print(OutputResverseLinkedList())


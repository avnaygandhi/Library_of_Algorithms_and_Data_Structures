#Data:String
#Left,Right:INTEGER
Data=["" for i in range(5)]
Left=[-1 for i in range(5)]
Right=[-1 for i in range(5)]
RootPointer=-1
FreePointer=0
for index in range(3):
    Left[index]=index+1
Left[4]=-1

def insert(NewData):
    global RootPointer,FreePointer
    if FreePointer==-1:
        print("Tree is full")
    else:
        NewNodePointer=FreePointer
        FreePointer=Left[FreePointer]
        Data[NewNodePointer]=NewData
        Left[NewNodePointer]=-1
        Right[NewNodePointer]=-1
        if RootPointer==-1:
            RootPointer=NewNodePointer
            
        else:
            CurrentPointer=RootPointer
            while CurrentPointer!=-1:
                PreviousPointer=CurrentPointer
                if NewData>Data[CurrentPointer]:
                    CurrentPointer=Right[CurrentPointer]
                else:
                    CurrentPointer=Left[CurrentPointer]

            if NewData<Data[PreviousPointer]:
               Left[PrevousPointer]=NewNodePointer
            else:
                Right[PreviousPointer]=NewNodePointer
                    
def Search(SearchValue):
    if RootPointer==-1:
        print("The binary tree is empty so element not found")
    else:
        CurrentPointer=RootPointer
        while CurrentPointer!=-1:
            if Data[CurrentPointer]>SearchValue:
                CurrentPointer=Right[CurrentPointer]
            elif Data[CurrentPointer]==SearchValue:
                print(SearchValue,"Found at index",CurrentPointer)
                return
            else:
               CurrentPointer=Left[CurrentPointer]

print(Search(5))


insert(1)
insert(5)
insert(8)
for index in range(len(Data)):
    print("Data: ",Data[index])

print(Search(1))



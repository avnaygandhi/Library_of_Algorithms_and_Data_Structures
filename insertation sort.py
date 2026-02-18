import random
Data=[random.randint(0,100) for i in range(10)]
print(Data)

def insertationSort(Data):
    for i in range(1,len(Data)):
        current=Data[i]
        postion=i
        while postion>0 and current<Data[postion-1]:
            Data[postion]=Data[postion-1]
            postion-=1
        Data[postion]=current
    return Data
print(insertationSort(Data))

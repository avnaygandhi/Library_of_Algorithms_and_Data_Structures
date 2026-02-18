import random
Data=[random.randint(0,100)for i in range(10)]
def Bubble_sort(Data):
    for i in range(len(Data)-1):
        for j in range(len(Data)-1-i):
            if Data[j]>Data[j+1]:
                Data[j],Data[j+1]=Data[j+1],Data[j]

    return Data


def BinarySearch(Data, SearchValue):
    LB=0
    UB=len(Data)
    Mid=int((LB+UB)/2)
    found=False
    while found==False and UB>LB:
        Mid=int((LB+UB)/2)
        if Data[Mid]>SearchValue:
            LB=Mid+1
        elif Data[Mid]<SearchValue:
            UB=Mid-1
        else:
            found=True
            print("Value found at index",Mid)
    

print("Sorted list: ", Bubble_sort(Data))
SearchValue=int(input("Enter a search value"))
print(BinarySearch(Bubble_sort(Data), SearchValue))

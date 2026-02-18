def Bubble_sort(Data):
    for i in range(len(Data)-1):
        for j in range(len(Data)-1-i):
            if Data[j]>Data[j+1]:
                Data[j],Data[j+1]=Data[j+1],Data[j]

    return Data
import random
Data=[random.randint(0,100)for i in range(10)]
print("Unsorted list:", Data)
print("Sorted list: ", Bubble_sort(Data))
    

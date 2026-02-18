import random
Data=[random.randint(0,100)for count in range(10)]
print("Unsorted data: ", Data)
for count in range(len(Data)-1):
    if Data[count]>Data[count+1]:
        Data[count],Data[count+1]=Data[count+1],Data[count]
print("Sorted data: ",Data)

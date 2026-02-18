import random
Data=[random.randint(0,100) for i in range(10)]
print(Data)
SearchValue=int(input("Enter the value to search for: "))
for index in range(len(Data)):
    if Data[index]==SearchValue:
        print(f"the {SearchValue} was found at {index}")
    

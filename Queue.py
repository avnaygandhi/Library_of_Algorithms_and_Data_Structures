#Decalre FrontOfQueuePointer,EndOfQueuePointer:Integer
#Declare List:Array[0:5] OF Integer
import random
FrontOfQueuePointer=0
EndOfQueuePointer=5

List=[random.randint(0,100) for num in range(5)]
print(List)

def EnQueue():
    NumToEnqueue=int(input("Enter the number to enqueue: "))
    EndOfQueuePointer=+1
    List.append(NumToEnqueue)
    print(List)

def DeQueue():
    List.pop(FrontOfQueuePointer)
    print(List)

choice=input("Do you want to add or remove? ")
if choice.title()=="Add":
    EnQueue()
elif choice.title()=="Remove":
    DeQueue()
else:
    print("Invalid choice")
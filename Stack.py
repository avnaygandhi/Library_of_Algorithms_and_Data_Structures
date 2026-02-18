Data = []

def AddData():
    Index = int(input("Enter the number of elements you want to insert: "))
    for count in range(Index):
        Data.append(int(input("Enter the number to insert: ")))
    print("Initial Data:", Data)

def push():
    DataToAdd = int(input("Enter the number to add (push): "))
    Data.append(DataToAdd)
    print("After push:", Data)

def pop():
    if len(Data) == 0:
        print("Stack is empty. Nothing to pop.")
    else:
        removed = Data.pop()  # Actually removes the last element
        print(f"Popped value: {removed}")
        print("After pop:", Data)

def main():
    AddData()
    Choice = input("Enter the operation you want to perform (push/pop): ").lower()
    if Choice == "push":
        push()
    elif Choice == "pop":
        pop()
    else:
        print("Invalid choice")

main()

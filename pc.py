class Components:
    def __init__(self,MN,Price):
        self.ModelName=MN
        self.Price=Price

class CPU(Components):
    def __init__(self,MN,Price,CC):
        super(). __init__(MN,Price)
        self.CoreCount=CC
class GPU(Components):
    def __init__(self,MN,Price,RAMSize):
        super(). __init__(MN,Price)
        self.VramSizeGB=RAMSize
class RAM(Components):
     def __init__(self,MN,Price,Capicity):
        super(). __init__(MN,Price)
        self.CapacityGB =Capicity

def GetTotalPrice() :
   total=CPU.Price+GPU.Price+RAM.Price
   return total


CPU("i",20,2)
GPU("o",10,200)
RAM("v",20,200)

print(GetTotalPrice())

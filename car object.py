class car:
    #BandName,OwnerName:String
    #PurchasePrice,WheelSize:Interger
    def __init__(self):
        self.__BrandName=""
        self.__WheelSize=0
        self.__PurchasePrice=0
        self.OwnerName=""
    def GetBrandName(self,B):
         self.__BrandName=B
        
    def GetWheelSize(self,WS):
        self.__WheelSize=WS

    def GetPurchasePrice(self,Price):
        self.__PurchasePrice=Price

    def GetOwnerName(self,Name):
        self.__OwnerName=Name

    def SetOwnerName(self,UpdateName):
        self.__OwnerName=UpdateName
    
    def DisplayDetail(self):
        print("The car brand name is ",self.__BrandName)
        print("The car wheel size is ",self.__WheelSize)
        print("The car was purchase at",self.__PurchasePrice)
        print("The ownner is",self.__OwnerName)


Car1=car()
Car1.GetBrandName("Nis")
Car1.GetWheelSize(2)
Car1.GetPurchasePrice(2000)
Car1.GetOwnerName("ni")
Car1.DisplayDetail()


Car1.SetOwnerName("Wi")
Car1.DisplayDetail()

class BankAccount:
    def __init__(self,AN,AHN):
        self.__AccountNumber=AN
        self.__AccountHolderName=AHN
        self.__AccountBalance=0

    def GetAcountNumber(self):
        print(f"Account number: {self.AccountNumber}")
        
    def GetAccountHolderName(self):
        print("The account is ownned by",self.__AccountHolderName)

    def GetAccountBalance(self):
        print("The account balance is",self.__AccountBalance)

    def SetAccountBalance(self):
        self.__AccountBalance=int(input("Enter the amount you have: "))

BankAccountDetail1=BankAccount(112101,"Av")
BankAccountDetail1.GetAcountNumber
BankAccountDetail1.GetAccountHolderName
BankAccountDetail1.SetAccountBalance
BankAccountDetail1.GetAccountBalance

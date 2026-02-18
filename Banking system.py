class StandardBankAccount:
    def __init__(self,AN,OdL,Balance):
        self.__Balance=Balance
        self.__AccountNumber=AN
        self.__OverdraftLimit=ODL
    def withdraw(self):
        if balance<__OverdraftLimit:
            print("Not possible")
        else:
           self.__Balance =self.__Balance-withdrawal

class SavingAcount(StandardBankAccount):
    def __init__(self,AN,OdL,Balance,IR):
        super().__init__(AN,OdL,Balance)
        self.__interestRate=IR
        self.__OverdraftLimit=0
    def applyInterest(self):
        self.__Balance=self.__Balance+self.__interestRate

class PremiumAccount(SavingAcount):
    def __init__(self,AN,OdL,Balance,MB):
        super().__init__(AN,OdL,Balance)
        self.__MinimumBalance=MB

    def withdraw(self):
        if self.__Balance<self.__MinimumBalance:
            self.__Balance=-35

    

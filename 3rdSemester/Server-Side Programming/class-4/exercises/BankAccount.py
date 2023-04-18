class BankAccount:
    def __init__(self, acc_number, acc_owner, acc_balance):
        self.acc_number = acc_number;
        self.acc_owner = acc_owner;
        self.acc_balance = acc_balance;
        
    def changeOwner(self, newOwner):
        self.acc_owner = newOwner;
        
    
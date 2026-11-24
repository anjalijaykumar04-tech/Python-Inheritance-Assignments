class Bank:
    def bank_name(self):
        print("Bank Name: SBI")

class SBI(Bank):
    def interest_rate(self):
        print("Interest Rate: 7%")

s = SBI()
s.bank_name()
s.interest_rate()
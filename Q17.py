class Bank:
    def interest_rate(self):
        print("General interest rate")

class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate is 7%")

class HDFC(Bank):
    def interest_rate(self):
        print("HDFC interest rate is 7.5%")

s = SBI()
h = HDFC()

s.interest_rate()
h.interest_rate()
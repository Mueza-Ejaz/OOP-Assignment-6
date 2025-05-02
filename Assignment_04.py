# Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    bank_name = "Bank Al-Habib"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank_1 = Bank()
print("Initial Bank Name:", bank_1.bank_name) # Initial Bank Name: Bank Al-Habib

bank_1.change_bank_name("Meezan Bank")
print("After changing the initial bank:", bank_1.bank_name) # After changing the initial bank: Meezan Bank






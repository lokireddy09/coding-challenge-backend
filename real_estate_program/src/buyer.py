from .loan import Loan
from .property import Property


class Buyer:
    def __init__(self, income, sqft, bedrooms, bathrooms):
        self.loan = Loan(income)
        self.requirements = Property(None, sqft, bedrooms, bathrooms)

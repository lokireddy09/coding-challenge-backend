import random
from .buyer import Buyer
from .property import Property

class RealEstateProgram:
    def __init__(self):
        self.buyer = None
        self.properties = []

    def gather_income_data(self):
        income = float(input("Enter your annual income: "))
        self.buyer = Buyer(income, None, None, None)

    def generate_house_listings(self):
        for _ in range(random.randint(2, 12)):
            price = random.randint(50000, int(self.buyer.loan.max_loan))
            square_footage = random.randint(250, int(price * 0.0125))
            bedrooms = random.randint(1, int(square_footage / 400))
            bathrooms = random.randint(1, bedrooms)
            self.properties.append(Property(price, square_footage, bedrooms, bathrooms))

    def purchase_property(self):
        for i, property in enumerate(self.properties):
            print(f"{i+1}. Price: {property.price}, Square footage: {property.square_footage}, Bedrooms: {property.bedrooms}, Bathrooms: {property.bathrooms}")
        choice = int(input("Choose a property to purchase (enter number): "))
        return self.properties[choice-1]

    def generate_bill_breakdown(self, property):
        monthly_payment = self.buyer.loan.max_loan / (30 * 12)
        print(f"Total monthly payment: {monthly_payment}")
        print(f"Amount being applied to balance each month: {monthly_payment * 0.5}")
        print(f"Amount of interest paid each month: {monthly_payment * 0.3}")
        print(f"Amount of taxes & insurance paid each month: {monthly_payment * 0.2}")

    def run(self):
        self.gather_income_data()
        self.generate_house_listings()
        property = self.purchase_property()
        self.generate_bill_breakdown(property)

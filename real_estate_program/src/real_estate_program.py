import random
from .buyer import Buyer
from .property import Property
# from src.config import MAX_LOAN_AMOUNT


class RealEstateProgram:
    def __init__(self):
        self.buyer = None
        self.properties = []

    # def calculate_min_income_limit(self):
    #     return MAX_LOAN_AMOUNT * (3/12)

    def gather_income_data(self):
        try:
            income = float(input("Enter your annual income: "))
        except Exception:
            raise Exception('Ensure to enter int or float values only')
        if income < 0:
            raise Exception("Invalid input. Ensure to give positive numbers")
        # if income < self.calculate_min_income_limit():
        #     raise Exception("YOu are not eligible for loan")
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
            print(f"{i+1}. Price: {property.price}, "
                  f"Square footage: {property.square_footage}, "
                  f"Bedrooms: {property.bedrooms}, Bathrooms: {property.bathrooms}")
        choice = int(input("Choose a property to purchase (enter number): "))
        if 0 <= choice > len(self.properties) -1:
            raise Exception("Invalid option choosen")
        return self.properties[choice-1]

    def generate_bill_breakdown(self):
        monthly_payment = self.buyer.loan.max_loan / (30 * 12)
        print(f"Total monthly payment                       : {monthly_payment}")
        print(f"Amount being applied to balance each month  : {monthly_payment * 0.5}")
        print(f"Amount of interest paid each month          : {monthly_payment * 0.3}")
        print(f"Amount of taxes & insurance paid each month : {monthly_payment * 0.2}")

    def run(self):
        try:
            self.gather_income_data()
            self.generate_house_listings()
            property = self.purchase_property()
            self.generate_bill_breakdown(property)
        except Exception as ex:
            print(ex)

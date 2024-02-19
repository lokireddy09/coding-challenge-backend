from src.config import MAX_LOAN_AMOUNT, LOAN_AMOUNT_PERCENTAGE


class Loan:
    def __init__(self, income):
        self.income = income
        self.max_loan = self.calculate_max_loan()

    def calculate_max_loan(self):
        monthly_income = self.income / 12
        max_monthly_payment = monthly_income / 3
        loan_amount = (max_monthly_payment * LOAN_AMOUNT_PERCENTAGE) * 12 * 30
        if loan_amount < MAX_LOAN_AMOUNT:
            raise Exception("YOu are not eligible for loan")
        return loan_amount

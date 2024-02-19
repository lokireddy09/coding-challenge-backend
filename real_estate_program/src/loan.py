class Loan:
    def __init__(self, income):
        self.income = income
        self.max_loan = self.calculate_max_loan()

    def calculate_max_loan(self):
        monthly_income = self.income / 12
        max_monthly_payment = monthly_income / 3
        loan_amount = (max_monthly_payment * 0.5) * 12 * 30
        return max(loan_amount, 50000)

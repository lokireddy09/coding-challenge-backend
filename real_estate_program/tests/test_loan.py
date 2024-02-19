from src.loan import Loan


def test_loan_init():
    loan = Loan(120000)
    assert loan.income == 120000


def test_calculate_max_loan():
    loan = Loan(120000)
    assert loan.calculate_max_loan() == 600000  # Assuming the calculation is correct

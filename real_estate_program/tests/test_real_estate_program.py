from unittest.mock import patch
from src.real_estate_program import RealEstateProgram
from src.buyer import Buyer


@patch('builtins.input', return_value='120000')
def test_gather_income_data(mock_input):
    program = RealEstateProgram()
    program.gather_income_data()
    assert program.buyer.loan.income == 120000


def test_generate_house_listings():
    program = RealEstateProgram()
    program.buyer = Buyer(120000, 2000, 3, 2)
    program.generate_house_listings()
    assert len(program.properties) >= 2
    assert len(program.properties) <= 12


@patch('builtins.input', return_value='1')
def test_purchase_property(mock_input):
    program = RealEstateProgram()
    program.buyer = Buyer(120000, 2000, 3, 2)
    program.generate_house_listings()
    property = program.purchase_property()
    assert property == program.properties[0]

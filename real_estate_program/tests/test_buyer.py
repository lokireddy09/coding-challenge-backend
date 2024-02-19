from src.buyer import Buyer


def test_buyer_init():
    buyer = Buyer(120000, 2000, 3, 2)
    assert buyer.loan.income == 120000
    assert buyer.requirements.square_footage == 2000
    assert buyer.requirements.bedrooms == 3
    assert buyer.requirements.bathrooms == 2

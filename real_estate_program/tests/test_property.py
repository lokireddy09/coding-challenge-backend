from src.property import Property

def test_property_init():
    property = Property(100000, 2000, 3, 2)
    assert property.price == 100000
    assert property.square_footage == 2000
    assert property.bedrooms == 3
    assert property.bathrooms == 2

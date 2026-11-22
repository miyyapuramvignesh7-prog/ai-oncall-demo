from app import calculate_average

def test_calculate_average():
    assert calculate_average(100, 4) == 25.0
    assert calculate_average(100, 0) == 0.0

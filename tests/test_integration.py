from quick_calc.calc import add, mul, div, clear

def test_integration_sequence_add_then_mul():
    result = add(5, 3)      # 8
    result = mul(result, 2) # 16
    assert result == 16

def test_integration_div_then_clear():
    result = div(9, 3)      # 3
    assert result == 3
    assert clear() == 0
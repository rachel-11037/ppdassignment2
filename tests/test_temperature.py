# Adam Heavey - Test File: Temperature

from PythonFiles.temperature import Temperature

# Test to convert celsius to fahrenheit
def test_convert_cel2far():
    number = Temperature(25)
    result = number.convert_cel2far()
    assert result == float((number.temp*9/5) + 32)

# Test tp convert fahrenheit to celsius
def test_convert_far2cel():
    number = Temperature(80)
    result = number.convert_far2cel()
    assert result == float((number.temp - 32)*5/9)

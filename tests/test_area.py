# Adam Heavey - Test File: Area

from PythonFiles.area import Area

# Test to convert acres to hectares
def test_convert_acr_to_hect():
    number = Area(20)
    result = number.convert_acr_to_hect()
    assert result == round((number.area / 2.471), 2)

# Test to convert acres to hectares
def test_convert_hect_to_acr():
    number = Area(10)
    result = number.convert_hect_to_acr()
    assert result == round((number.area * 2.471), 2)

# This was the first test file I worked on
# I did not originally include .area, after number (in the last line of both)
# So it took a while for me to fix before realising

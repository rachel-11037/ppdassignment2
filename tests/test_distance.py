# Adam Heavey - Test File: Distance

from PythonFiles.distance import Distance

# Test to convert miles to kilometres
def test_convert_miles2km():
    number = Distance(30)
    result = number.convert_miles2km()
    assert result == round(float(number.distance*1.609), 2)

# Test to convert kilometres to miles
def test_convert_km2miles():
    number = Distance(20)
    result = number.convert_km2miles()
    assert result == round(float(number.distance/1.609), 2)

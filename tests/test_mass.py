# Adam Heavey - Test File: Mass

from PythonFiles.mass import Mass

# Test to convert kilogrammes to stone
def test_convert_kg_to_st():
    number = Mass(5)
    result = number.convert_kg_to_st()
    assert result == round((number.mass / 6.35), 2)

# Test to convert stone acres to kilogrammes
def test_convert_st_to_kg():
    number = Mass(10)
    result = number.convert_st_to_kg()
    assert result == round((number.mass * 6.35), 2)

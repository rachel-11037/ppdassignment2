# Adam Heavey - Test File: Volume

from PythonFiles.volume import Volume

# Test to convert pints to litres
def test_convert_pnt_to_ltr():
    number = Volume(20)
    result = number.convert_pnt_to_ltr()
    assert result == round((number.volume / 1.7598), 2)

# Test to convert litres to pints
def test_convert_lrt_to_pnt():
    number = Volume(15)
    result = number.convert_lrt_to_pnt()
    assert result == round((number.volume * 1.7598), 2)

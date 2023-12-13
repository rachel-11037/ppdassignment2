# Rachel Gillespie - temperature class

class Temperature:
    def __init__(self,temp):
        self.temp = temp

    @property
    def temp(self):
        return self._temp
    
    @temp.setter
    def temp(self, value):
        self._temp = value

    def convert_cel2far(self): # convert °C to °F
        result = float((self.temp*9/5) + 32)
        return result
    
    def convert_far2cel(self): # convert °F to °C
        result = float((self.temp - 32)*5/9)
        return result


if __name__ == "__main__":
    temp1 = Temperature(50) # this is a dummy temperature to test the class.
    print(f"{temp1.temp}°C = {temp1.convert_cel2far()}°F")
    print(f"{temp1.temp}°F = {temp1.convert_far2cel()}°C")

# Rachel Gillespie - distance class

class Distance:
    def __init__(self,distance) -> None:
        self.distance = distance
    
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self,value):
        self._distance = value

    def convert_miles2km(self):
        result = round(float(self._distance*1.609), 2)
        return result
    
    def convert_km2miles(self):
        result = round(float(self._distance/1.609), 2)
        return result


if __name__ == "__main__":
    dist1 = Distance(200) # this is a dummy distance to test the class.
    print(f"{dist1.distance} miles to kilometres = {dist1.convert_miles2km()}")
    print(f"{dist1.distance} kilometres to miles = {dist1.convert_km2miles()}")

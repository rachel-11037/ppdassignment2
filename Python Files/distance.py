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
        result = float(self._distance*1.609)
        return result
    
    def convert_km2miles(self):
        result = float(self._distance/1.609)
        return result
    
if __name__ == "main":
    dist1 = Distance(200)
    print(dist1.convert_miles2km())
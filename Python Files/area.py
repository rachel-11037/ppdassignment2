# Adam Heavey - Class: Area

class Area:
    def __init__(self, area):
        self.area = area

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, new):
        self._area = new

    # Acres to Hectares
    def convert_acr_to_hect(self):
        conversion = round((self.area / 2.471), 2)
        return conversion

    # Hectares to Acres
    def convert_hect_to_acr(self):
        conversion = round((self.area * 2.471), 2)
        return conversion

if __name__ == "__main__":
    example1 = Area(100)
    print(f"{example1.area} hectares converted to acres is {example1.convert_hect_to_acr()}")
    print(f"{example1.area} acres converted to hectares is {example1.convert_hect_to_acr()}")

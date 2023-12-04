# Adam Heavey - Class: Mass

class Mass:
    def __init__(self, mass):
        self.mass = mass

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, new):
        self._mass = new

    # Kilogrammes to Stone
    def convert_kg_to_st(self):
        conversion = (self.mass / 6.35)
        return conversion

    # Stone to Kilogrammes
    def convert_st_to_kg(self):
        conversion = (self.mass * 6.35)
        return conversion


if __name__ == "__main__":
    example1 = Mass(10)
    print(f"{example1.mass} kilogrammes converted to stone is {example1.convert_kg_to_st()}")
    print(f"{example1.mass} stone converted to kilogrammes is {example1.convert_st_to_kg()}")


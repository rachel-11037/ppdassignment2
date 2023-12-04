# Adam Heavey - Class: Volume

class Volume:
    def __init__(self, volume):
        self.volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new):
        self._volume = new

    # Pints to Litres
    def convert_pnt_to_ltr(self):
        conversion = (self.volume / 1.7598)
        return conversion

    # Litres to Pints
    def convert_lrt_to_pnt(self):
        conversion = (self.volume * 1.7598)
        return conversion


if __name__ == "__main__":
    example1 = Volume(15)
    print(f"{example1.volume} pints converted to litres is {example1.convert_pnt_to_ltr()}")
    print(f"{example1.volume} litres converted to pints is {example1.convert_lrt_to_pnt()}")

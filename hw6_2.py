"""
Implement the Road class, in which to define the attributes: length (length), width (width). The values of these
attributes must be passed when the class is instantiated. Make the attributes protected. Determine the method for
calculating the mass of asphalt required to cover the entire roadway. Use the formula: length * width * mass of
asphalt to cover one square meter of the road with 1 cm thick asphalt * number of cm of roadway thickness. Check the
work of the method.
"""


class Road:
    """ Roadbed class """
    # specific weight of 1 sq.m. road bed 1 cm thick (tons)
    _surface_spec_gravity: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        """
        :param length: Roadbed length in meters
        :param width: Roadbed width in meters
        """
        self._length = float(length)
        self._width = float(width)

    def get_surface_gravity(self, thickness: float) -> [float, None]:
        """ Calculation of the mass of the roadbed of a given thickness
        :param thickness: Pavement thickness in centimeters
        :return: Roadbed weight in tons if everything is OK, otherwise None
        """
        try:
            return (self._length * self._width
                    * thickness * self._surface_spec_gravity)
        except TypeError:
            return None


if __name__ == '__main__':
    try:
        road = Road(5000, 25)
        print(
            'The mass of the road surface will be:',
            road.get_surface_gravity(5),
            'tons'
        )
    except TypeError:
        print('the class Road requires 2 positional arguments')

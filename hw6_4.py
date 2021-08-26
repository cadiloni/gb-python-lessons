class Car:
    """ Base class of a Car """
    def __init__(self, color: str, name: str, is_police: bool = False):
        """
        :param color: Car color
        :param name: Name of the model
        :param is_police: Police car or not
        """
        self.color = color
        self.name = name
        self.is_police = True if is_police else False

        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        """ Starts from given speed
        :param speed: Movement speed
        """
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        """ Stops the car """
        self.speed = 0

    def turn(self, direction: str):
        """ Gives the turn to the auto while driving
        :param direction: direction of the turn ('left', 'right')
        """
        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return

        if not self.speed:
            print(f"'Can't turn to {direction}' in place")
            return

        self._direction = direction

    def show_speed(self):
        """ Shows the current speed """
        print(f'My speed is {self.speed} km/h')

    @property     # Decorator
    def direction(self):
        """ Shows the current direction """
        return self._direction


class TownCar(Car):
    """ Class for town cars """

    # max speed for town cars
    _max_granted_speed = 60

    def __init__(self, *args):
        """
        :param args: Auto parameters
        """
        super().__init__(*args)

    def show_speed(self):
        """ shows the speed, and if the speed
        becomes more than max_granted_speed warn """
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class SportCar(Car):
    """ Class for sport cars """
    def __init__(self, *args):
        """
        :param args: Auto parameters
        """
        super().__init__(*args)


class WorkCar(Car):
    """ Class for work car """

    # max speed for work car
    _max_granted_speed = 40

    def __init__(self, *args):
        """
        :param args: Auto parameters
        """
        super().__init__(*args)

    def show_speed(self):
        """ shows the speed, and if the speed
        becomes more than max_granted_speed warn """
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class PoliceCar(Car):
    def __init__(self, *args):
        """
        :param args: Auto parameters
        """
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_data = {
        ('Yellow', 'Kia Rio'): TownCar,
        ('Black', 'Ferrari'): SportCar,
        ('White', 'Lada Granta'): WorkCar,
        ('Blue', 'BMW F10'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print(f"Car name '{car.name}'")
        print(f"Car color '{car.color}'")
        print(f"Car is police '{car.is_police}'")
        print(f"Car speed '{car.speed}'")
        print(f"Car direction '{car.direction}'")
        print(f"Car show speed '{car.show_speed()}'")

        car.turn('asd')     # To test if everything works just fine
        car.turn('left')
        car.go('asd')       # To test if everything works just fine
        print("Car speed after invalid go", car.speed)
        car.go(30)
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('left')
        print(f"Car direction '{car.direction}'")
        car.turn('right')
        print(f"Car direction '{car.direction}'")
        car.stop()
        car.show_speed()
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\n\n')

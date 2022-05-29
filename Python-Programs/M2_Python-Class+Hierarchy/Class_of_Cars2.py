"""Original design By: Mostafa Mohamed April 2022"""
class Car:
    """Define my car class"""

    def __init__(self, color, model, year):
        self.color = color
        self.__model = model    # private
        self.__year = year      # private
        self._make = "Unknown"  # protected

    def get_model(self):
        """Returns the car model"""
        return self.__model

    def get_year(self):
        """Returns the car year"""
        return self.__year

    def get_make(self):
        """Returns the car make"""
        return self._make


class PersonalCar(Car):
    """ a child of the car class"""

    def __init__(self, color, make, model, year, number_seats, number_doors):
        # Car.__init__(self, color, model, year)
        super().__init__(color, model, year)
        self.number_seats = number_seats
        self.number_doors = number_doors
        self.body_type = "Full size"
        self._make = make

    def get_info(self):
        """Returns the car information"""
        # Mazda, 2010, blue color, Full size, 4 doors, 5 seats
        return "{}, {}, {}, {} color, {}, {} doors, {} seats".format(
            self._make, self.get_model(), self.get_year(), self.color,
            self.body_type, self.number_doors, self.number_seats
        )

    def get_model(self):    # Overrides the parent method
        return self.get_make() + ", " + super().get_model()  # calles the parent's method


car1 = Car("Blue", "Mazda", 2010)
# Mazda, 2010 with blue color
print(car1.get_model() + ", " + str(car1.get_year()) +
      " with " + car1.color + " color")
# print(car1.__year)  # will give an error as the year is a private attribute
car2 = PersonalCar("Gray", "Ford", "Impala", 2020, 7, 5)
print(car2.get_info())
print(car2.get_model(), car2.color)

print(car2.get_make())

print(isinstance(car1, Car))               # True
print(isinstance(car1, PersonalCar))       # False

print(isinstance(car2, Car))               # True
print(isinstance(car2, PersonalCar))       # True

print(issubclass(PersonalCar, Car))        # True
print(issubclass(Car, PersonalCar))        # False

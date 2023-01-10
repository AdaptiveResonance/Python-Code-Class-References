from asyncio.windows_events import NULL
from operator import contains
#helpful link:https://funtech.co.uk/latest/explain-object-oriented-programming-to-kids
#Based upon CPRG-104 A1
#Python Zoo class with Hierarchy + Inheritence

class Animal:
    def __init__(self):
        self.__number_of_legs = 4
        self.__number_of_hands = 0

    def look(self):
        return "Number of hands: {hand}, Number of legs: {leg}".format(
            hand=self.__number_of_hands, leg=self.__number_of_legs)


class Bird:
    def __init__(self):
        self.__number_of_legs = 2
        self.__number_of_wings = 2

    def look(self):
        return "Number of wings: {wings}, Number of legs: {leg}".format(
            wings=self.__number_of_wings, leg=self.__number_of_legs)


class Feline(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__characteristic = "Felines belong to the cat family"

    def look(self):
        return super().look() + "\n" + self.get_characteristic()

    def get_characteristic(self):
        return self.__characteristic


class Tiger(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.__characteristic = "Tigers can roar and are lethal predators"

    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic


class WildCat(Feline):
    def __init__(self):
        Feline.__init__(self)
        self.__characteristic = "Wild cats can climb trees"

    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic



class Canine(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.__characteristic = "Canines belong to the dog family"

    def look(self):
        return super().look() + "\n" + self.get_characteristic()
    # Overrides the Look method to show the parent Look in a line + the Canine characteristic

    def get_characteristic(self):
        return self.__characteristic


class Wolf(Canine):
    def __init__(self):
        Canine.__init__(self)
        self.__characteristic = "Wolves hunt in packs and have a leader"

    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic


class FlightBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.__characteristic = "Flight birds fly and hunt for food"

    def look(self):
        return super().look() + "\n" + self.get_characteristic()

    def get_characteristic(self):
        return self.__characteristic


class Eagle(FlightBird):
    def __init__(self):
        FlightBird.__init__(self)
        self.__characteristic = "Eagles fly extremely high and can see their prey from high up in the sky"

    def get_characteristic(self):
        return super().get_characteristic() + "\n" + self.__characteristic


class Zoo:
    def __init__(self):
        self.__animal_list=[] #as a private list
        self.__bird_list=[] #as a private list

    def add(self, living_thing):
        #print('Checking space for', living_thing)# <__main__.Eagle object at 0x000001F0F7ED9FC0>
        if isinstance(living_thing, Bird):#checks bird class>flightbird class>
        #checks if Eagle is instance of Bird, whereas below 3 will not allow
            if len(self.__bird_list) < 1:
                self.__bird_list.append(living_thing)
                print("Bird Added")
            else:
                print("Zoo full for birds")
        else: #living_thing is Animal
            if len(self.__animal_list) < 2:
                self.__animal_list.append(living_thing)#Add living_thing to the animal_list
                print("Animal Added")
            else:
                print("Zoo full for animals")

    def looking(self):
        if len(self.__bird_list)<1 & len(self.__animal_list)<1:#  If both bird_list and animal_list are empty
            print("Zoo empty")
        for animal in self.__animal_list:
            print(animal.look())
            print("")
        for bird in self.__bird_list:
            print(bird.look())
            print("")


zoo = Zoo()
zoo.add(Tiger())#input Tiger Object
zoo.add(Wolf())
zoo.add(WildCat())
zoo.add(Eagle())
zoo.looking()

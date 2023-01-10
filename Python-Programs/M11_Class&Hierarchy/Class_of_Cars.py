# -*- coding: utf-8 -*-
class car:
    __number_of_wheels = 4
    def __init__(self, company_name, model_name, year_of_make,number_of_seats):
        self.__company_name = company_name
        self.__model_name = model_name
        self.__year_of_make = year_of_make
        self.__number_of_seats = number_of_seats
        self.__speed = 0
        
    def get_company_name(self):
        return self.__company_name
    
    def get_model_name(self):
        return self.__model_name
    
    def get_year_of_make(self):
        return self.__year_of_make
    
    def get_number_of_seats(self):
        return self.__number_of_seats
    
    @staticmethod
    def get_number_of_wheels():
        return car.__number_of_wheels
    
    def get_speed(self):
        return self.__speed
    
    def accelerate(self):
        current_speed = self.__speed
        self.__speed += 5
        print("Car accelerates from ",current_speed," to ",self.__speed)
    
    def brake(self):
        current_speed = self.__speed
        if current_speed >= 5:
            self.__speed -= 5
            print("Car brakes from ",current_speed," to ",self.__speed)
        elif current_speed <= 5 and current_speed > 0:
            self.__speed = 0
            print("Car brakes from ",current_speed," to ",self.__speed)
        else:
            print("Car already stopped.")
            

civic = car("toyota","civic",2020,4)

print("company_name: ", civic.get_company_name())
print("model_name: ",civic.get_model_name())
print("year_of_make: ",civic.get_year_of_make())
print("number_of_seats: ",civic.get_number_of_seats())
print("number_of_wheels: ",civic.get_number_of_wheels())
print("current_speed: ",civic.get_speed())
civic.accelerate()
civic.accelerate()
civic.accelerate()
civic.brake()
print("current_speed: ",civic.get_speed())

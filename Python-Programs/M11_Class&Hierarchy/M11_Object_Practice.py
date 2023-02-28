# -*- coding: utf-8 -*-
from typing import final


class Person:
    def __init__(self, name, age, gender, date_of_birth):
        self.__name = name
        self.__age = age
        self.__date_of_birth = date_of_birth
        self.__gender = gender

    def get_name(self):
        return self.__name

    @final#make inmutable and cannot override in subclass
    def get_age(self):
        return self.__age

    @final
    def get_date_of_birth(self):
        return self.__date_of_birth

    @final
    def get_gender(self):
        return self.__gender


class Employee(Person):
    
    def __init__(self, name, age, gender, date_of_birth,
                 company_name, salary, designation):
        super().__init__(name, age, gender, date_of_birth)
        self.__company_name = company_name
        self.__salary = salary
        self.__designation = designation

    def get_designation(self):
        return self.__designation

    def get_company_name(self):
        return self.__company_name

    def get_salary(self):
        return self.__salary

    def get_name(self):
        return super().get_name() + ", " + self.get_designation()


employee = Employee("Tom", 25, "X", "25-June-1996", "BMO", 7000, "developer")
print(employee.get_name())

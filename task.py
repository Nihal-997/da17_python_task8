# 1.BankAccount


class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner              # private variable
        self.__balance = balance          # private variable

    def deposit(self, amount):
        self.__balance += amount          # private method logic

    def _display_balance(self):           # protected method
        print(f"{self.__owner}'s Balance: ₹{self.__balance}")


# 2.Product

class Product:
    def __init__(self, name, price):
        self._name = name                 # protected variable
        self.__price = price              # private variable

    def _get_name(self):                  # protected method
        return self._name

    def __apply_discount(self, percent):  # private method
        self.__price *= (1 - percent / 100)


# 3.Employee


class Employee:
    def __init__(self, name, salary):
        self.__name = name                # private variable
        self._salary = salary             # protected variable

    def _calculate_bonus(self):           # protected method
        return self._salary * 0.1

    def __get_name(self):                 # private method
        return self.__name
    


# 4.Car

class Car:
    def __init__(self, brand, speed):
        self.__brand = brand              # private variable
        self._speed = speed               # protected variable

    def _accelerate(self):                # protected method
        self._speed += 10

    def __get_brand(self):                # private method
        return self.__brand
    

# 5.Student

class Student:
    def __init__(self, roll_no, grade):
        self.__roll_no = roll_no          # private variable
        self._grade = grade               # protected variable

    def _upgrade_grade(self):             # protected method
        self._grade += 1

    def __get_roll_no(self):              # private method
        return self.__roll_no

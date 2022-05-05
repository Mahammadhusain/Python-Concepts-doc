# # Python Abstraction
# from abc import ABC,abstractmethod

# class Car(ABC):

#     @abstractmethod
#     def mileage(self):
#         pass

#     @staticmethod
#     def speed(self):
#         pass

# x=Car()
# x.mileage()


# class Tesla(Car):
#     a=100
#     def color(self):
#         print('This is Red Color')

#     def mileage(self):
#         print("This is Tesla & its mileage is 30kmph")

#     def speed(self):
#         print("This is Tesla Speed 400")


# class Suzuki(Car):
#     def mileage(self):
#         print("This is Suzuki & its The mileage is 25kmph ")


# class Duster(Car):
#      def mileage(self):
#           print("The mileage is 24kmph ")

# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph ")

from abc import ABC, abstractmethod


class Payment(ABC):
    def print_slip(self, amount):
        print('Purchase of amount- ', amount)

    @abstractmethod
    def payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def payment(self, amount):
        print('Credit card payment of- ', amount)


class MobileWalletPayment(Payment):
    def payment(self, amount):
        print('Mobile wallet payment of- ', amount)


p = CreditCardPayment()
p.payment(200)
p.print_slip(400)

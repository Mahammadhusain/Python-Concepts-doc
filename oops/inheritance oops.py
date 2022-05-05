# class Student:
#     name = 'Rajesh'
#     mobile = 888888888
    

#     def get_info(self):
#         return self.name


# class Addmi(Student):
#     name = 'Mukesh'
#     # mobile = 7777777777
#     year = 2020

#     def get_info(self):
#         return self.name


# add = Student()
# print(add.get_info())



# add = Addmi.name
# mob= Addmi.mobile
# yr = Addmi.year


# print(add)
# print(mob)
# print(yr)



# class Parent:
#     name1 = 'Rahul'
#     name2 = 'Mehul'
#     mobile1 = 999999999
#     mobile2 = 888888888

#     def Property(self):
#         return 'This is Parent Property'



# class Son(Parent):
#     pass



# son1 = Son()
# son2 = Son()
# son3 = Son()
# son4 = Son()
# son5 = Son()
# son6 = Son()
# print('Rahul',son1.mobile1)
# print('Mehul',son2.mobile2)
# print(son1.name)
# print(son1.mobile)
# print(son1.Property())


# class Car:
#     name1 = 'Tesla'
#     name2 = 'Maruti'
#     name3 = 'Hundai'
#     model = 'ABC'
    # def get_model1(self):
    #     print self.name1
    # def get_model2(self):
    #     print self.name2
    # def get_model3(self):
    #     print self.name3

# class Car1:
#     milageTesla = '200 km/h'
#     milageMarhuti = '400 km/h'
#     milageHundai = '600 km/h'

# class TeslaCar(Car,Car1):
#     color = 'Black'
# class HundaiCar(Car,Car1):
#     cartype = 'Sport Car'
# class MarutiCar(Car,Car1):
#     withac = 'True'


# t1 = TeslaCar()
# print(t1.milageTesla)
# print(t1.color)

# m1 = MarutiCar()
# print(m1.milageMarhuti)
# print(m1.w)

# h1 = HundaiCar()
# print(h1.milageHundai)
# print(h1.cartype)


# Heirical Inheritance
# class Fruit:
#     colorMango = 'Yellow'
#     colorCherry = 'Red'
#     colorKiwi = 'Brown'


# class Mango(Fruit):
#     pass

# class Cherry(Fruit):
#     pass


# class Kiwi(Fruit):
#     pass


# mangocolor = Mango()
# print(mangocolor.colorMango)

# ------------------------------------- Python Inheritance Concepts -------------------------------------
# Single Inheritance
# class A:
#     pass
# class B(A):
#     pass


# Multiple Inheritance
# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass

# Multilevel Inheritance
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass

# Heirical Inheritance
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(A):
#     pass
# class E(A):
#     pass


# Hybrid Inheritance
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass

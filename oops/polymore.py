# Polymorephisam in Python Duck typing
class Tomato:
    def food_type(self):
        print("Vegetable")

    def color(self):
        print("Red")

class Banana:
    def food_type(self):
        print("Fruit")

    def color(self):
        print("Yellow")

class Kaju:
    def food_type(self):
        print("Dry-Fruit")

    def color(self):
        print("White")

# PolymorePhisum Handler Class

# for Calling F_TYPE METHOD
def calling_type_of_food(a):
    a.food_type()

# for Calling COLOR METHOD
def calling_color(b):
    b.color()


# ------------------------------------------
# obj_tomato = Tomato()
# obj_banana = Banana()
# obj_kaju = Kaju()
# # ------------------------------------------
# calling_type_of_food(obj_tomato)
# calling_color(obj_tomato)
# calling_type_of_food(obj_banana)
# calling_color(obj_banana)
# calling_type_of_food(obj_kaju)
# calling_color(obj_kaju)
# ------------------------------------------



# ------------------------------------------
# # Method Overloading
# ------------------------------------------
# class Myclass:
# 	def sum(self, a=None, b=None, c=None):
# 		if a!=None and b!=None and c!=None:
# 			s = a + b + c
# 		elif a!=None and b!=None:
# 			s = a + b
# 		else:
# 			s = 'Provide at least Two Numbers'
# 		return s
		
# obj = Myclass()
# print(obj.sum())

# ------------------------------------------
# Method Overriding-1
# ------------------------------------------
# class Add:
#     def result(self, a, b):
# 	    print('Addition:', a+b)
		
# class Multi(Add):
#     def result(self, a, b):
# 	    print('Multiplication:', a*b)
		
# m = Multi()
# m.result(10, 20)

# ------------------------------------------
# Method Overriding-2
# ------------------------------------------
# class Add:
# 	def result(self, a, b):
# 		print('Addition:', a+b)
		
# class Multi(Add):
# 	def result(self, a, b):
# 		super().result(10, 20)				# Calling Parent Class's Method
# 		print('Multiplication:', a*b)
		
# m = Multi()
# m.result(10, 20)

# ------------------------------------------
# Operator Overloading
# ------------------------------------------
# class A:
# 	def __init__(self, x):
# 		self.x = x
# 	def __add__(self, other):
# 		return self.x + other.x
			
# class B:
# 	def __init__(self, x):
# 		self.x = x
		
# a = A(100)
# b = B('200')
# print(a+b)		#A.__add__(a, b)

# 10+20			int.__add__(10, 20)
# 'a'+'b'			str.__add__('a', 'b')
# print(a+b)			#A.__add__(a, b)

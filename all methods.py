# List

# a= [1,2,88,74,6,88]
# b= [9,54,12]
# print('Origanl list',a)
# a.append(80)
# print('New list',a)

# a.clear()
# print('New list',a)

# a.copy()
# print('New list',a)

# b= a.count(88)
# print('Total elements',b)

# a.extend(b)
# print('Extended A By B',a)

# p=a.index(88)
# print(p)


# a.insert(4,74)
# print(a)

# a.pop()
# print(a)

# a.remove(88)
# print(a)

# a.reverse()
# print(a)

# a.sort()
# print(a)

# p=print(len(a))

# a=['apple',5.6,9,4.555]
# print(type(a))

# ----------------------------------------------------------------

# Tuple

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.index(5)

# print(x)

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(5)

# print(x)

# a= '{Digit} - Accosiated with - {char} and Its Symbols is {symb}'.format(char ='A', Digit = 1, symb = '😁')
# print(a)


# a= ['Apple','Banana','Orange','Kiwi']
# p = " and ".join(a)  
# print(p)


# a=[1,5,8]

# print('Hello')
   

# ----------------------------------------------------------------
# Dictionary


# a= [♔,♕,♖,♗,♘,♙,♚]
# b= ['a','b','c','d','e','f','g']
# for i in a:
#     print(i)

# a= ['Apple','Banana','Orange']
# a = enumerate(a)
# print(list(a))

# print(a[::3])
# print(a[slice(4)])


# a=10
# b=20
# print(a,b)
# a,b = b,a
# print(a,b)
# import random
# a= [1,5,19,4]
# random.shuffle(a)
# print(a)



# List Slicing

# a= [1,52,8,94,34,5,7,52,]
# print(a[])
# p = 12
# q = 15
# r = 14
# s = 65

# a = [p,q,r,s]
# print(type(a))

# a= []
# while len(a)<=3:
#     a.append(int(input("Enter Your Number = ")))
#     print(a)
    
# a= 'Yash Pal'
# a = ['Apple',2,3.14,'Yes',45,56]
# print(len(a))
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# for i in a:
#     print(i)

# for i in a:
#     if i == 'P':
#         break
#     print(i)
#     print(type(i))
    
# a = ['Apple',2,3.14,'Yes',45,56]
# for i in a:
#     if i == 'Yes':
#         continue
#     print(i)

# a= [1,45,25,78,36,98,45,24,47,65,28]
# for i in a:
#     if i == 78:
#         break
#     print(i)

# for i in a:
#     if i == 24:
#         continue
#     print(i)

# for i in range(0,20,5):
#     print(i)

# a= [1,2,3,4]
# b= ['A','B','C','D',"e"]
# for i in a:
#     for j in b:
#         print(i,j)

# a= [1,2,3,4]
# for i in a:
#     pass

# a= [1,2,3,4]
# sum = 0
# for i in a:
#     sum = sum+i
# print(sum)


# reduce,map,filter,format

# Map Function

# def Squre(n):
#     return n*n

# a= [1,2,3,4,5]

# b= map(Squre,a)
# print('Orignel List',a)
# print('Squers Of List',list(b))



# Filter Function

# a=[1,54,84796,564,5455,455,7485,58,45,528,145,58,45,88,4,8]

# def MyFilter(a):
#     if a<2000:
#         return False
#     else:
#         return True

# d = filter(MyFilter,a)
# print(list(d))


# Fromat Function
# For String Only
# a= 'This Is {var2} and his roll {var1}'
# p = a.format(var1 = 'Rahul',var2=101,)
# print(p)

# For List
# a= [101,102,103,104]
# b=['Rajesh','Mukesh','Dinesh','Ramesh']
# c=['Apple','Banan','Kiwi','Orange']

# for i in range(0,len(a)):
#     mydat ='This is-  {0} eat - {1}'
#     print(mydat.format(b[i],c[i]))

# a= [101,102,103,104]
# b=['Rajesh','Mukesh','Dinesh','Ramesh']
# c=['Apple','Banan','Kiwi','Orange']


# Reduce Function
# from functools import reduce
# numbers = [3, 4, 6, 9, 34, 12]

# def custom_sum(a,b):
#     return round(a / b)

# result = reduce(custom_sum, numbers)

# print(result)

# F - String
# b=20
# a=f'My Age is - {b} '

# print(a)

# new = []
# for i in range(0,10):
#     new.append(i)

# print(new)


# Dictionary

# a={'A':1,'B':2,'C':3}
# print(a)

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": {'A':1,'B':2,'C':3}
# }

# print(thisdict.fromkeys(thisdict))

# a={1:1,'B':2,'C':3}
# print(a.get(1))
# print(a[1])

# a={'A':1,'B':2,'C':3}
# p =list(a.items())
# print(type(p))


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.keys()

# print(list(x))

# a={'A':1,'B':2,'C':3}
# a.popitem()
# print(a)

# car = {
#   "brand": "Ford",
#   "model": '',
#   "year": 1964
  
# }

# x = car.setdefault("tesla", "tesla m1")

# print(x)

# Change Value
# a={'A':1,'B':2,'C':3}
# a['A'] = 3
# print(a)

# Add Items
# a={'A':1,'B':2,'C':3}

# a['D'] = 4
# print(a)

# For loop Access only keys
# a={'A':1,'B':2,'C':3}
# for i in a:
#     print(i)

# For Loop Access only Values
# a={'A':1,'B':2,'C':3}
# for i in a:
#     print(a[i])

# Get Values Using .values() Method
# a={'A':1,'B':2,'C':3}
# b=[]
# for i in a.values():
#     #Append Values or keys or item
#     b.append(i)
# print(b)

# a= {'Apple':100,'Banana':{'Jan':100,'Feb':50,'Mar':{'1':80,'5':250}}}
# print(a['Banana']['Mar'])


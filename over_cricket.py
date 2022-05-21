# # over = 0
# # ball = 0

# # while True:
# #     p = input('y = ')
# #     if p == 'y' and (ball)in range(0,6):
# #         ball += 1
print()
# #         if ball > 5:
# #             over+=1
# #             ball = 0

# #     print(ball,"******** ball ************")
# #     print((over+(ball*0.1))  ,"********* over ***********")

# # --------- Script for OVER Counter with 6 BALL in Cricket ------------

# # I created one python script for count OVER with 6 BALL when i reach at 0.3 BALL then i got OVER = 0.30000000000000004
# # insted of 0.3 how to solve it with bellow script

# # In python (0.1 + 0.2) is not equal 0.3 but,
# # it's give an outupt (0.1 + 0.2) = 0.30000000000000004

# # i want to outout (0.1 + 0.2) = 0.3


# over = 0
# ball = 0

# while True:
#     p = input('y = ')
#     if p == 'y' and (ball)in range(0,6):
#         ball += 1
        
#         if ball > 5:
#             over+=1
#             ball = 0
#     q =over+(ball*0.1)
#     if q == 0.30000000000000004:
#         q = 0.3
#         print(ball,"******** ball ************")
#         print(q  ,"********* over ***********")
#     else:
#         print(ball,"******** ball ************")
#         print(q  ,"********* over ***********")




# a  =  0.1
# b  =  0.2
# c = a+b
# print(c)
# w = Decimal(str(c))

# # print(round(w,20))
# print(0.29999999999999998890)

# score, overs, balls = 0, 0, 0


# while True:
#     runs = int(input("Input number of runs : "))
#     if runs in range(0,7):
#         score += runs
#         balls += 1
#         if balls == 6:
#             overs += 1
#             balls = 0 
            
#     print("Score :",score)
#     print("Overs :",str(overs)+'.'+str(balls))
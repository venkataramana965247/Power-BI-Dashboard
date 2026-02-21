'''pattern programs'''

# for i in range(1,10):
#     for j in range(1,10):
#         if (i==j or i+j==10 or i==1 or i==9):
#             print("*",end =" ")
#         else:
#             print(" ", end=" ")
#     print()        

# for i in range(1,10):
#     for j in range(1,10):
#         if ((j==5) or (i==5) or(j==9 and i>=5) or (j==1 and i<=5) or (i==9 and j<=5) or (i==1 and j>=5)):
#             print("*",end =" ")
#         else:
#             print(" ", end=" ")
#     print() 

# for i in range(1,10):
#     for j in range(1,10):
#         if ((i==j and i<=5) or (i+j==10 and i<=5) or (j==5 and i>=5)):
#             print("*",end =" ")
#         else:
#             print(" ", end=" ")
#     print()  


# for i in range(1,10):
#     for j in range(1,10):
#         if ((i+j==6) or (i-j==4) or (j-i==4) or (i+j==14)):
#             print("*",end =" ")
#         else:
#             print(" ", end=" ")
#     print()
 

# for i in range(1,10):
#     for j in range(1,10):
#         if ((j==5 and i>=5) or (i+j==10 and i<=5) or (i==j and i<=5)):
#             print("*",end =" ")
#         else:
#             print(" ", end=" ")
#     print()

'''pattern programs 5*5'''
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()





"""range based programs(Tables and how to find the even numbers)"""

# n=4
# if (n%2==0):
#     print(f"{n} is the even")

# for n in range(1,21):
#     if (n%2==0):
#         print(f"{n} is the even")

# n=5
# for i in range(1,11):
#     print(f"{n} * {i}= {n*i}")

# for n in range(5,11):
#     for i in range(1,11):
#         print(f"{n} * {i}= {n*i}")

'''factorial of 1 number and given numbers'''

# n=5
# fact =1
# for i in range(1,n+1):
#     fact=fact*i
# print(f"{n} factorial : {fact}")


# for n in range(2,9):
#     fact =1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(f"{n} factorial : {fact}")

'''prime numbers'''

# n=7
# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count+=1
# if (count==2):
#     print(f"{n} is prime")

# for n in range(1,51): 
#     count=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count+=1
#     if (count==2):
#         print(f"{n} is prime")

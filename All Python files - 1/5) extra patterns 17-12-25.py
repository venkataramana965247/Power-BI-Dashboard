'''pattern programs 5*5'''
# for i in range(1,6):
#     for j in range(1,6):
#         # print("*",end=" ")
#         # print(j,end=" ")
#         print(i,end=" ")
#         # print(j%2,end=" ")
#         # print(i%2,end=" ")
#     print()

'''pattern programs 7*7 with numbers 1 to 9'''
# k=1
# for i in range(1,8):
    
#     for j in range(1,8):
#         print(k,end=" ")
#         k=k+1
#         if (k==10):
#             k=1
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if (i%2==0):
#             print("$",end=" ")
#         else:
#             print("#",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if (j%2==0):
#             print("$",end=" ")
#         else:
#             print("#",end=" ")
#     print()

'''pattern programs with i=increasing and j=decreasing'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
    
'''pattern programs with i=decreasing and j=increasing'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

'''pattern programs with i=increasing and j=decreasing from i to 1'''
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''pattern programs with i=increasing and j=increasing from i to 5'''
# for i in range(1,6):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()

'''1)pattern programs with i=decreasing and j=decreasing from 5 to i'''
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

'''2)pattern programs with i=increasing and j=decreasing from 5 to i'''
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()

'''3)pattern programs with i=decreasing and j=increasing from i to 5'''
# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()

'''4)pattern programs with i=decreasing and j=decreasing from i to 1'''
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''1)pattern programs with left side spaces and j increasing from 1 to i'''
# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

'''2)pattern programs with left side spaces and j decreasing from i to 5'''
# for i in range(5,0,-1):
#     for k in range(1,i):
#         print(" ",end=" ")
#     for j in range(i,6):
#         print(j,end=" ")
#     print()

'''slicing concept'''
# # #     0  1  2  3  4  5
# list=[10,20,30,40,30,40]
# # #     -6 -5 -4 -3 -2 -1

# # print(list[ : : ])
# # print(list[ :])
# # print(list[2:5])
# # print(list[0:6:2])  #step/skip value
# # print(list[-5:-2])
# # print(list[ : :-1])  #reverse order
# print(list[0:len(list)])


'''methods of the list'''

'''1)append() or add'''

# list=[]
# print("Enter the 5 integers:")
# for i in range(5):
#     ele= int(input())
#     list.append(ele)
# print("list is :" ,list)

'''2)insert()'''
# #     0   1  2  3
# list=[10,20,30,20]
# #    -4  -3 -2  -1

# list.insert(0,100)
# print("list is : ", list)

'''3)extend()'''
# #     0   1  2  3
# list=[10,20,30,20]
# #    -4  -3 -2  -1
# list.extend([12,17,32,23])
# print(list)

'''4)sort() or ascendig order'''
# #     0   1  2  3
# list=[10,20,30,20]
# #    -4  -3 -2 -1
# list.sort()
# print(list)

'''5)reverse()'''
# #     0   1  2  3
# list=[10,20,30,20]
# #    -4  -3 -2  -1
# list.reverse()
# print(list)

'''6)pop()'''
# list=[10,20,30,20,40,30,50]
# list.pop()
# print(list)


# #     0  1  2  3   4  5  6
# list=[10,20,30,20,40,30,50]
# #     -7 -6 -5 -4 -3 -2 -1
# list.pop(3)
# print(list)

'''7)count()'''
# #     0  1  2  3   4  5  6
# list=[10,20,30,20,40,30,50]
# #     -7 -6 -5 -4 -3 -2 -1

# print(list.count(20))

'''8)remove()'''
# #     0  1  2  3   4  5  6
# list=[10,20,30,20,40,30,50]
# #     -7 -6 -5 -4 -3 -2 -1
# list.remove(20)
# print(list)

'''9)clear()'''
# #     0  1  2  3   4  5  6
# list=[10,20,30,20,40,30,50]
# #     -7 -6 -5 -4 -3 -2 -1
# list.clear()
# print(list)

'''extra examples of the list methods'''

# list=[10,20,30,40]

# list.append(120)
# print(list)

# list.remove(20)
# print(list)

# list[0]=list[0]+5
# print(list)

# tuple=(10,20,30,20)
# print(tuple)





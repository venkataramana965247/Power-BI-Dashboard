'''Recursion => Function calling itself'''

# def test():
#     print("hi")
#     test()
#     print("bye")
#     return
# test()

# def test(n):
#     print(n)
#     if n>1:
#         test(n-1)
#     print(n)
#     return    #The return at the end is redundant — it just exits the function and returns None, which would happen anyway when the function reaches its end.
# test(4)

# def test(n):
#     print(n)
#     if n>1:
#         test(n-1)
#     print(n)
#     #return
# test(4)

# def test(n):
#     print(n)
#     if n>1:
#         test(n-1)
#     # print(n)
#     return
# test(4)

# def test(n):
#     # print(n)
#     if n>1:
#         test(n-1)
#     print(n)
#     return
# test(4)

# def test(n):
#     print(n)
#     # if n>1:
#     #     test(n-1)
#     # print(n)
#     return
# test(4)

'''factorial of the n nums by using the recursion function'''
# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# res=fact(4)
# print(res)

'''lambda built-in fun'''
# nums=[3,7,4,8,5,2,9,6]
# print(nums)

# doubles=list(map(lambda x:x*2,nums))
# print(doubles)

# evens=list(filter(lambda x:x%2==0,nums))
# print(evens)

'''find the squares and then check even also'''
# nums=[3,7,4,8,5,2,9,6]

# squares=list(map(lambda x:x**2,nums))
# evens=list(filter(lambda x:x%2==0,squares))
# print(evens)

'''in single of code like how the both map() and filter() add'''
# nums=[3,7,4,8,5,2,9,6]
# print(nums)
# evens=list(filter(lambda x:x%2==0 ,map(lambda x:x**2,nums)))
# print(evens)

                # [or]

# nums=[3,7,4,8,5,2,9,6]
# evens=list(map(lambda x:x**2,filter(lambda x:x%2==0,nums)))
# print(evens)



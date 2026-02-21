'''functions of python'''
# definition:
        # it is a block of the instruction defined to perform a task. 
        # and funtion has name to call

# print("hi")
# print("hello")
# print("welcome")

# def test():
#     print("hi")
#     print("hello")
#     print("welcome")
#     return
# test()     #fun call



# def st():
#     print('abc.....')
#     return

# def end():
#     print("xyz.....")
#     return

# st()
# end()
# end()

# def add(a,b):
#     c=a+b
#     print(f"{a} + {b} = {c}")
#     return
# add(12,13)

'''functions with even num'''
# def even(n):
#     if (n%2==0):
#         print(f"{n} is the even num")
#     else:
#         print(f"{n} is not even num")
#     return
# even(12)

'''functions with tables'''
# def tables(n):
#     for i in range(1,11):
#         print(f"{n} * {i}= {n*i}")
#     return
# tables(13)
# tables(2)

'''functions with the arguments and with the return values'''

# def add(a,b):
#     c= a + b
#     return c
# res=add(10,20)
# print(f"sum = {res}")

'''functions with even num with return values'''
# def even(n):
#     if (n%2==0):
#         return "yes it is a even num"
#     else:
#         return "it is the not even num"
# res=even(13)
# print(f"{res}")

'''functions with the biggest num'''
# def big(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     else:
#         return c
# res=big(10,60,30)
# print(f"big num is : {res}")

'''functions with the perfect num'''
# def perfect(n):
#     sum=0

#     for i in range (1,n):
#         if (n%i==0):
#             sum=sum+i
#     if(n==sum):
#         return "perfect num"
#     else:
#         return "not perfect num"

# res=perfect(6)
# print(res)

'''Argument type functions: required,default,keyword,variable'''

'''1)required arg func: we need to pass same num of values to args'''
# def test(a,b,c):
#     print(a,b,c)
#     return
# test(10,20,30)
# test(10,20)  #it will throws an error ,test() missing 1 "required positional argument": 'c'

'''2)default args fun: providing default values to args in the definition of fun'''
# def test(a=10,b=20,c=30):
#     print(a,b,c)
#     return
# test()    #default args fun
# test(15)   #default args fun
# test(5,10)  #default args fun
# test("ram","sita","hanuman")
# test("abc","xyz","pqr")

'''3)keyword args fun:we can pass values by using arg names as keywords
                    we can pass values in any order'''

# def data(name,age):
#     print(f"name : {name}, Age = {age}")
#     return
# data("ramana",22)  #keyword args fun
# data(22,"ramana")   #keyword args fun ,if you forgot the values where to write then the keyword args understand  
# data(age=22,name="ramana")  #keyword args fun

'''4)variable args func(*): we can take any num of args into single variable'''
# def test(*arr):  # * it is a capable of holding any num of values into variable
#     print(arr)
#     return

# test()
# test(10,10)
# test("abc",12,3.34)
# test(10,20,30,40,50)

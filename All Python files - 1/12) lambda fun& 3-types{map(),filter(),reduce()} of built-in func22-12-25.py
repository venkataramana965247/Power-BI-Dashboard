'''lambda expression:
    1)a lambda can take any no.of arguments but has only one expression
    2)use cases short, one line functions often used with like map(),filter(), and reduce()
'''
'''syntax of lambda:'''
    #lambda arguments(ex: a,b) : expression(ex: a+b)
'''ex: '''
# res=lambda a,b : print(f"sum of these two nums : {a+b}")
# res(10,20)

'''normal fun'''
# def fun():
#     print("hello")
#     return
# fun()

'''lambda fun'''
# fun=lambda : print("hello")
# fun()

'''normal fun'''
# def add(a,b):
#     print(f"sum: {a+b}")
#     return
# add(10,20)

'''lambda fun'''
# add=lambda a,b: print(f"sum: {a+b} ")
# add(10,20)

# add=lambda a,b: print(f"sum:",a+b)
# add(10,20)

'''Functions with arguments and the return values '''

'''normal fun'''
# def add(a,b):
#     return a+b
# res=add(10,20)
# print(f"sum = {res}")

'''lambda fun'''
# add=lambda a,b:a+b
# res=add(10,20)
# print(f"sum = {res}")

'''lambda fun with 3-types of built-in functions'''

'''1)lambda with map():=> perform operation on each element and returns same length of the list'''
                        # "that is the input len is same as the output len"

'''syntax => list(map(lambda fun, iterable(for loops))'''

# ex:
# input is nums= [3,6,2,7,8,5,4,9]   len is the 8
# doubles =[6,12,4,14,16,10,8,18] len is the 8
# squares=[9,36,4,49,64,25,16,81]  len is the 8

# ex:program using map()

# nums=[3,7,2,8,4,5]
# doubles=list(map(lambda x : x+x,nums))
# print(doubles)

# nums=[3,7,2,8,4,5]
# res=list(map(lambda x: x+1,nums))
# print(res)

# nums=[3,7,2,8,4,5]
# squares=list(map(lambda x:x*x ,nums))
# print(squares)

# nums=[3,7,2,8,4,5]
# squares=list(map(lambda x:x%2==0 ,nums))
# print(squares)

# words=['python','java','andoid','php']
# res=list(map(lambda s:len(s) ,words))
# print(res)

# words=['python','java','andoid','php']
# res=list(map(lambda s:s.upper(),words))
# print(res)

# words=['python','java','andoid','php']
# res=list(map(lambda x: x,words))
# print(res)

# words=['python','java','andoid','php']
# res=list(map(lambda s:len(s)>5,words))
# print(res)

'''2)lambda with filter() :filter the list on given condition(may not the same length)'''
        
'''syntax => list(filter(lambda conditions, iterable(for loops))'''
# ex:
#     nums= [3,6,2,7,8,5,4,9]
#     even=[6,8,4,8]

# nums=[3,7,2,8,4,5]

# res=list(filter(lambda x:x<=5 ,nums))
# print(res)

# evens=list(filter(lambda x:x%2==0 ,nums))
# print(evens)

# words=['python','java','andoid','php']
# res=list(filter(lambda s:len(s)>=5,words))
# print(res)

'''3)lambda with reduce() : perform operation on each element and returns single value'''
# syntax::
'''from functools import reduce
    reduce(lambda fun ,iterable,initial value(0))'''

'''EX ::'''

'''add of two nums'''
# from functools import reduce
# nums=[3,7,4,8,5,2,9,6]

# res=reduce(lambda x,y:x+y,nums)
# print(res)

'''count of nums'''
# from functools import reduce
# nums=[3,7,4,8,5,2,9,6]

# res=reduce(lambda x,y:x+1,nums,0)
# print(res)

# from functools import reduce
# nums=[3,7,4,8,5,2,9,6]

# res=reduce(lambda x,y:x<y,nums,0)
# print(res)

'''big of the two nums'''

# big=lambda x,y: x if x>y else y
# res=big(10,20)
# print(res)

'''find the big of the three nums'''

# big=lambda x,y,z: x if x>y and x>z else y if y>z else z
# res=big(10,30,20)
# print(res)

'''find the big of the two nums using reduce()'''
# from functools import reduce
# nums=[3,7,4,8,5,2,9,6]

# res=reduce(lambda x,y:x if x>y else y ,nums)
# print(res)

'''find the big of the three nums using reduce()'''
# from functools import reduce

# a, b, c = 10, 30, 20
# res = reduce(lambda x, y: x if x > y else y, [a, b, c])
# print(res)  # 30

''':::     EXTRA EXAMPLES(WITH ADVANCED)   :::'''


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
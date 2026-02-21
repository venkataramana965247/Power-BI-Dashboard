
'''list comprehension(plz remember the syntax then only it is easy) :'''
'''definition of list of comprehension'''
# List comprehension is a short ,
# single-line way to create a new list by looping through items and applying a condition or operation
'''syntax : '''
        # new_list=[expression for item in iterable if condition==True]


'''1)normal list'''
# list=[]
# for i in range(1,101):
#     list.append(i)
# print(list)

'''2)list comprehension'''
# list=[x for x in range(1,101)]
# print(list)

# list=[x for x in range(1,101) if x%2==0]
# print(list)

'''from the num of 1 to 10 nums doubles'''
# doubles=[x*2 for x in range(1,11)]
# print(doubles)

'''from the num of 1 to 10 squares'''
# squares=[x**2 for x in range(1,11)]
# print(squares)

'''only even nums of squares will print??'''
# squres=[x**2 for x in range(1,11) if x%2==0 ]
# print(squres)

'''another examples of the normal program even nums of 1 to 20'''
# list=[]
# for i in range(1, 21):
#     if (i%2==0):
#         list.append(i)
# print(list)


'''by using the list comprehension method from the nums of the 1 to 20'''
# evens=[x for x in range(1,21) if x%2==0]
# print(evens)

'''normal program of the find the grater than 5 in the given list'''
# nums = [3,2,5,8,6,9,4,7]
# res=[]
# for x in nums:
#     if x>5:
#         res.append(x)
# print(res)

'''list comprehension'''
# nums = [3,2,5,8,6,9,4,7]
# res=[x for x in nums if x>5]
# print(res)

'''normal program of find given list of only even nums'''
# nums=[3,2,5,8,6,9,4,7]
# res=[]
# for x in nums:
#     if x%2==0:
#         res.append(x)
# print(res)

'''list comprehension find given list of only even nums'''
# nums=[3,2,5,8,6,9,4,7]
# res=[x for x in nums if x%2==0]
# print(res)


'''normal program string conversion lower cases to upper cases'''
# words=["java","python","react","c++"]

# res=[]
# for s in words:
#     res.append(s.upper())
# print(res)

'''list comprehension string conversion lower cases to upper cases'''
# words=["java","python","react","c++"]
# res=[s.upper() for s in words]
# print(res)

'''extra examples of by using the list comprehension'''
# words=["Java","Python","React","C++"]
# res=[len(s) for s in words]
# print(res)

# words=["Java","Python","React","C++"]
# first=[s[0] for s in words]
# print(first)

# words=["Java","Python","React","C++"]
# last=[s[-1] for s in words]
# print(last)

# words=["Java","Python","React","C++"]
# rev=[s[ : :-1] for s in words]
# print(rev)

'''list comprehension one more ex'''

# words=["Java","Python","React","C++"]

# res=[(s,len(s)) for s in words]
# print(res)

'''dictionary comprehension'''
# words=["Java","Python","React","C++"]

# res={s:len(s) for s in words}
# print(res)

'''1)'''
# res={s:s**2 for s in range(1,21) if s%2==0 }
# print(res)
'''2)'''
# res={s:s*s for s in range(1,21) if s%2==0 }
# print(res)

'''normal program of the >=5 print that type of the string and convert upper cases'''
# words=['java','python','net','android']
# res=[]
# for i in words:
#     if len(i)>=5:
#         res.append(i.upper())
# print(res)

'''write the program the if string is >= 5 then convert this into the upper cases '''
# words=['java','python','net','android']
# res = [(i.upper()) for i in words if len(i)>=5]
# print(res)


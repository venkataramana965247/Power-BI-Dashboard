'''set :
    1)it is defined as a {}
    2)not allow the duplicates
    3)not index based as well as a not slicing based
    4)mutable
'''


# set={10,20,30,40,50,30,40,50} #set it will remove the duplicates values

# print(set)

# set.add(78)
# print(set)

# set.discard(30) #delete
# print(set)

# print(set[2])  #error :no indexing

'''operations of the set fun'''
'''1)union'''
# s1={1,2,3,4}
# s2={3,4,5,6}

# print(s1.union(s2))
# # or 
# print(s1 | s2)  # union symbol

'''2)intersection'''
# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.intersection(s2))  #common elements will print
# print(s1 & s2)

'''3)difference'''
# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.difference(s2))
# print(s1-s2)

# print(s2-s1)

'''4)symmetric_difference'''
# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.symmetric_difference(s2))  #it is a reverse operation of the intersection
# print(s1 ^ s2)

'''5)update'''
# adds all elements from the given iterable into the single set in-place 
# s1={1,2,3,4}
# s2={3,4,5,6}
# s1.update(s2)
# print(s1)


'''extra examples or exercises'''
# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.intersection(s2))  #common elements will print
# print(s1 & s2)              #intersection symbol(&)
# (ex : the given two sets consists of the two common elements those are (3,4))

# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.difference(s2))     
# print(s1-s2)                #difference symbol(-)


# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s2.difference(s1))    
# print(s2-s1)                #difference symbol(-)


# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.symmetric_difference(s2))  #it is a reverse operation of the intersection
# print(s1 ^ s2)              #symmetric_difference symbol(^)

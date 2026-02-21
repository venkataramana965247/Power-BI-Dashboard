'''Data type List :programs'''

''' 1)it is defined as a square brackets []
    2)it is a mutable (we can change the values)
    3)it allows the duplicate or common values (ex: [20,20,10,10,45,32,23])
    4)it allows the hetrogeneous values(eg: integer , float , char , string ,boolean)
    5)it is an ordered collection of items
    6)it allows the indexing and slicing
'''

'''basic list programs'''
# list=[10,20,30,40,30,40]
# print(list)
# print(list[0])
# print(list[-1])
# print(list[-len(list)])

      #  0   1  2  3  4  5  6  7
# arr = [3 , 4, 5, 5, 7, 2, 9, 5]
#        -8 -7 -6 -5 -4  -3 -2 -1
# print("length of the array:", len(arr))
# print("first ele:" , arr[0])
# print("last ele:" , arr[-1])


'''list by using only the without using the range'''

#     #  0  1   2  3  4  5  6  7
# arr = [3 , 4, 5, 5, 7, 2, 9, 5]
# #      -8 -7 -6 -5 -4 -3 -2 -1
# print("elements are :")
# for i in arr:
#     print(i)

'''list by using the range function'''
#     #  0  1   2  3  4  5  6  7
# arr = [3 , 4, 5, 5, 7, 2, 9, 5]
# #      -8 -7 -6 -5 -4 -3 -2 -1
# print("elements are : ")
# for i in range(0,len(arr)):  #len(arr)=8, so 8-1=7, last index is 7
#     print(arr[i])

'''list by using the reverse range function'''
#     #    0  1   2  3  4  5  6  7
# arr = [3 , 4, 5, 5, 7, 2, 9, 5]    
#        # -8 -7 -6 -5 -4 -3  -2 -1

# print("elements reverse are :")
# for i in range(len(arr)-1,-1,-1):  #len(arr)=>8, so 8-1=>7, last index is 7, -1 is stop value(0) ,-1 is step/skip value
#     print(arr[i])

'''How It Works(49 line):

range(len(arr)-1,-1,-1):

len(arr)-1=>8-1=>7 : Starts from the last index of the list.
-1: Stops just before index -1 (so it stops at 0).   like -5,-4,-3,-2,-1,0,1,2,3,4,5
-1: Moves backward one step at a time.'''

'''[or]'''
# arr = [3 , 4, 5, 5, 7, 2, 9, 5]
# print("elements reverse are :")
# for i in arr[::-1]:   #slicing concept with step/skip value -1
#     print(i)

'''sum of the all elements in the list'''
# arr = [3,8,4,9,6,2,7,5]

# sum=0
# for i in arr:
#     sum=sum+i
#     print("sum of the step by step arr :", sum)
# print("sum of the all elements in the given arr :", sum)

'''count the even num in the list'''
# arr = [3,8,4,9,6,2,7,5]
# count=0
# for i in arr:
#     if(i%2==0):
#         count=count+1    # or count+=1

# print("count of the even num in given arr :" , count)

'''count only even num in given list'''
# arr = [3,8,4,9,6,2,7,5]
# for i in arr:
#     if (i%2==0):
#         print("even num in given arr :", i)

'''sum of the even num in the list'''
# arr = [3,8,4,9,6,2,7,5]
# sum=0
# for i in arr:
#     if(i%2==0):
#         sum=sum+i
# print("sum of the even num in given arr :" , sum)

'''Exercises on string::'''


'''1)Display the all char in reverse order using range'''
# s="abc@123$#"
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

'''2)Display the only alphabets from the given string'''
# s="abc@123$#"
# for ch in s:
#     if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
#         print(ch)

'''3)count the alphabets , digits and symbols'''
# s="abc@123$#"
# alphabets=0
# digits=0
# symbols=0
# for ch in s:
#     if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
#         alphabets=alphabets+1
#         #alphabets+=1
#     elif (ch>='0' and ch<='9'):
#         digits=digits+1
#         #digits+=1
#     else:
#         symbols=symbols+1
#         #symbols+=1
# print("alphabets:", alphabets)
# print("digits:", digits)
# print("symbols:", symbols)

'''4)sum of the digits in the given string'''
# s="abc@123$#"
# sum=0
# for i in range(4,7):
#     sum=sum+int(s[i])   # converting str to int
# print("sum of the digits in the given string:", sum)

'''5)check '@' is present in the given string or not'''
# s="abc@123$#"
# if '@' in s:      # membership "in"  ,not in,is, is not operator
#     print("@ is the present in the given string")
# else:
#     print("@ is not present in the given string")




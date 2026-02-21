'''
            Exception(error) Handling

-->Exception is a Runtime error
-->Exception is a Class
-->Exception terminates program execution means while run the code then you will get the doesn't understand the output.

pre-defined exceptions are three :-

1)ValueError(it must the first letters of the V and E should be capital)
2)ZeroDivisionError(it must the first letters of the Z , D and E should be capital)
3)IndexError(it must the first letters of the I and E should be capital)

or 

# 🔹Common Built-in Exceptions : 
# Exception Name :	            Meaning :
# 1) ValueError	                Wrong value
# 2) ZeroDivisionError      	Divide by zero
# 3) IndexError	                Invalid index
# 4) KeyError	                Missing key
# 5) TypeError	                Wrong data type
# 6) FileNotFoundError	        File not found

'''
# ex:

'''1)ValueError :
            ValueError happens when the value(str) is wrong, even though the data type(int) is correct.
ex : 
    int("abc")
This causes ValueError because "abc" is a string (correct type for int() input), but its value cannot be converted to a number.

'''

# (when you run the given below code , when you give the input as integer value then you will definitely get the output as integer)
# (when you run the given below code , when you give the input as integer value as the str (abc) then you will definitely get the output as the ValueError)

# a= int(input("enter a num: "))
# b= int(input("enter a num: "))
# c=a+b
# print(f"sum is = {c}")

'''when you give the input as a string then you will get the error'''
'''the given below is the error after run the above program input as the str value'''
# enter a num: abc
# Traceback (most recent call last):
#   File "c:\Users\kadum\OneDrive\Desktop\Data teach.ai\python\16) normal program.py", line 28, in <module>
#     a= int(input("enter a num: "))
# ValueError: invalid literal for int() with base 10: 'abc'

'''(How can you handle the ValueError execption)???'''
#while you run the code when you give the input is correct then it will give output 
#while you run the code when you give the input is not correct then it will give output as ValueError
#ex : input is int when you give the string as input then it gives the ValueError

'''(ValueError Handling exception)'''
# -->To avoid the error we use try and except block
# -->giving the proper msg to the user

# try block: The try block contains the code that may cause an error.
# except block: is use to handle the exception

# try:          #Here, division by zero may cause an error, so we put it inside try.

#     a= int(input("enter a num: "))
#     b= int(input("enter a num: "))
#     c=a+b
#     print(f"sum is = {c}")
# except ValueError:
#     print("Exception : Invalid Input")

'''
one try Block can have any number of except blocks to handle different types of exceptions(like:ValueError,IndexError,ZeroDivisionError,etc)
'''
'''2) ZeroDivisionException : 
            ZeroDivisionError happens when we try to divide any number by zero.

Ex : 10/0 = get ZeroDivisionError

'''
# try:          #Here, division by zero may cause an error, so we put it inside try.
#     a= int(input("enter a num: "))
#     b= int(input("enter a num: "))
#     c=a/b
#     print(f"div is = {c}")
# except ValueError:            #The except block contains the code that runs only if an error occurs in the try block(ValueError).
#     print("Exception : Invalid Input")
# except ZeroDivisionError:     #except handles the error instead of stopping the program.
#     print("Exception : can't divide by 0 ")

'''

-->Exception is a parent class to all exceptions.
--> We can handle multiple exceptions using single except block
--> Every exception has pre-defined message(msg).

'''
# try:
#     a= int(input("enter a num: "))
#     b= int(input("enter a num: "))
#     c=a/b
#     print(f"div is = {c}")
# except Exception as msg:
#     print(f"Exception : {msg}")


'''3)IndexError : 
            IndexError happens when the index is out of range.

'''
#Ex 1) : 
# nums=[21,21,43,5,42,23,43,46]
# a=nums[5]
# b=nums[18]
# print(a)
# print(b)

#Ex 2) :
# nums=[5,2,0,4,9,0,6,3]
# try:
#     a=int(input("enter a index-1 num: "))
#     b=int(input("enter a index-2 num: "))
    
#     x=nums[a]                #collect the data from the nums
#     y=nums[b]                #collect the data from the nums
#     z=x/y

# except ValueError:
#     print("Exception : Invalid Input")
# except ZeroDivisionError:
#     print("Exception : can't divide by 0 ")
# except IndexError:
#     print("Exception : out of Index(Bound)")


'''
write the all exception in a single except block
'''

# nums=[5,2,8,4,9,0,6,3]
# try:
#     a=int(input("enter a index-1 num: "))
#     b=int(input("enter a index-2 num: "))
    
#     x=nums[a]                #collect the data from the nums
#     y=nums[b]                #collect the data from the nums
#     z=x/y

# except Exception as msg:
#     print(f"Exception : {msg}")


''' 1) Custom Exception handling(InvalidAgeError)'''
# class InvalidAgeError(Exception):           #Custom Exception
#     pass                                    #Custom Exception

# class person:
#     def can_vote(age):
#         if age>=18:
#             print("you can vote")
#         else:
#             raise InvalidAgeError("you can't vote")  #we should Create exception object and raise when problem occurs.
#         return
    
# age = int(input("enter your age: "))

# try:
#     person.can_vote(age)        #we need to handle exception while calling the method
# except InvalidAgeError as msg:      #inside store the msg is the "you can't vote"
#     print(f"Exception : {msg}")     #inside store the msg is the " Exception : you can't vote"

''' 2) Custom Exception handling(LowBalanceError)'''

# class LowBalanceError(Exception):
#     pass

# class account:
#     balance = 4000            
#     def withdraw(amount):
#         if (amount<=account.balance):
#             print(f"collect the cash : {amount}")
#             account.balance = account.balance - amount
#         else:
#             raise LowBalanceError("Low Balance")
#         return
    
# amt=int(input("Enter withdraw the amount: "))
# try:
#     account.withdraw(amt)
# except LowBalanceError as msg:
#     print(f"Exception : {msg}")

# print(f"Final balance is : {account.balance}")


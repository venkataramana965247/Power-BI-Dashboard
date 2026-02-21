'''Oops'''


'''normal function program'''

'''1)static variable'''
# a=10
# def fun():
#     print("fun...")
#     return

# print(f"a val : {a}")   #direct calling is called as static variable
# fun()           

'''2)dynamic variable'''

'''fun program by using the Oops program'''
# class test:
#     a=10          #dynamic variable
#     def fun():
#         print("fun...")
#         return

# res=test.a        #dynamic variable(res) create an object
# print(res)         
# test.fun()         #How calling of fun through the class(class name.fun name())

'''more than one class'''
# class first:
#     a=10
#     def fun():
#         print("first - fun...")
#         return

# class second:
#     a=20
#     def fun():
#         print("second - fun...")
#         return
    
# res1=first.a          #dynamic variable(res1) create an object
# res2=second.a         #dynamic variable(res2) create an object
# print(res1)
# print(res2)
# first.fun()           #How calling of fun through the class(class name.fun name())
# second.fun()          #How calling of fun through the class(class name.fun name())
# second.fun()
# first.fun()

'''different types of functions in the Oops concept'''

'''1) no arguments - no return values'''
'''=>normal fun program'''
# def hello():
#     print("hello all")
#     return
# hello()

# def hi():
#     print("hi this is the ramana")
#     return
# hi()

'''=>using the class(Oops)'''
# class stu:
#     def hello():
#         print("hello all")
#         return
    
# stu.hello()             #How calling of fun through the class(class name.fun name())

# class ram_bro:
#     def hi():
#         print("hi this is the ramana")
#         return
# ram_bro.hi()            #How calling of fun through the class(class name.fun name())


'''2) with arguments - no return values'''
# class do:
#     def add(a,b):
#         print(f"sum = {a+b}")
#         return
#     def sub(a,b):
#         print(f"difference = {a-b}")
#         return
# do.add(10,20)         #How calling of fun through the class(class name.fun name())
# do.sub(20,10)         #How calling of fun through the class(class name.fun name())

'''3) with args - with return values(blind remember this::[when you wrote the 'return' value then you should take one variable])'''
# class check:
#     def even(n):
#         if n%2==0:
#             return "Even"
#         else:
#             return "it is not even num"
# res=check.even(10)      #when you wrote the any data in return then you need to store in temp var
# print(res)


'''Extra example'''
'''write the program for the tables using class'''
# class tables:
#     def table(n):
#         for i in range(1,11):
#             print(f"{n} * {i} = {n*i}")
#         return
# tables.table(13)


'''write the program for the big of the num to take the three inputs'''
# class find:
#     def big(a,b,c):
#         if a>b and a>c:
#             return f"{a} is the big num"      #when you wrote the any data in return then you need to store in temp var
#         elif b>c:
#             return f"{b} is the big num"
#         else:
#             return f"{c} is the big num"      #when you wrote the any data in return then you need to store in temp var
# res=find.big(50,60,30)            #this is the temp var
# print(res)

'''write the code for the check vowel(a,e,i,o,u) or not'''
# class check:
#     def vowel(ch):
#         if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#             return f"{ch} is the vowel"
#         else:
#             return f"{ch} is not a vowel"
# res=check.vowel('x')
# print(res)

'''1) static method :
            Defining a method inside the class we call using class- name
            define method without 'self'.
'''
# ex:
class test:
    def fun():
        print("fun...")
        return
    
test.fun()  # direct call the fun

'''2) dynamic method(self) :
            Defining a method using 'self' variable as a first argument
            we call using object - address
'''
# ex 1): 
# class test:
#     def fun(self):
#         print("fun...")
#         return

# obj = test()    #create obj
# obj.fun()     # call the fun using obj

# ex 2):
# class person:
#     def vote(self,age):
#         if age>=18:
#             print("eligible for vote")
#         else:
#             print("not eligible for vote")
#         return

# class check:
#     def prime(self,n):        #self is a keyword,dynamic or instance method
#         count=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 count=count+1
#         if count==2:
#             print("prime num")
#         else:
#             print("not prime num")
#         return
    
# p=person()
# p.vote(11)

# c=check()
# c.prime(2)


'''best example of how to understand the static method and dynamic method'''
# class first:
#     def abc():              #static method
#         print("first - abc")
#         return
#     def xyz(self):          #dynamic method
#         print(self)
#         print("first - xyz")
#         return

# class second:
#     def abc():              #static method
#         print("second - abc")
#         return
#     def xyz(self):          #dynamic method
#         print(self)
#         print("second - xyz")
#         return
    
# first.abc()     # static method call
# res1=first()    #dynamic var creation
# res1.xyz()      #call of dynamic mathod

# second.abc()    # static method call
# res2=second()   #dynamic var creation
# res2.xyz()      #call of dynamic mathod


'''3) constructor :define a method using __init__(self) it executes automatically in object creation'''

# ex :
# class test:
#     def abc():
#         print("static method")
#         return
#     def xyz(self):
#         print("dynamic method")
#         return
#     def __init__(self):
#         print("constructor method")
#         return
    
# test.abc()      #static method call
# res=test()      #constructor method & object creations done
# res.xyz()       #dynamic method call

'''1) ex :'''
# class employee:                 #class like a blueprint & “I am creating a blueprint called employee” & You are naming a box of rules as employee.
#     def __init__(self,num,name,salary):   #stores data  #This runs automatically(245,246,247) when we create a new employee.Stores this function inside the employee class
#         self.num=num        #Left side 👉 where to store & Right side 👉 value coming in    #e1.num = 101
#         self.name=name                                                                       #e1.name = "ram"
#         self.salary=salary                                                                   #e1.salary = 100000
#         return                      #return means Ends the function
    
#     def details(self):              #Defines another function to show employee data
#         # print(self.num,self.name,self.salary)
#         print(f"{self.num},{self.name},{self.salary}")
#         return                      #return means Ends the function   

# e1=employee(101,"ram",100000)           #Creating employee objects
# e2=employee(102,"chaithu",200000)       #Creating employee objects
# e3=employee(103, "kiran", 300000)       #Creating employee objects

# e1.details()
# '''Explanation of the (e1.details)'''
#     #You are creating one employee
# '''Execution process of the (e1.details)'''
#     #Python does 4 steps internally
#     #1)Creates an empty object → e1
#     #2)Automatically calls:   __init__(e1, 101, "ram", 100000)
#     #3)Now execute inside __init__ line by line
#    #python
#         #self.num = num
#    #Becomes :
#         #e1.num = 101

#     #python
#         #self.name = name
#     #becomes :
#         #e1.name = "ram"

#     #python
#         #self.salary = salary
#     #Becomes :
#         #e1.salary = 100000

# e2.details()    #same execution process as same as above line #Calling details() method
# e3.details()    #same execution process as same as above line #Calling details() method


'''2) ex :'''

# class student:
#     def __init__(self,name,course,fee):
#         self.name=name
#         self.course=course
#         self.fee=fee
#         return
    
#     def details(self):
#         print(f"{self.name},{self.course},{self.fee}")
#         return

# s1=student("ram","python",1000)        #object creation
# s2=student("ravi", "java", 2000)        #object creation
# s3=student("kiran", "c", 3000)          #object creation

# s1.details()                            #method call through the object
# s2.details()                            #method call through the object
# s3.details()                            #method call through the object



'''3) ex :'''
# class account:
#     def __init__(self,num,balance):
#         self.num=num
#         self.balance=balance
#         return

#     def details(self):
#         print(f"{self.num},{self.balance}")
#         return

#     def get_balance(self):
#         return self.balance

# a1=account(123, 1000)
# a2=account(456, 2000)

# a1.details()
# a2.details()

# print(f"a1 balance is :{a1.get_balance()}")
# print(f"a2 balance is :{a2.get_balance()}")


'''4) ex: '''

# class account:                          #The class account is like a blueprint of a bank account.
#     def __init__(self,balance):         #__init__ runs automatically when we create an object
#         self.balance=balance            #balancen = 5000
#         return

#     def get_balance(self):          #Returns the current balance
#         return self.balance         #If balance is 5000, this returns 5000

#     def deposit(self,amount):               #Deposit = 3000 or amount = 3000
#         self.balance = self.balance+amount     #Adds money to balance & Balance = 5000,Deposit = 3000,New balance = 5000 + 3000 = 8000
#         return

#     def withdraw(self,amount):          #Checks if enough money is available #amount = 6500
#         if amount<=self.balance:      #ex : 6500<=8000  #If yes → withdraw money & If no → show error & Balance = 8000,Withdraw = 6500 ,New balance = 8000 - 6500 = 1500 
#             print(f"collect cash : {amount}")  #collect cash : 6500
#             self.balance=self.balance-amount     #self.balance = 8000-6500=1500
#         else:
#             print("error : low balance")
#         return

# acc = account(5000)
# print(f"balance is account :{acc.get_balance()}")

# acc.deposit(3000)
# print(f"after deposit, balance is : {acc.get_balance()}")

# acc.withdraw(6500)
# print(f"after withdraw, balance is : {acc.get_balance()}")


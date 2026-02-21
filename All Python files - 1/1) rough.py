'''the big number among two numbers'''

# a=int(input("Enter a number: "))
# b=int(input("Enter b number: "))
# if (a>b):
#     print(f"the big num is the :{a} ")
# else:
#     print(f"the big num is the :{b} ")

'''if-elif-else statement to find of the Triangle,square,pentagon,other shape'''

# side =int(input("Enter the side value: "))
# if (side==3):
#     print("Triangle")
# elif(side==4):
#     print("square")
# elif(side==5):
#     print("Pentagon")
# else:
#     print("other shape")

'''nested if: writing if inside another if '''
# n=int(input("Enter a number: "))
# if (n>=0):
#     if (n%2==0):
#         print(f"{n} it is a even number")
#     else:
#         print(f"{n} it is a odd number")
# else:
#     print("the given num is the negative number")

'''Check the given num is the single digit,two,three,four,and other digit'''

# n=int(input("Enter the num: "))
# if (n>=0 and n<=9):
#     print("single digit")
# elif(n>=10 and n<=99):
#     print("two digit")
# elif(n>=100 and n<=999):
#     print("three digit")
# else:
#     print("other digit")

'''biggest of the four num'''
# a=int(input("Enter a num: "))
# b=int(input("Enter b num: "))
# c=int(input("Enter c num: "))
# d=int(input("Enter d num: "))

# if (a!=b!=c!=d):
#     if (a>=b and a>=c and a>=d):
#         print("a is the biggest")
#     elif(b>=c and b>=d):
#         print("b is the biggest")
#     elif(c>=d):
#         print("c is the biggest")
#     else:
#         print("d is the biggest")
# else:
#     print("please enter different numbers")


#      0  1  2   3  4  5
# list=[10,20,30,40,30,40]
#      -6 -5 -4 -3 -2 -1
# list.append(4)
# print(list)

# list.insert(3,200)
# print(f"this is using by the insert method:" , list)

# list.extend([1101,121,1032,12])
# print("this is using by the extend method:" ,list)

# list.sort()
# print(list)

# list.pop(3)
# print(list)

# list.count(30)
# for i in list[2:5:2]:
#     print(i)

# print(list.count(30))

# a=(10,20,30,40,50)
# print(min(a))
# print(max(a))
# print(sum(a))
# print(len(a))

'''normal program of the find the grater than 5 in the given list'''
# nums = [3,2,5,8,6,9,4,7]
# res=[]
# for i in nums:
#     if i>5:
#         res.append(i)  
# print(res)


# res =[i for i in nums if i>5]
# print(res)


'''normal program of find given list of only even nums'''
# nums = [3,2,5,8,6,9,4,7]
# res=[]
# for i in nums:
#     if i%2==0:
#         res.append(i)
# print(res)

# nums = [3,2,5,8,6,9,4,7]
# res=[i for i in nums if i%2==0]
# print(res)

'''normal program string conversion lower cases to upper cases on a given list'''
# words=["java","python","react","c++"]
# res=[]
# for i in words:
#     res.append(i.upper())
# print(res)

# words=["java","python","react","c++"]
# res=[x.upper() for x in words]
# print(res)

'''normal functions'''
# def add(a,b):
#     return a+b
# res=add(10,20)
# print(f"sum = {res}")

'''lambda fun'''
# add=lambda a,b:a+b
# res=add(10,50)
# print(res)

# nums=[3,7,2,8,4,5]
# res=list(map(lambda x :x+x ,nums))
# print(res)

# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# res=fact(5)
# print(res)

# nums=[3,7,4,8,5,2,9,6]
# res=list(map(lambda x:x**2,filter(lambda x: x%2==0,nums)))
# print(res)

# class find:
#     def big(a,b,c):
#         if (a>b and a>c):
#             return f"{a} is the big num"
#         elif (b>c):
#             return
#         else:
#             return f"{c} is the big num"
# res=find.big(10,20,30)
# print(res)


# class check:
#     def vowel(ch):
#         if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#             return f"{ch} is the vowel"
#         else:
#             return f"{ch} is not a vowel"
# res=check.vowel('x')
# print(res)


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


# class person:
#     def vote(self,age):
#         if age>=18:
#             print("eligible for vote")
#         else:
#             print("not eligible for vote")
#         return

# class check:
#     def prime(self,n):
#         count=0
#         for i in range(1,n+1):
#             if n%i==0:
#                 count=count+1
#         if count==2:
#             print("prime")
#         else:
#             print("not prime")
#         return
    
# p=person()
# p.vote(20)

# c=check()
# c.prime(5)


# class bank_account:
#     def __init__(self,acc_num,acc_name,balance):
#         self.acc_num=acc_num
#         self.acc_name=acc_name
#         self.balance=balance
#         return
    
#     def get_balance(self):
#         return self.balance
    
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         return
    
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance=self.balance-amount
#         else:
#             print("insufficient balance")

# acc=bank_account(101, "ram", 10000)
# print(f"balance before add deposit acc is the : {acc.get_balance()}")

# acc.deposit(5000)
# print(f"balance after add of deposit acc : {acc.get_balance()}")

# acc.withdraw(1)
# print(f"after withdraw, balance is : {acc.get_balance()}")


# class s1:
#     def m1():
#         print("yes this is the first print")
#         return
    
#     def m2():
#         print("yes this is the second print")
#         return
    
# s1.m1()
# s1.m2()
# try:
#     a= int(input("enter a num: "))
#     b= int(input("enter a num: "))
#     c=a+b
#     print(f"sum is = {c}")
# except ValueError:
#     print("Exception : Invalid Input")


# # try:
# a= int(input("enter a num: "))
# b= int(input("enter a num: "))
# c=a/b
# print(f"div is = {c}")
# # except ValueError:
# #     print("Exception : Invalid Input")
# # except ZeroDivisionError:
# #     print("Exception : can't divide by 0 ")


# try:
#     a= int(input("enter a num: "))
#     b= int(input("enter a num: "))
#     c=a/b
#     print(f"div is = {c}")
# except Exception as msg:
#     print(f"Exception : {msg}")

# try:
#     a=int(input("enter the num : "))
#     b=int(input("enter the num : "))
#     c=a/b
#     print(f"sum of the a & b is the = {c}")
# except ValueError:
#     print(f"Exception : Invalid input")
# except ZeroDivisionError:
#     print(f"Exception : can't div by 0 ")


# nums=[21,21,43,5,42,23,43,46]
# a=nums[5]
# b=nums[18]
# print(a)
# print(b)

# file = open("input.txt",mode="r")
# print("File Opened")

# try:
#     file = open("input.txt", mode="r")
#     print("File Opened...")

#     data = file.read()
#     print(data)

#     file.close()
#     print("File Closed...")

# except FileNotFoundError:
#     print("Exception : File Not Found")


# try:
#     src = open("input.txt", mode="r")
#     dest=open("output.txt",mode="w")        #new file creation
#     print("file are ready...")

#     for ch in src:
#         dest.write(ch)
#     print("Data Copied...")

#     src.close()
#     dest.close()
#     print("file closed...")


# except FileNotFoundError:
#     print("Exception : File Not Found")


'''
reading CSV file
CSV : Comma Separated Values(Records)
        101, Amar, 5000
        looking like Excel Sheet

'''

# import csv

# try:
#     file = open("data.csv",mode="r")
#     table = csv.reader(file)
#     print("CSV file opened")

#     for record in table:
#         print(record)

#     file.close()
#     print("file closed")

# except FileNotFoundError:
#     print("Exception : File not found")

# try:
#     # file = open("input",mode="r")
#     file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt",mode="r")
#     print("File Opened")

# except FileNotFoundError:
#     print("Exception : File Not Found")

# a=int(input("Enter first num : "))
# b=int(input("Enter second num : "))
# print(f"sum = {a+b}")

# ch = input("Enter a character : ")
# if ch.isalpha():
#     print("it is a alphabet")
# else:
#     print("it is not alphabets")

# a=int(input("Enter the first num : "))
# b=int(input("Enter the second num : "))
# c=int(input("Enter the third num : "))
# if (a>b and a>c):
#     print(f" a is the big num : {a}")
# elif (b>c):
#     print(f"b is the big num : {b}")
# else:
#     print(f"c is the big num : {c}")


# n=int(input("Enter the num : "))
# count=0
# for i in range(1,n+1):
#     if(n%i==0):
#         count+=1
# if (count==2):
#     print(f"{n} is prime")
# else:
#     print(f"{n} is not a prime num")

# n=[1,2,3,4]
# res=list(map(lambda x:x*x ,n))
# print(res)

# words=["Apple","Ball","Cat","Dog","Banana"]
# res=list(filter(lambda x: len(x) >=5 ,words))  #using built-in functions len
# print(res)


# squares=lambda x:x*x
# res=squares(7)
# print(res)

# class employee():
#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
#     def details(self):
#         print(self.id,self.name,self.salary)

# e1=employee(1,"K.RAMANA",50000)
# e2=employee(2,"K.RAM",35000)
# e3=employee(3,"K.SITHA",60000)


# e1.details()
# e2.details()
# e3.details()

# try:
#     a=int(input("Enter the first num : "))
#     b=int(input("Enter the second num : "))
#     c=a/b
# except ZeroDivisionError:
#     print(f"Exception : invalid input ")
# except ValueError:
#     print(f"Exception : wrong value ")
# except IndexError:
#     print(f"Exception : Invalid index form ")



# try:
#     a=int(input("Enter the first num : "))
#     b=int(input("Enter the second num : "))
#     c=a/b
# except Exception as work:
#     print(f"Exception occur due to the : {work}")

# import csv      #i want to work with csv files

# file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt","r") #open the csv file and "r" means read mode
# data=csv.reader(file)       #create csv data into the rows and each row becomes list

# for row in data:        #reads one row at a time and print all records
#     print(row)
# # print(file.read())
# # print(data)
# file.close()            #good prictice to close file


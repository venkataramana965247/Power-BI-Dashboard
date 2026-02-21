'''

File Handling :

---> file handling means Creating,opening,reading,writing and closing files using python.
---> files help us to store data permanently.

Types of Files : 
1)Text files ---> .txt , .csv,  .log
2)Binary files ---> .jpg,  .mp3,  .pdf,  .exe

'''

'''Basic Steps in file Handling'''
# 1) Open the file
# 2) perform operation (read,write,append)
# 3) close the file

# open() Function :
# syntax of the open() fun :
# file = open("filename","mode")

'''
File Modes :

| Mode   | Meaning           |
| ------ | ----------------- |
|  "r"   | Read              |
|  "w"   | Write (overwrite) |
|  "a"   | Append            |
|  "x"   | Create new file   |
|  "rb"  | Read binary       |
|  "wb"  | Write binary      |
|  "r+"  | Read + Write      |
|  "w+"  | Write + Read      |

'''

# ex : 

# 1️⃣ Create & Write to a File :

# f = open("demo.txt", "w")           # "w" → creates file if not exists
# f.write("Hello Python")             # write() → writes data 
# f.write("File handling example")    # write() → writes data
# f.write("hey hi this is the ramana....!")
# f.write(".....HI......")

# f.close()                          # close() → saves & closes file

# 2️⃣ Read a File :
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()

# 3️⃣ Append Data (Add without deleting)
# f = open("demo.txt", "a")         #"a" =append keeps old data and adds new data at the end.
# f.write("\nThis line is added")
# f.close()


# import os

# if os.path.exists("demo.txt"):
#     print("File exists")
# else:
#     print("File not found")


# file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt",mode="r")
# file = open("input.txt",mode="r")

# print("file is opended")

# file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt","r")
# data=file.read()
# # print(file.read())
# print(data)
# file.close()

# ex 1) : 

# try:
#     file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt",mode="r")
#     #file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt","r")
#     print("File Opened")

# except FileNotFoundError:
#     print("Exception : File Not Found")

# ex 2) : 
# try:
#     file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt", mode="r")
#     print("File Opened...")

#     data = file.read()
#     print(data)

#     file.close()
#     print("File Closed...")

# except FileNotFoundError:
#     print("Exception : File Not Found")


# ex 3) : 
# try:
#     src = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt", mode="r")
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
CSV :   Comma Separated Values(Records)
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


# import csv      #i want to work with csv files

# file = open("C:\\Users\\kadum\\OneDrive\\Desktop\\input.txt","r") #open the csv file and "r" means read mode
# data=csv.reader(file)       #create csv data into the rows and each row becomes list

# for row in data:        #reads one row at a time and print all records
#     print(row)
# # print(file.read())
# # print(data)
# file.close()            #good prictice to close file
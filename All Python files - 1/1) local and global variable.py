'''1) 🔹 Local Access (Local Variable) :

--> A local variable is a variable that is created inside a function and can be accessed only inside that function.
--> Local access means the variable works only inside the function.

'''

# Ex :
# def my_func():
#     x = 10   # local variable
#     print(x)

# my_func()
# # print(x)   ❌ Error

'''Explanation : '''

# 1) x is created inside my_func()
# 2) It works only inside the function
# 3) Outside the function → ❌ NameError


'''2) 🔹 Global Access (Global Variable)

--> A global variable is a variable that is created outside a function and can be accessed anywhere in the program.
--> Global access means the variable works everywhere.

'''

# Ex :
# y = 20   # global variable

# def my_func():
#     print(y)

# my_func()
# print(y)       #✔️ y works both inside and outside the function

# 🔹 Important rule (Very important!)
# ❗ You can read a global variable inside a function
# ❗ But you cannot modify it without global keyword

# ❌ Wrong:

# x = 5
# def change():
#     x = x + 1   # error

# change()

# ✅ Correct (using global):

# x = 5

# def change():
#     global x
#     x = x + 1

# change()
# print(x)   # 6



# 🔹 Local vs Global (Easy table) :

# | Feature                | Local                     | Global               |
# | ---------------------- | ------------------------- | -------------------- |
# | Defined                | Inside function           | Outside function     |
# | Access                 | Only inside function      | Everywhere           |
# | Lifetime               | During function execution | Whole program        |
# | Modify inside function | ✔️                        | ❌ (without `global`) |


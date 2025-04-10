print("It Worked!")

x = None

example = "I am a string" # the example variable has been assigned the string value of I am a string
a = 3 # the a variable has been assigned the integer value 3
b = 4.0 # the b variable is now holding the float value 4.0
c = True # the c variable is now holding the Boolean value True
d = False # the d variable is now holding the Boolean value False
e = 'Hey!' # the e variable is now holding the string value hey!
f = None # the f variable is now holding the None value type
age = 32 # the age variable has been assigned the integer value of 32
name = "insert your name here!" # the name variable has been assigned the string value of "insert your name here!"
instrument = "insert your instrument here!" # the instrument variable has been assigned the string value insert your instrument here1!

'''
comment stuff (kinda)
'''



#Problem 1
# name = input("Please enter your name: ")

# age = input("Please enter your age: ")

# print(name, type(name))
# print(int(age), type(age))

#Problem 2
# num1 = int(input("First number: "))
# num2 = int(input("Second number: "))

# if num1 == num2:
#     print("They are equal!")
# elif num1 > num2:
#     print("First number bigger bro")
# elif num2 > num1:
#     print("Second number way bigger bro")
# else:
#     print("what")


#Problem 5
x = input("Please enter your full name: ")
while " " in x:
    x = x.replace(" ", "")
print(len(x))

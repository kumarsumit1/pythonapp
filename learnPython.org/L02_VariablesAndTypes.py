'''
Python is completely object oriented, and not "statically typed". 
You do not need to declare variables before using them, or declare their type. 
Every variable in Python is an object.
'''

#Numbers

'''
Python supports two types of numbers - integers and floating point numbers.
(It also supports complex numbers but not explained here )
'''

myInt=9
print("The type of variable is ::",type(myInt),myInt)

print("The integer type is ", type(myInt) is int)

if isinstance(myInt, int):
    print("It is an int")


#Float
'''
To define float one can use decimal (.) or float() function
'''

myFloat=8.0
anotherFloat=float(8)

if isinstance(myFloat,float) and isinstance(anotherFloat,float) and myFloat==anotherFloat :
    print("Both the floats are equal")    
    
#String
'''
Strings are defined either with a single quote or a double quotes.
Double quotes helps when the string itself has single quotes as in apostrophe
'''
myString='myStrng'
anotherString="myString"

print("the type of both vars are %s %s" %(type(myString),type(anotherString)))
    

#Simple operators can be executed on numbers and strings:
one=1
two=2
three=one+two

print("the summation is %d " % three)    

hello="hello"
world="world"
helloWorld=hello+" "+world 
print(helloWorld)

#Assignments can be done on more than one variable "simultaneously"

three,four=3,4

print("the values of var three is %d and four is %d" % (three,four))


    
    
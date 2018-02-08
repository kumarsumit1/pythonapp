'''
Python uses C-style string formatting to create new, formatted strings. 
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
 together with a format string, which contains normal text together with "argument specifiers",
  special symbols like "%s" and "%d".
'''

name="john"
age=29
print("The name is %s and my age is %d!  " % (name,age))


#Any object which is not a string can be formatted using the %s operator as well. 
#The string which returns from the "repr" method of that object is formatted as the string.

myList=[1,2,3]
print("The list is %s " % myList)

'''
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''

#Exercise : Print --> Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello"

print("%s %s %s. Your current balance is $%.2f." % (format_string,data[0],data[1],data[2]))

#How to merge or add element in tuple
#st=(format_string)+data
#print(st)

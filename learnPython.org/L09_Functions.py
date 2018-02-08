#Block keywords you already know are "if", "for", and "while".
#Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. 
#the block head is of the following format: block_keyword block_name(argument1,argument2, ...) 


def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print("The sum of two numbers are %d " % x)
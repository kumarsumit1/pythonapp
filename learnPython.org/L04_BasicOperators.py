#Arithmetic Operators

myOp=1+2*3/4.0
print("the output is ",myOp)

#Using two multiplication symbols makes a power relationship.

twoSqr=2 ** 2
print("The square of two is",twoSqr)

twoQube=2 ** 3
print("The cube of 2 is",twoQube)

#Python also supports multiplying strings to form a string with a repeating sequence:

multipleHello="hello " * 4
print(multipleHello)

#Using Operators with Lists
## Lists can be joined with the addition operators:
even_no=[2,4,6,8]
odd_no=[1,3,5,7]
numbs=even_no+odd_no
print(numbs)

## Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator

multipleList= even_no * 3

print(multipleList)


#Excercise
'''
The target of this exercise is to create two lists called x_list and y_list, 
which contain 10 instances of the variables x and y, respectively.
 You are also required to create a list called big_list, which contains the
  variables x and y, 10 times each, by concatenating the two lists you have created.
'''

x= object()
y= object()

x_list= [x] * 10
y_list= [y] * 10
big_list=x_list+y_list


print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
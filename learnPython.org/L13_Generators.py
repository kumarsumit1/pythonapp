#Generators

#Generators are iterators, but you can only iterate over them once. 
# It’s because they do not store all the values in memory, 
# they generate the values on the fly:

mygenerator = (x*x for x in range(3))
for i in mygenerator:
     print(i)

#It is just the same except you used () instead of [] as in list comprehension. 
# BUT, you can not perform for i in mygenerator a 
# second time since generators can only be used once: 
# they calculate 0, then forget about it and calculate 1,
#  and end calculating 4, one by one.


# A Python program to generate squares from 1 
# to 100 using yield and therefore generator 
  
# An infinite generator function that prints 
# next square number. It starts with 1 
def nextSquare(): 
    i = 1; 
  
    # An Infinite loop to generate squares  
    while True: 
        yield i*i                 
        i += 1  # Next execution resumes  
                # from this point      
  
# Driver code to test above generator  
# function 
for num in nextSquare(): 
    if num > 100: 
         break    
    print(num) 

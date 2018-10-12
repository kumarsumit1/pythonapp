
print("Hello World")


#https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
print(sum(range(1,10)))

nums=[1,2,3,4,5,6,7,8,9]
x=0
#for n in nums: x=x+n:
 # print(x)

#------------------
a =4
b=7
x=lambda: a if 1 else b 
lambda x: 'big' if x > 100 else 'small'
print(x())

#-----------------
def x():
    print("x")
    return True

def y():
    print("y")
    return False

def z():
    if x() or y() : print("11")
    if x() and y() : print( "12")
    else : print("Z")
    
z()    

#-----------
class class1:
    a=1
    
    def func1():
        a=2
        class1.a+=1
        a +=1
        print(class1.a)
        print(a)
        
        
myclass= class1

class1.func1()

class1.func1()        


#-----------------

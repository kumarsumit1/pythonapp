#List
'''
Lists are very similar to arrays. They can contain any type of variable, 
and they can contain as many variables as you wish. Lists can also be 
iterated over in a very simple manner.
'''

myList=[1,"two",3,4.0,'five']

print(myList)

anotherList=[]
anotherList.append(6)
anotherList.append('seven')
anotherList.append(7.0)
anotherList.append("eight")

print(anotherList[2])

for item in anotherList:
    print("the elements are %s " % item)
    
    
# sorted
lst=[4,3,1,6,7]
 
print(sorted(lst))   

print(lst)


######################## TUPLES ######################################

#To put it lightly, tuples are lists which can't be edited. Once you create a tuple, you cannot edit it, it is immutable.


point = (3,7)

print(type(point))

print(point[0])

# the below line gives an error "'tuple' object does not support item assignment" as it is immutable.
'''
point[0]= 4
'''

print(lst)

lst[4]= "newItem"

print(lst)



#However note that to add a new item that increases the size of list one will have to use append method.

lst.append("adding_an_element")

print(lst)


#However adding an element at a new position is not allowed
#'type' object does not support item assignment
'''
list[6]="extraLength"
'''

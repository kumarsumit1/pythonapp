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
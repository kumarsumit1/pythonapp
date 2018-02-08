#A dictionary works with keys and values 
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

#another way to implement Dictionary is

phonebook1 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook1)


#Iterating over dictionaries

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
    
#Removing a value one can use del or pop

del phonebook["John"]
print(phonebook)

phonebook1.pop("John")
print(phonebook1)
    
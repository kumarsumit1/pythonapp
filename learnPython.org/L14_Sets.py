#Sets are lists with no duplicate entries

aset=set("my name is Eric and Eric is my name".split())

print(aset)


a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended both events, you may use the "intersection" method

print(a.intersection(b))
print(b.intersection(a))

# To find out which members attended only one of the events, use the "symmetric_difference" method

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# To find out which members attended only one event and not the other, use the "difference" method

print(a.difference(b))
print(b.difference(a))

# To receive a list of all participants, use the "union" method:

print(a.union(b))


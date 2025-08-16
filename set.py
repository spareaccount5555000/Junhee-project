#sample_list = [1,1,2,2,3,3]
#sample_set = set(sample_list)
#print(sample_set)
#print(sample_set[2])

#if 4 in sample_set:
    #print("yes")
#else:
    #print("no")

#myset = set([])
#myset.add(4)
#myset.add(3)
#myset.add(2)
#myset.add(1)

#print(myset)

#myset.remove(2)
#myset.remove(5)
#myset.discard(5)

#print(myset)


a = {1,2,3,4,5}
b = {4,5,6,7,8}

#a.union(b) = {1,2,3,4,5,6,7,8}

#a.intersection(b) = {4,5}

#c = {1,2,3}
#d = {4,5,6}

#c.intersection(d) = None

#a-b = {1,2,3}
#b-a = {6,7,8}

#a symDiff b = {1,2,3,6,7,8}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a-b)

print(a.symmetric_difference(b))
print(a^b)



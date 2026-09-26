conjunto = {1,2,3,4,5,6,7,6}

print(conjunto)

c1 = {1,2,3,4,5,6}
c2 = {4,5,6,7,8,9}

c3 = set([8,9,2,1,3])

print(c1)
print(c2)
print(c3)

c4 = c1.union(c2)
#c4 = c1 | c2

print(c4)

c5 = c1.intersection(c2)
# c5 = c1 & c2

print(c5)

c6 = c1-c2

print(c6)




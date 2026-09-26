from collections import Counter

c1 = Counter(a=3, b=2)
c2 = Counter(a=1, b=3, c=1)

print(c1)
print(c2)
# c1 + c2 = Counter({'b': 5, 'a': 4, 'c': 1})
c3 = c1+c2
print(f'c1 + c2 = {c3}')

# c1 - c2 = Counter({'a': 2})
c4 = c1-c2
print(f'c1 - c2 = {c4}')





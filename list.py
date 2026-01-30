a,b,c = [1,2,3]
l1 = a,b,c
# data = l1.remove(30)
l1 = list(l1)
l1[2] = 30

l1 = [_*_ for _ in l1]

print(l1)
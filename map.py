import functools 
l1 = [1,2,3,4,5]

def f1(x):
    if(x %2 == 0):
        return x*x
    return x**4

def fact(a,b):
    return a*b

# ans = map(f1,l1)
# for val in ans:
#     print(val,end=' ')

# ans = functools.reduce(lambda a,b : a*b, l1)
ans = list(filter(lambda a : (a%2 == 0), l1))

print(ans)
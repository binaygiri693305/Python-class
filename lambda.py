# add = (lambda a,b:a+b)(int(input("Enter a number : ")),int(input("Enter a number : ")))
# print(add)

fact = lambda n: n * fact(n-1) if n>0 else 1

print(fact(7))
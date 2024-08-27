def max_value(a,b,c):
    if a>b and a>c:
        return a
    if b>c and b>a:
        return b
    if c>a and c>b:
        return c

a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))

print(max_value(a,b,c))
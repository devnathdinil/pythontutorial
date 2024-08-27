def is_even(number):
    return number % 2==0

z=int(input("enter the number"))
if is_even(z):
    print(f"{z} is even")
else:
    print("false")


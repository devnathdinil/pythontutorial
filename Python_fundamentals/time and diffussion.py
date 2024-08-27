import time
n=int(input("enter the time: "))
for i in range(n,0,-1):
    print(i)
    time.sleep(1)

y=input("cut red or blue? ")
if y=="red":
    print("bomb explodes")
elif y=="blue":
    print("bomb diffused ")



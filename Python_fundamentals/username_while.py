username="devnath"
password="1234567"
attempts=3
while(attempts>0):
    input_username=input("Enter your username")
    input_password=input("enter your password")
    if(input_username==username and password==input_password):
        print("entry successfull")
        break
    else:
       attempts = attempts-1
else:
    print("maximum attempt reached get lost sucker_Alan")



username="devnath"
password="1234567"
attempts=3
for attempts in range(3,0,-1):
    input_username=input("Enter your username:")
    input_password=input("enter your password:")
    if(input_username==username and password==input_password):
        print("entry successfull")
        break
    else:
       attempts = attempts-1
       print(f"you have{attempts}left")
else:
    print("maximum attempt reached get lost sucker_Alan")
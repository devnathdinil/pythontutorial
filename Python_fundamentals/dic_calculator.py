def calc_operator(a,b):
    while True:
        print("\n Calculator:")
        print("1. ADDITION")
        print("2. SUBSTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("5. EXIT")
        
        choice = input("Choose an option: ")

        if choice == "1":
            print("sum=",a+b)
        elif choice=="2":
            print("difference=",a-b)
        elif choice=="3":
            print("product=",a*b)
        elif choice=="4":
            print("division=",a/b)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

a=int(input("Enter the 1st numbers: "))
b=int(input("Enter the 2nd numbers: "))
print(calc_operator(a,b))

        

        
        
        
    
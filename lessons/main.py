import calculations
import greetings
import menu

def main():
    greetings.say_hello("User")
    menu.display_Menu()

    while True:
        choice=input("Enter your choice: ")

        if choice=="1":
            name=input("Enter your name: ")
            greetings.say_hello(name)

        elif choice=="2": 
            num1=int(input("Enter the first number: "))
            num2=int(input("Enter the second number: "))

            operation=input("Enter the operation(+,-,*,?): ")
            if operation == "+":
                print("Result: ",calculations.add(num1,num2))

            elif operation == "-":
                print("Result: ",calculations.subtract(num1,num2))

            elif operation == "*":
                print("Result: ",calculations.multiply(num1,num2))

            elif operation == "/":
                try:
                    print("Result: ",calculations.divide(num1,num2))
                except ValueError as e:
                    print(e)
            else:
                print("invalid operation,please choose + ,- ,* ,/ ")
        
        elif choice == "3":
            greetings.say_Goodbye("user")
            break
        
        else:
            print("invalid choice.please choose 1,2 or 3")

if __name__  == "__main__":
    main()

    
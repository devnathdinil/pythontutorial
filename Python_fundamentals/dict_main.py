Contact_list ={
"Devnath":8921279004,
"Alan":9048377149,
"Greeshma":9447180419
}

while True:
    x=input("enter what you have to do: ")


    if(x=="update"):
    
        Contact_list["Greeshma"] = 995365795
        print(Contact_list)

    elif(x=="delete"):
        if("Greeshma" in Contact_list):
            print(Contact_list)
            Contact_list.pop("Greeshma")
            print(Contact_list)
        else:
            print("Contact not found")

    elif(x=="add"):
        Contact_list["Jackson"] = 775367890
        print(Contact_list)

    elif(x=="view all contacts"):
        Contact_list.items()
        print(Contact_list)

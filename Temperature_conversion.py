def convert_temperature(temp,convert_to="C"):
    if convert_to == "F":
        return(temp-32)*5/9
    elif convert_to == "C":
        return (temp*9/5) + 32

print(convert_temperature(100,"F"))
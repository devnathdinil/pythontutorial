def get_factors(num):
    list_of_factors=[]
    if num < 1:
        return list_of_factors
    else:
        for i in range(1,num+1):
            if(num % i==0):
                list_of_factors.append(i)
        return list_of_factors
z=int(input("enter the num: "))  
print(get_factors(z))
    
    
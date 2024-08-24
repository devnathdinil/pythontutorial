def print_digit_sum(n):
    
    total=0
    n=abs(n)
    for i in str(n):
        total=total+int(i)
    return total

print(print_digit_sum(-200))
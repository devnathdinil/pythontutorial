def add(a,b):
    """Return the sum of a and b"""
    return a+b

def subtract(a,b):
    """Return thr product of a and b"""
    return a-b

def multiply(a,b):
    """Return thr product of a and b"""
    return a*b

def divide(a,b):
    """Return thr divisor of a and b"""
    if b==0:
        raise ValueError("cannot divide by zero")
    return a/b
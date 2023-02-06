def performSub(x, y):
    return x - y 

def performMult(x,y):
    return x * y

def performDiv(x,y):
    if(y == 0):
        return ZeroDivisionError
    return x / y
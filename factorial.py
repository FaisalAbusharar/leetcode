def factorial(n):
    number = 1
    for x in range(1,n+1):
        number *= x
    return(number)
    
    
print(factorial(5))
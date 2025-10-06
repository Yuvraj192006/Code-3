def isprime(a):
    if a<=1:
        return False
    elif a>1 and a<=3:
        return True
    elif a%2==0:
        return False
    for i in range(3,int(a**0.5)+1):
         if a%i==0:
            return False
    return True

def isarmstrong(a):
    b=0
    x=str(a)
    n=len(x)
    for i in x:
        i=int(i)**n
        b=b+i
    if b==a:
        return True
    else:
        return False
        

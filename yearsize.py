def yearsize(a):
    if a%400==0:
        return 366
    elif a%100==0:
        return 365
    elif a%4==0:
        return 366
    else:
        return 365

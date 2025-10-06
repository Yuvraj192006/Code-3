def isperfect(a):
    if a<=1:
        return False
    sum_divisor=0
    for i in range(1,a):
        if a%i==0:
            sum_divisor=sum_divisor+i
    if sum_divisor==a:
        return True
    else:
        return False

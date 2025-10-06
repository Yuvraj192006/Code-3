def ator(n):
    if n<=0 or n>3999:
        return None
    roman=""
    while n>=1000:
        roman+="M"
        n=n-1000
    while n>=900:
        roman+="CM"
        n=n-900
    while n>=500:
        roman+="D"
        n=n-500
    while n>=400:
        roman+="CD"
        n=n-400
    while n>=100:
        roman+="C"
        n=n-100
    while n>=90:
        roman+="XC"
        n=n-90
    while n>=50:
       roman+="L"
       n=n-50
    while n>=40:
        roman+="XL"
        n=n-40
    while n>=10:
        roman+="X"
        n=n-10
    while n>=9:
        roman+="IX"
        n=n-9
    while n>=5:
        roman+="V"
        n=n-5
    while n>=4:
        roman+="IV"
        n=n-4
    while n>=1:
        roman+="I"
        n=n-1
    return roman
    
    

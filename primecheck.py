def isPrime(a):
    if (a<=1):
        return "No"
    if (a==2):
        return "Yes"
    if (a%2==0):
        return "No"
    
    k=round(a**0.5)
    for j in range(2,k+1):
        if(a%j==0):
            return "No"
    return "Yes"

a = int(input("Enter the number for prime check: "))
print(isPrime(a))
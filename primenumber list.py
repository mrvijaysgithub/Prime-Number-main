def prime(a,l):
    
    if (a<=1):
        return None
    if (a==2):
        return l.append(a)
    if (a%2==0):
        return None
    
    k=round(a**0.5)
    for j in range(2,k+1):
        if(a%j==0):
            return None
    return l.append(a)
list1=[]
s=int(input('Enter the starting value: '))
e=int(input('Enter the ending value: '))
for i in range(s,e):
    prime(i,list1)
print(list1)

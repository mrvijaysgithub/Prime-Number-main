def prime(a,l):
    k=round(a**0.5)
    for j in range(2,k+1):
        if(a%j==0):
            return None
    return l.append(a)
list1=[]
s=-40
e=500
if s<=2:
    s=3
    list1.append(2)
for i in range(s,e,2):
    prime(i,list1)
print(list1)

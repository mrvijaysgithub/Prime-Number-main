# limit is the constain change accordingly
limit = 1000000
# Creating a list for sum
suml = [0] * limit
# Creating a list for true and false
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        suml[i] = suml[i-1] + i
        # changing the value as false for all the multiple
        for n in range(i*i, limit, i):
            a[n] = False
    else:
        suml[i] = suml[i-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(suml[n])
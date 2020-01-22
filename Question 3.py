mysum= 0
for i in range(0,101):
    mysum +=i
print (mysum)


def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(100))
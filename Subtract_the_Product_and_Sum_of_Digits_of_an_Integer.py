n=int(input())
s=0
m=1
while n>0:
    r=n%10
    m*=r
    s+=r
    n=n//10
print(m-s)    
n=int(input())
t=n
s=n**2
d=0
while n>0:
    n=n//10
    d+=1
m=s%10**d
if m==t:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
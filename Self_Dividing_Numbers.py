a=int(input())
b=int(input())
for i in range(a,b+1):
    r=i
    while r>0:
        d=r%10
        if d==0 or i%d!=0:
            break
        r=r//10
    if r==0:
        print(i,end = ' ')
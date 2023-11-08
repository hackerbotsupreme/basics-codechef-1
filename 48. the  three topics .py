# cook your dish here
a,b,c,x=(map(int,input().split()))
#x=int(input())
if x==a or x==b or x==c:
    print("YES")
else:
    print("NO")




# cook your dish here
a,b,c,x=map(int,input().split())
k=[]
k.append(a)
k.append(b)
k.append(c)
if x in k:
        print("YES")
else:
        print("NO")




a=list(set(map(int,input().split())))
l=len(a)
if l==4:
    print("no")
else:
    print("yes")
        
        

i=int(input())
while i>0:

    a,b,c=[int (a) for a in input().split()]
    if ((b*1+c*2)>=a):
        print("Qualify")
    else:
        print("NotQualify")
    i=i-1
    
    

T = int(input())
for tc in range(T):
   X,A,B=input().split()
   X=int(X)
   A=int(A)
   B=int(B)
   N=int(A+(B*2))
   if(N>=X):
      print("Qualify")
   else:
      print("NotQualify")



# cook your dish here
t=int(input())
for i in range(t):
        x,a,b=map(int,input().split())
        print("Qualify") if (a+2*b>=x) else print("Notqualify")
        
        
# cook your dish here
t=int(input())
for i in range(t):
    x,a,b=map(int,input().split())
    b*=2
    if(x<=(a+b)):
        print("Qualify")
    else:
        print("NotQualify")
        
        
        
for _ in range(int(input())):
    x,a,b = map(int,input().split())
    if (a*1) + (b*2) >= x:
        print('Qualify')
    else:
        print('NotQualify')
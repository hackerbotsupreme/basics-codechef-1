t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    dic={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,
    '7':3,'8':7,'9':6}
    c=a+b
    c=str(c)
    ans=0
    for i in c:
        ans+=dic[i]
    print(ans)
        
        
        
        
        
        
        
        
        
t=int(input())
s=""
sum=0
for i in range(t):
    a,b=map(int,input().split(" "))
    s=str((a+b))
    sum=0
    for j in s:
        if(j=="1"):
            sum+=2
        elif(j=="7"):
            sum+=3
        elif(j=="4"):
            sum+=4
        elif(j=="2" or j=="3" or j=="5"):
            sum+=5
        elif(j=="0" or j=="6" or j=="9"):
            sum+=6
        elif(j=="8"):
            sum+=7
    print(sum)













L1 = [2, 3, 5]
L2 = [0, 6, 9]
L3 = [1, 4, 7,8]
t = int(input())
for i in range(t):
    A, B = map(int,input().split())
    Sum = A + B
    total = 0
    while (Sum > 0):
        n = Sum % 10
        Sum = Sum // 10

        if n in L1:
            total = total + 5
        elif n in L2:
            total = total + 6
        elif (n == 1):
            total = total + 2
        elif (n == 4):
            total = total + 4
        elif(n==8):
            total=total+7
        else:
            total = total + 3
    print(total)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
Dict = {0: 6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6 }
for _ in range(int(input())):
  a,b=map(int,input().split())
  n=a+b
  c=0
  while n:
    digit = n % 10
    n //= 10
    c=c+Dict[digit]
  print(c)
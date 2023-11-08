# cook your dish here
T = int(input())
for tc in range(T):
    n = int(input())
    arrA = list(map(int,input().split()))
    arrB = list(map(int,input().split()))
    
    streak = 0
    maxstreak = 0
    
    for i in range(n):
        if arrA[i] > 0 and arrB[i] > 0:
            streak += 1
        else:
            streak = 0
        
        if streak > maxstreak:
            maxstreak = streak
        
    print(maxstreak)
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    st=0;maxst=0
    for i in range(n):
        if a[i]!=0 and b[i]!=0:
            st+=1;
        elif a[i]==0 or b[i]==0:
            maxst=max(maxst,st)
            st=0
    maxst=max(maxst,st)
    print(maxst)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dev=shiv=0
    for i in range(n):
        if a[i]==0 or b[i]==0:
            dev=max(dev,shiv)
            shiv=0
        else:
            shiv+=1
    dev=max(dev,shiv)
    print(dev)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for i in range(int(input())):
    days= int(input())
    chef_sent = list(map(int, input().split(" ")))
    chefina_sent = list(map(int, input().split(" ")))
    streak, max_streak = 0, 0
    for j in range(len(chef_sent)):
        if(chef_sent[j] == 0 or chefina_sent[j] == 0):
            streak = 0
        else:
            streak += 1
        if(max_streak < streak):
            max_streak = streak
    print(max_streak)
    
# cook your dish here
for i in range(int(input())):
    s = input()
    print(s.count('4'))
    
    
    
    
    
    
    
    
T = int(input())
for i in range(T):
    a = int(input())
    c = 0
    while(a>0):
        rem = a%10
        if (rem == 4):
            c = c+1
        a = a//10
    print(c)
        
        
        
        
        
        
        
        
        
        
        
        
        
for _testcase in range(int(input())):
    a = input()
    print(a.count('4'))
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
x=[]

for i in range(0,t):
    x.append(int(input()))
for j in x:
    c=0
    k=str(j)
    for g in k:
        if(g=="4"):
            c+=1 
    print(c)
        
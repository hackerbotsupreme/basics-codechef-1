# cook your dish here
t=int(input())
for i in range(t):
    sa,sb,sc=map(int,input().split())
    if sa < sb and sa <sc:
        print("draw")
    elif sb<sa and sb <sc:
        print("Bob")
    else:
        print("Alice")
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
t = int(input())
ans = ''

for i in range(t):
    s = list(input())
    t = list(input())
    for j in range(len(s)):
            if s[j] == t[j]:
                ans += 'G'
            else:
                ans += 'B'
    print(ans)
    ans = ''
    
    
    
    
    
    
    
    
    
    
# Wordle
for i in range(int(input())):
    a=''
    s=list(input())
    t=list(input())
    for j in range(0,len(t)):
        if(s[j]==t[j]):
            a+='G'
        else:
            a+='B'
    print(a)    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    a=''
    s=list(input())
    t=list(input())
    for j in range(0,len(s)):
        if s[j]==t[j]:
            a+='G'
        else:
            a+='B'
    print(a)
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    m=input()
    d=len(s)
    a=''
    for j in range(0,d):
        if(s[j]==m[j]):
            a+='G' 
        else:
            a+='B' 
    print(a)
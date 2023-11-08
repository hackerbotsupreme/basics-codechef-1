# cook your dish here
N=int(input())
a=list(map(int,input().split()))
e=0
o=0
for i in a:
        if i%2==0:
            e+=1# -*- coding: latin-1 -*-
        else:
            o+=1
            
if e>o:
        print("READY FOR BATTLE")
else:
        print("NOT READY")





n = int(input())
    
w = list(map(int, input().split()))
    
l = 0
    
for x in w:
    if x % 2 == 0:
        l += 1
            
if l > (n-l):
    print('READY FOR BATTLE')
else:
    print('NOT READY')
    
    
    
    
# cook your dish here
n = int(input())
N = list(map(int,input().split()))
e =0
o = 0
for i in N:
    if(i%2!=0):
        o+=1 
    else:
        e+=1 
if(o>=e):
    print("NOT READY")
else:
    print("READY FOR BATTLE")
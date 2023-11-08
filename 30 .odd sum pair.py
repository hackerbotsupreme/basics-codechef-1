goals = int(input())
for distractions in range(goals):
    wife, life, knife = map(int, input().split())
    if (wife + life) % 2 == 1:
        print('YES')
    elif (wife + knife) % 2 == 1:
        print('YES')
    elif (life + knife) % 2 == 1:
        print('YES')
    else:
        print('NO')
        
        
        
        
        
#for 2 or more numbers

test_case = int(input())
for _ in range(test_case):
    x = list(map(int, input().split()))
    nl = len(x)


    def check_even_or_odd():
        for i in x:
            if i % 2 == 0:
                return "even"
            else:
                return "odd"


    def check_for_odd():
        for i in range(1, nl):
            if x[i] % 2 != 0:
                return True


    def check_for_even():
        for i in range(1, nl):
            if x[i] % 2 == 0:
                return True


    if check_even_or_odd() == "even":
        if check_for_odd():
            print("yes")
        else:
            print("no")
    elif check_even_or_odd() == "odd":
        if check_for_even():
            print("yes")
        else:
            print("no")







# cook your dish here
t=int(input()) 
for i in range(t): 
    a,b,c=map(int,input().split())
    if (a+b)%2!=0 or (b+c)%2!=0 or (c+a)%2!=0:
        print("YES")
    else : 
        print("NO")
    






# cook your dish here
t=int(input())
for i in range(t):
        A,B,C=map(int,input().split())
        if((A+B)%2!=0 or (B+C)%2!=0 or (A+C)%2!=0):
                print("YES")
        else:
                print("NO")
                
                
                
                
                
                
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    odd=0
    even=0
    for j in a:
        if j%2==0:
            even+=1
        else:
            odd+=1
    if even>0 and odd>0:
        print("Yes")
    else:
        print("No")




























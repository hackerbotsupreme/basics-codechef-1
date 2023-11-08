a=int(input())
for i in range(a):
    count=0
    b=input()
    for i in b:
        if int(i)==4:
            count=count+1
    print(count)
    
    
    
    
    
    
    
    
# cook your dish here 
for _ in range(int(input())):
    l=input()
    a=0
    for i in l:
        if int(i)==4:
            a+=1
    print(a)
    
    
    
    
    
    
    
    
    
T = int(input())
for i in range(T):
    arr = str(input())
    l = []
    for i in arr:
        if i == '4':
            l.append(i)
    print(len(l))





# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal
x=int(input())
for e in range(x):
    y=int(input())
    s=str(y)
    a=s.count('4')
    print(a)
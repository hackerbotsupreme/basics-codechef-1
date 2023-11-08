for _ in range(int(input())):
    x,y=map(int,input().split())
    z=list(map(int,input().split()))
    z.sort()
    print(z[x-y]-1)
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    arr=[]
    for i in range(x):
        max1=max(a)
        arr.append(max1)
        a.remove(max1)
        i-=1
    min1=min(arr)
    print(min1-1)
    
    
    
    
    
    
    
    
    
    
    
    
for i in range(int(input())):
    x,n=map(int,input().split())
    l=list(map(int,input().strip().split()))
    l=sorted(l)
    l1=l[::-1]
    print(l1[n-1]-1)
    
    
    
    
    
    
    
    
    
# cook your dish here
T = int(input())
for i in range(T):
    N,X = map(int,input().split())

   
    marks = list(map(int, input().split()))

    # Sorting marks in descending order
    marks.sort(reverse=True)

    # Printing minimum passing marks
    print(marks[X-1]-1)
    
    
    
    
    
    
    
    
    
    
    
T = int(input())

for i in range(T):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    passing_mark = A[N - X]

    print(passing_mark-1)
    

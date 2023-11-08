# cook your dish here
for _ in range(int(input())):
    n, money = map(int, input().split())
    L = list(input().split())
    for i in range(n):
        L[i] = int(L[i])
        
    ns = ""
    for i in range(n):
        if (L[i] <= money):
            ns += "1"
            money -= L[i]
        else:
            ns += '0'
    
    print(ns)
    
    
    
    
    
    
    
    
# cook your dish here
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = ""
    for i in range(N):
        if K >= A[i]:
            K -= A[i]
            result += "1"
        else:
            result += "0"
    print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
T = int(input())

for tc in range(T):
    
    (peopleInLine, atmTotal) = list(map(int, input().split(' ')))
    amountToTakeOut = list(map(int, input().split(' ')))
    satisfactionReport = ''
    
    for i in range(peopleInLine):
        if amountToTakeOut[i] <= atmTotal:
            satisfactionReport += '1'
            atmTotal -= amountToTakeOut[i]
        else:
            satisfactionReport += '0'

    print(satisfactionReport)
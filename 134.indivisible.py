for t in range(int(input())):
    a, b, c = map(int, input().split())
    for k in range(1, 100):
        if a%k != 0 and b%k != 0 and c%k != 0:
            print(k)
            break
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
        a,b,c=map(int,input().split())
        for i in range(1,100):
                if (a%i!=0 and b%i!=0 and c%i!=0):
                        print(i)
                        break
                    
                    
                    
                    
                    
                    
                    
def main():
    T = int(input())
    while T > 0:
        non_divisible_num()
        T -= 1

def non_divisible_num():
    A, B , C = map(int, input().split())
    i = 2
    while i < 100:
        if (((A % i) != 0) and ((B % i) != 0) and((C % i) != 0)):
            print (i)
            break
        i += 1

main()













for _testcase in range(int(input())):
    x,y,z = map(int,input().split()) 
    for i in range(2,100):
        if x%i != 0 and y%i != 0 and z%i != 0:
            print(i)
            break
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int,input().split())
    for i in range(2,100):
        if(a%i!=0 and b%i!=0 and c%i!=0):
            print(i)
            break
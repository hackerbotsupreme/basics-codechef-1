for _ in range(int(input())):
    n = int(input())
    s = input()
    if n<=3:
        print("YES")
    else:
        for i in range(n-3):
            string = s[i:i+4]
            vow1 = 'a' in string or 'e' in string or 'i' in string 
            vow2 = 'o' in string or 'u' in string 
            if not vow1 and not vow2:
                print("NO")
                break 
        else:
            print("YES")
        
    
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for t in range(int(input())):
    n=int(input())
    st=input()
    c=0
    flag=False
    vowels=['a','e','i','o','u']
    for i in st:
        if i not in vowels:
            c+=1
        else:
            c=0
        if c>=4:
            flag=True
    if flag:
        print("NO")
    else:
        print("YES")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
T = int(input())
for i in range(T):
    n = int(input())
    s = str(input())
    vowel = ['a','e','i','o','u']
    hardness = 0
    for j in range(n):
        if s[j] not in vowel:
            hardness = hardness + 1
            if hardness == 4:
                break
        else:
            hardness=0
    if hardness < 4:
        print('yes')
    else:
        print('no')
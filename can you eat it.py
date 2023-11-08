# cook your dish here
t=int(input())
for _ in range(t):
    x=input()
    a="Sad"
    for i in range(len(x)-2):
        if x[i] in {'a','e','i','o','u'}:
            if x[i+1] in {'a','e','i','o','u'}:
               if x[i+2] in {'a','e','i','o','u'}:
                   a="Happy"
                   break
    print(a) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
T = int(input())
VOWELS = ['a', 'e', 'i', 'o', 'u']

for tc in range(T):
    string = input()
    string = [x for x in string]
    
    for i in range(len(string)-2):
        chefIsFeeling = "Sad"
        x = i+1
        y = i+2
        
        if string[i] in VOWELS and string[x] in VOWELS and string[y] in VOWELS:
            chefIsFeeling = "Happy"
            break
    print(chefIsFeeling)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
 
for i in range(int(input())):
    v="aeiouAEIOU"
    s=input()
    l=len(s)
    c=0
 
    for j in range(l):
        if s[j]in v:
            c=c+1
        else:
            c=0
        if c==3:     
          print("Happy")
          break
          
    if c<3:
       print("Sad")
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
T=int(input())
for _ in range(T):
    st=input()
    vwl=['a','e','i','o','u']
    flag=''
    for i in st:
        res=i in vwl
        flag=flag+str(res)
    if "TrueTrueTrue" in flag:
        print("Happy")
    else:
        print("Sad")
    
    
    
    
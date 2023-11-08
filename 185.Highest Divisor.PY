n = int(input())
i = 1
while i < 10:
    if n % i == 0:
        c = i
    i+=1
print(c)












# cook your dish here
n=int(input())
l=[]
for i in range(1,11):
    if(n%i==0):
        l.append(i)
print(max(l))










# cook your dish here
N = int(input())
l = []
for i in range(1,11):
  if N % i == 0:
    l.append(i)
print(max(l))
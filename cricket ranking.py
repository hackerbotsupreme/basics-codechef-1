for _testcase in range(int(input())):
    a,b,c = map(int, input().split())
    d,e,f = map(int, input().split())
    acount = 0
    bcount = 0
    if a > d: acount += 1
    else: bcount += 1
    if b > e: acount += 1
    else: bcount += 1
    if c > f: acount += 1
    else: bcount += 1
    
    if acount > bcount: print('A')
    else:               print('B')
    
    
    
    
    
    
    
    
    
    
    
    
    
# cook your dish here
for t in range(int(input())):
    r1,w1,c1 = map(int,input().split())
    r2,w2,c2 = map(int,input().split())
    d1 =0
    d2 =0
    if(r1>r2):
        d1+=1 
    else:
        d2+=1
    if(w1>w2):
        d1+=1 
    else:
        d2+=1
    if(c1>c2):
        d1+=1 
    else:
        d2+=1
    if(d1>d2):
        print("A")
    else:
        print("B")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
from functools import reduce
from collections import Counter, UserString
from math import log2, lcm, gcd as hcf

mod = lambda n : int(n % ((10 ** 9) + 7))

_fc = [1]
for i in range(1,1000001):
    _fc.append(i * _fc[i - 1])
    _fc[i] = mod(_fc[i])

def fact(n):
    if -1000001 < n < 1000001:
        if n > -1:
            return _fc[n]
        else:
            return -_fc[abs(n)]

    else:
        raise ValueError("values only from 1000000 to -1000000 can be factorialized\n")

def wonky(s, rev = False):
    if not rev:
        return ''.join([s[i].lower() if i % 2 == 0 else s[i].upper() for i in range(len(s))])
    return ''.join([s[i].upper() if i % 2 == 0 else s[i].lower() for i in range(len(s))])

def yn(b, caps = False, y = "Yes", n = "No"):
    if b:
        returning = y
    
    else:
        returning = n
    
    if caps == 2:
        return returning.lower()
    
    elif caps == 3:
        return wonky(returning)
    
    elif caps == 32:
        return wonky(returning, True)
    
    elif caps:
        return returning.upper()
    
    return returning

def prob(l, n):
    return l.count(n) / len(l)

def pairSum(l, k):
    returning = []
    check = set()
    for i in l:
        temp = k - i
        if n in check:
            returning.append((k - temp, temp))
        check.add(i)
    return returning

def isSubseq(s1, s2):
    n,m = len(s1),len(s2)
    i,j = 0,0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1
    return i == n

def isPrime(n):
    if(n > 1):
        for i in range(2, int(n ** 0.5) + 1):
            if not n % i:
                return False

        else:
            return True
    
    return True

def percentDiff(n, diff):
    return n + (n * (diff / 100))

def prodLst(l1, nl):
    if isinstance(nl, int):
        return [i * nl for i in l1]
    else:
        return [i * j for i, j in zip(l1, nl)]

def divLst(l1, nl, mxMn = False):
    if isinstance(nl, int):
        return [i // nl for i in l1]
    else:
        if mxMn:
            return [max(i,j) // min(i,j) for i, j in zip(l1, nl)]
        else:
            return [i // j for i, j in zip(l1, nl)]

def modLst(l, n):
    return [i % n for i in l]

def sumLst(l1, nl):
    if isinstance(nl, int):
        return [i + nl for i in l1]
    else:
        return [i + j for i, j in zip(l1, nl)]

def absLst(l):
    return [abs(i) for i in l]

def diffLst(l1, nl, isAbs = False):
    if isinstance(nl, int):
        returning = [i - nl for i in l1]
    else:
        returning = [i - j for i, j in zip(l1, nl)]
    if isAbs:
        return absLst(returning)
    else:
        return returning

def remCommonOccurs(l, remLst):
    srl = set(remLst)
    returning = []
    for i in l:
        if i not in remLst:
            returning.append(i)
    return returning

def remPosNeg(l, posNeg = False):
    returning = []
    if not posNeg:
        for i in l:
            if i >= 0:
                returning.append(i)
    else:
        for i in l:
            if i < 0:
                returning.append(i)
    return returning

def flip(nl):
    if isinstance(nl, int):
        return -nl
    elif isinstance(nl, list):
        return [-i for i in nl]

def prod(l):
    return reduce(lambda x, y : x * y, l)

def subtract(l,isRevSorted = False):
    _l = l
    if isRevSorted:
        _l = sorted(_l)[::-1]
    returning = _l[0]
    for i in range(1, len(_l)):
        returning -= _l[i]
    return returning

def ev(n):
    return not(n&1)

def decimal(n):
    returning = int(n)
    if list(set(str(n)[(str(n).index('.') + 1) :])) == ['0']:
        return returning
    else:
        return returning + 1

def printdeci(n):
    print(decimal(n))

def printWonk(s):
    print(wonky(s))

def printWonkRev(s):
    print(wonky(s, True))

def printabs(n):
    print(abs(n))

def pr_int(fs):
    print(int(fs))

def printMax(*l):
    print(max(l))

def printMin(*l):
    print(min(l))

def printm(n):
    print(mod(n))

def printy(b, caps = False, y = "Yes", n = "No"):
    print(yn(b, caps, y, n))

def simplify(n, d):
    _div = hcf(n, d)
    _n = n // _div
    _d = n // _div
    return _n, _d
    

class mutableStr(UserString):
    
    def ins(self, n, s):
        if n < 0:
            self.data = self.data = ''.join(list(self.data)[: n + 1]) + s + ''.join(list(self.data)[n + 1 :])

        else:
            self.data = ''.join(list(self.data)[: n]) + s + ''.join(list(self.data)[n :])
    
    def rem(self, s): 
        self.data = self.data.replace(s, "")

alphabetOrd = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
alphabet = list("abcdefghijklmnopqrstuvwxyz")

listToStr = lambda l : ''.join(map(str, l))
bint = lambda b : int(str(b), 2)
r2 = lambda n : range(1, n + 1)
rl = lambda *l : range(len(l[0])) if len(l) == 1 else range(l[0], len(l[1]))
alph = lambda s : s.isalpha()
sl = lambda l : list(set(l))

inf = float('inf')

soli = lambda : sorted(map(int, input().split()))
sosi = lambda : sorted(input())
ii = lambda : int(input())
li = lambda : list(map(int, input().split()))
si = lambda : mutableStr(str(input()))
lsi = lambda : list(input())
sepi = lambda _type = int : map(_type, input().split())
seti = lambda : set(map(int, input().split()))

for t in range(int(input())):
    
    # Taking input for each testcase:
    
    playerAStats = li()
    playerBStats = li()
    
    superiorStats = 0
    
    for i in rl(playerAStats):
        if playerAStats[i] > playerBStats[i]:
            superiorStats += 1
        
        else:
            superiorStats -= 1
    
    # Outputting the answer:
    
    printy(superiorStats >= 0, 1, 'a', 'b')
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int r1,w1,c1;
	    int r2,w2,c2;
	    
	    cin >> r1 >> w1 >> c1;
	    cin >> r2 >> w2 >> c2;
	    
	    int a=0,b=0;
	    
	    if(r2>r1)
	    b++;
	    else
	    a++;
	    
	    if(w2>w1)
	    b++;
	    else
	    a++;
	    
	    if(c2>c1)
	    b++;
	    else
	    a++;
	    
	    if(a>b)
	    cout << "A" << endl;
	    else
	    cout << "B" << endl;
	    
	    
	}
	return 0;
}


















#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin >> t;
	while(t--)
	{
	    int r1,w1,c1;
	    int r2,w2,c2;
	    
	    cin >> r1 >> w1 >> c1;
	    cin >> r2 >> w2 >> c2;
	    
	    int a=0,b=0;
	    
	    if(r2>r1)
	    b++;
	    else
	    a++;
	    
	    if(w2>w1)
	    b++;
	    else
	    a++;
	    
	    if(c2>c1)
	    b++;
	    else
	    a++;
	    
	    if(a>b)
	    cout << "A" << endl;
	    else
	    cout << "B" << endl;
	    
	    
	}
	return 0;
}
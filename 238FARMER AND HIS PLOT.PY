# cook your dish here
for i in range(int(input())):
    a,b=map(int,input().split())
    for j in range(1,min(a,b)+1): 
        if a%j==0 and b%j==0:
            m=j 
    print((a*b)//(m*m))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#include <stdio.h>

int main(void) {
  int T;
  scanf("%i", &T);
  while (T--) {
    int l, b;
    scanf("%i %i", &l, &b);
    for (int i = l; i > 0; i--) {
      if ((l % i == 0) && (b % i == 0)) {
        printf("%i\n", (l / i) * (b / i));
        break;
      }
    }
  }
  return 0;
}










#include <stdio.h>

int main(void) {
  int T;
  scanf("%i", &T);
  while (T--) {
    int l, b;
    scanf("%i %i", &l, &b);
    for (int i = l; i > 0; i--) {
      if ((l % i == 0) && (b % i == 0)) {
        printf("%i\n", (l / i) * (b / i));
        break;
      }
    }
  }
  return 0;
}
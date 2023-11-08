# cook your dish here
n,m,k=map(int,input().split())
i=1
c=0
while(i<=n):
    s=list(map(int,input().split()))
    # print(s)
    i+=1
    if sum(s)-s[k]>=m and s[k]<=10:
        c+=1
print(c)














#include <stdio.h>

int main(void) {
	// your code goes here
	int N,M,K;
	scanf("%d %d %d",&N,&M,&K);
	int Q,I,total=0;
	while(N--)
	{
	  int A[K],sum=0;
	  for(I=0;I<K;I++)
   	  {
	      scanf("%d",&A[I]);
	      sum=sum+A[I];
	  }
	  scanf("%d",&Q);
	  if(sum>=M && Q<=10)
	  total++;
	}
	printf("\n%d",total);
	return 0;
}

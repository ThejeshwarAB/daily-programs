//sourcecode
#include<stdio.h>
#include <stdlib.h>

int main()
{
int n,i,j;
scanf("%d",&n);
for(i=1;i<=n;i++)
{
for(j=1;j<=n;j++)
printf("%d ",i*j);
printf("\n");
}
}
//n multiples of n until n

/*
Sample IP:
4

Sample OP:
1 2 3 4 
2 4 6 8 
3 6 9 12 
4 8 12 16 
*/

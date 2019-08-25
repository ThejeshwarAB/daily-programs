//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
int n,k,a[100000];
int i,j;
scanf("%d %d",&n,&k);
for(i=0;i<n;i++)
scanf("%d",&a[i]);
int s=0;
for(i=0;i<k;i++)
s+=a[i];
for(i=n-k;i<n;i++)
printf("%d ",s-a[i]);
}
//specific difference of subarray sum

/*
Sample IP:
6 4
1 2 3 4 5 6

Sample OP:
7 6 5 4 
*/

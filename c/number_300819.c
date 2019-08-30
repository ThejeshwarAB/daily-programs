//sourcecode
#include<stdio.h>
#include <stdlib.h>
int c=0;

int isPrime(int n)
{
    c=0;
    for(int i=2;i<n;i++)
    if(n%i==0)
    c++;
    return c;
}
main()
{
int n,i;
scanf("%d",&n);

for(i=2;i<=n;i++)
if(!isPrime(i))
printf("%d ",i);

printf("\n");

for(i=2;i<=n;i++)
if(isPrime(i))
printf("%d ",i);
}
//print prime,composite until input no.

/*
Sample IP:
10

Sample OP:
2 3 5 7
4 6 8 9 10
*/

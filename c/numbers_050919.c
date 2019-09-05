//sourcecode
#include<stdio.h>
main()
{
int n,l;
scanf("%d",&n);
l=n%10;
while(n%10)
n=n/10;
printf("%d%d",n,l);
}
//print first and last digit

/*
Sample IP:
1824

Sample OP:
14
*/

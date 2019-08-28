//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
    int a,b[100];
    scanf("%d",&a);
    int i,j,s=0,n;
    while(a)
    {
        s=s*10+(a%10);
        a/=10;i++;
    }
    n=i;
    for(i=0;i<n;i++)
    {
        b[i]=s%10;
        s/=10;
    }
    for(i=0;i<n-1;i++)
    for(j=0;j<b[i+1];j++)
    printf("%d",b[i]);
}
//print present digit for next digit no. of times
//ignore the last digit of the no. while printing

/*
Sample IP:
432
 
Sample OP:
44433
*/

//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
int n,s=0,a; char c;
scanf("%d",&n);
while(n)
{
    scanf("%d%c",&a,&c);
    s+=a;n--;
}
printf("%d",s);
}
//accept n no. of nums and chars.
//print the sum of nums as output

/*
Sample IP:
3
1a20b300c

Sample OP:
321
*/

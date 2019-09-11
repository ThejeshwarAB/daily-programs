//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
int a,o,e,i,p,q;
o=e=p=q=0;
while(scanf("%d",&a)==1)
{
    if(a%2)
    {
        o+=a;
        p++;
    }
    else if(a!=0)
    {
        e+=a;
        q++;
    }
}
if(q)
printf("%d",e);
else
printf("-1");
if(p)
printf("\n%.1f",(float)o/p);
else
printf("\n-1");
}
//find number of odd
//find number of evn
//print even sum
//print odd aveg
//else prints -1
//neglect zeroes

/* 
Sample IP:
1 2 3 4

Sample OP:
6     (2+4)
2.0   ((1+3)/2)
*/

//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
int x,y,i,p;
scanf("%d %d",&x,&y);
p=y;
if(x>y)
p=x;
for(i=1;i<=10;i++)
printf("%d ",p*i);
}
//find max of x,y as p
//print 10 multps of p

/*
Sample IP:
2 1

Sample OP:
2 4 6 8 10 12 14 16 18 20
*/

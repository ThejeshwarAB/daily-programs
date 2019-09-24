//sourcecode
#include<stdio.h>
#include <stdlib.h>
main()
{
int a,b,c,d,e;
scanf("%d*%d+%d-%d*%d",&a,&b,&c,&d,&e);
int f=(a*((b+c)-d)*e);
printf("%d",f);
}
//use precedence +,-,*

/*
Sample IP:
1*0+0-1*1

Sample OP:
-1
{
1*((0+0)-1)*1)
}*/

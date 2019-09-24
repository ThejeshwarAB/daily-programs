//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
    int a,b,c;
    scanf("%d %d.%d",&a,&b,&c);
    printf("%d.%d",a*b,a*c);
}

/*
Sample IP:
4 2.0

Sample OP:
8.0
{
4*2
4*0
}
*/

//sourcecode
#include<stdio.h>
#include <stdlib.h>
main()
{
char a[10000];
scanf("%s",a);
int i,j;
char t=a[strlen(a)-1];
for(i=0;i<strlen(a);i++)
if(a[i]==t)
a[i]='0';
printf("%d",atoi(a));
}
//last digit of no.as t
//replace all t as zero
//print altered integer

/*
Sample IP:
10201

Sample OP:
20
(00200)
*/

//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
char x,y;
int p=1;
scanf("%c %c",&x,&y);
if(x>y)
p=-1;
for(char a=x;;a+=p)
{if(a!='a'&&a!='e'&&a!='i'&&a!='o'&&a!='u')
printf("%c ",a);
if(a==y)
break;}
}
//print consonants in range x and y

/*
Sample IP:
e a

Sample OP:
d c b
*/

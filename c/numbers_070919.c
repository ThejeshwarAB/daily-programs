//sourcecode
#include<stdio.h>
#include <stdlib.h>
int main()
{
int a[100],i,c,d,x,y,n;
scanf("%d",&n);
for(i=0;i<n;i++)
scanf("%d",&a[i]);
scanf("%d %d",&x,&y);
for(i=0;i<n;i++)
if(a[i]%x==0)
{c=i;break;}
for(i=0;i<n;i++)
if(a[i]%y==0)
{d=i;}
int t=a[c];
a[c]=a[d];
a[d]=t;
for(i=0;i<n;i++)
printf("%d ",a[i]);
}
//find first multiple of x
//&find last multiple of y
//swap both and print them

/*
Sample IP:
6
2 4 5 11 22 8
2 11

Sample OP:
2 22
*/

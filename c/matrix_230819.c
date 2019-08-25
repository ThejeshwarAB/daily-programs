//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
int a[1000][1000],b[1000],n,i,j;
scanf("%d",&n);
for(i=0;i<n;i++)
{b[i]=0;
for(j=0;j<n;j++)
{scanf("%d",&a[i][j]);
if(a[i][j]==1)b[i]++;}
}
int max=-1;int y;
for(i=0;i<n;i++)
if(b[i]>max)
{max=b[i];y=i+1;}
printf("%d",y);
}

/*
Sample IP:
4 4
1 0 0 0 
1 1 1 1 
1 0 1 0 
0 0 1 0
Sample OP:
2
*/

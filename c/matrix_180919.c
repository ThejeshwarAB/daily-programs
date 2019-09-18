//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
int a[100][100],n;
scanf("%d",&n);
int i,j;
for(i=0;i<n;i++)
for(j=0;j<n;j++)
scanf("%d",&a[i][j]);
if(n%2==0)
{
    for(j=0;j<n;j++)
    {
    for(i=0;i<n;i++)
    if(j==0||j==n-1)
    printf("%d ",a[i][j]);
    printf("\n");}
}
else
{
    for(i=0;i<n;i++)
    {
    for(j=0;j<n;j++)
    if(i==0||i==n-1)
    printf("%d ",a[i][j]);
    printf("\n");}
}
}
//print first, last row if n is odd
//print first, last col if n is evn

/*
Sample IP:
3
1 2 3 
4 5 6 
7 8 9

Sample OP:
1 2 3
7 8 9
*/

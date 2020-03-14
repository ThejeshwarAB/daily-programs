//sourcecode
#include<stdio.h>
#include <stdlib.h>

int main()
{
int r,c;
scanf("%d %d\n",&r,&c);
int i,j;
char s[200][200];
for(i=0;i<r;i++)
if(i%2==0)
for(j=0;j<c;j++)
scanf("%c ",&s[i][j]);
else
for(j=c-1;j>=0;j--)
scanf("%c ",&s[i][j]);
for(i=0;i<r;i++){
for(j=0;j<c;j++)
printf("%c",s[i][j]);}
}

/*
Sample IP:
4 4
appr 
nehe
sive
ssen

Sample OP:
apprehensiveness
*/

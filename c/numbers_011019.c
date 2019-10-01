//sourcecode
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
main()
{
int cex,cey,cx,cy;
scanf("%d %d\n%d %d",&cex,&cey,&cx,&cy);
double r,a,pi=22/7.0;
r=sqrt(((cex-cx)*(cex-cx))+((cey-cy)*(cey-cy)));
printf("%.2f",pi*r*r);
}
//given two pair of coordinates
//first pair denotes center cos
//second pair denotes circum co
//calculate radius, area values
//print 2 pt precise area value

/*
Sample IP:
0 0 
1 0

Sample OP:
3.14
*/

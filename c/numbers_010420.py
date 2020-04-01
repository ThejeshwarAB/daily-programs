//sourcecode
#include<stdio.h>
#include<stdlib.h>
main()
{
unsigned long long n,s,p;
scanf("%llu",&n);
int i=0,t=n,m=0;
while(m<t)
{
    s=0;
    p=1;
    if(m%2==1){
    for(i=1;i<n;i++){
    p*=i;
    printf("%llu*",i);}
    p*=i;
    printf("%llu=%llu",i,p);
    n--;
    }
    else{
    for(i=1;i<n;i++){
    s+=i;
    printf("%llu+",i);}
    s+=i;
    printf("%llu=%llu",i,s);
    n--;
    }
    m++;
    printf("\n");
}
}
//print the following pattern

/*
Sample IP:
3

Sample OP:
1+2+3=6
1*2=2
1=1
*/

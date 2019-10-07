#include<stdio.h>
main()
{
    int N;
    scanf("%d",&N);
    for(int ctr=1; ctr <= N; ++ctr)
    {
      if(N%ctr == 0)
      {
      if(ctr%2 != 0)
        printf("%d ",ctr);
      }
    }
}
//print odd factors only

/* 
Sample IP:
10

Sample OP:
1 5
*/

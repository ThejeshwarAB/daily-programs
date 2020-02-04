#sourcecode
n=int(input())
for i in range(n,0,-1):
    for j in range(n):
        if i==j+1 or (i==n and j==0) or (i==1 and j==n-1):
            print("%",end='')
        else:
            print("-",end='')
    print(end='\n')
#percentage pattern

'''

Sample IP:
5

Sample OP:
%---%
---%-
--%--
-%---
%---%

'''

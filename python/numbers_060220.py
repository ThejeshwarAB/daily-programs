#sourcecode
n,m=map(int,input().split())
l,s=[],0
for i in range(n):
    l=list(map(int,input().split()))
    x=[]
    for j in l:
        x.append(j)
    l.sort()
    if x==l:
        s+=1 
print(s)
#print no. of sorted rows in 2d array

''' 
Sample IP:
3 5
1 2 3 4 5
2 3 4 5 6 
1 3 2 4 5

Sample OP:
2
'''

#sourcecode
n,c=input(),0
l=list(map(str,input().split()))
for i in range(len(n)-1):
    if len(l[i])>len(l[i+1]):
        c=1
if c==0:
    print("Yes")
else:
    print("No")
#check if the input len is in asc. ord
#if yes print yes and if else print no

'''
Sample IP:
5
a ab abc

Sample OP:
Yes
'''
